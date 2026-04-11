#!/usr/bin/env python3
"""
sync_gdd.py — Sincroniza advento-gdd/src/ADVENTO → advento-journey/docs/
e regenera o mkdocs.yml com a navegação atualizada.

Inclui suporte a imagens no formato Obsidian (![[img.png]]):
- Copia as imagens para docs/assets/images/
- Reescreve os links para markdown padrão com caminho relativo correto

Uso:
    python sync_gdd.py
    python sync_gdd.py --gdd-path ../advento-gdd/src/ADVENTO
    python sync_gdd.py --github-user meu_usuario_github
"""

import os
import re
import shutil
import argparse
import unicodedata
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
GDD_DEFAULT = SCRIPT_DIR.parent / "advento-gdd" / "src" / "ADVENTO"
# Pasta raiz do GDD completo (onde ficam assets/, não só ADVENTO/)
GDD_ROOT_DEFAULT = SCRIPT_DIR.parent / "advento-gdd"
DOCS_DIR = SCRIPT_DIR / "docs"
IMAGES_DIR = DOCS_DIR / "assets" / "images"
MKDOCS_YML = SCRIPT_DIR / "mkdocs.yml"

IMAGE_EXTS = {'.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg'}


# ─── Helpers ──────────────────────────────────────────────────────────────────

def clean_display(name: str) -> str:
    """
    Remove emojis e prefixos numéricos do nome, preservando acentos portugueses.

    Parâmetros:
        name (str): Nome bruto do arquivo ou pasta.

    Retorno:
        str: Nome limpo para exibição na navegação.
    """
    # U+0000–U+024F cobre ASCII + Latin-1 + Latin Extended (todos acentos PT)
    name = re.sub(r'[^\u0000-\u024F\s\-_.()\[\]]', '', name).strip()
    name = re.sub(r'^\d+\s*[-–]\s*', '', name).strip()
    return name or 'Sem Título'


def slugify(text: str) -> str:
    """
    Converte texto em slug ASCII URL-safe. Transliteração: 'ã'→'a', 'ç'→'c'.

    Parâmetros:
        text (str): Texto original (pode conter emojis, acentos, espaços).

    Retorno:
        str: Slug minúsculo com hífens, ex: 'visao-geral'.
    """
    text = re.sub(r'^\d+\s*[-–]\s*', '', text).strip()
    text = text.lower().replace('&', 'e')
    text = re.sub(r'[^\u0000-\u024F\s\-_]', '', text)
    text = unicodedata.normalize('NFKD', text)
    text = text.encode('ascii', 'ignore').decode()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    return re.sub(r'-+', '-', text).strip('-') or 'pagina'


def slugify_image(filename: str) -> str:
    """
    Gera nome de arquivo seguro para imagens, preservando a extensão original.

    Parâmetros:
        filename (str): Nome original da imagem, ex: 'Pasted image 20260225.png'.

    Retorno:
        str: Nome slugificado, ex: 'pasted-image-20260225.png'.
    """
    p = Path(filename)
    return slugify(p.stem) + p.suffix.lower()


# ─── Índice de páginas markdown ───────────────────────────────────────────────

def build_md_index(gdd_path: Path) -> dict:
    """
    Percorre o GDD e mapeia cada stem original de arquivo .md ao caminho
    relativo que ele terá em docs/ após a slugificação.

    Usado para resolver links internos Obsidian [[Nome da Página]].

    Parâmetros:
        gdd_path (Path): Raiz do GDD (advento-gdd/src/ADVENTO).

    Retorno:
        dict: {'🧠 01 - Visão Geral': 'visao-geral/01-visao-geral.md', ...}
    """
    index = {}
    for root, dirs, files in os.walk(gdd_path):
        dirs.sort()
        root_path = Path(root)
        rel_root = root_path.relative_to(gdd_path)

        for filename in sorted(files):
            if not filename.endswith('.md'):
                continue
            stem = filename[:-3]

            if rel_root == Path('.') and filename == 'ADVENTO.md':
                dest_rel = 'index.md'
            else:
                slug_parts = [slugify(p) for p in rel_root.parts]
                file_slug = slugify(stem)
                dest_rel = '/'.join(slug_parts + [file_slug]) + '.md' if slug_parts else f'{file_slug}.md'

            index[stem] = dest_rel

    return index


# ─── Índice de imagens ────────────────────────────────────────────────────────

def build_image_index(gdd_root: Path) -> dict:
    """
    Percorre todo o repositório GDD e mapeia cada nome de imagem ao seu caminho.
    Em caso de nomes duplicados, prevalece o primeiro encontrado.

    Parâmetros:
        gdd_root (Path): Raiz do repositório advento-gdd (não só src/ADVENTO).

    Retorno:
        dict: {'nome_original.png': Path('/caminho/completo/nome_original.png')}
    """
    index = {}
    for root, _, files in os.walk(gdd_root):
        for f in files:
            if Path(f).suffix.lower() in IMAGE_EXTS:
                if f not in index:
                    index[f] = Path(root) / f
    return index


# ─── Reescrita de links Obsidian ──────────────────────────────────────────────

def rewrite_obsidian_images(content: str, dest_file: Path, docs_root: Path,
                             image_index: dict) -> str:
    """
    Substitui links Obsidian ![[img.png]] por markdown padrão ![img](caminho/relativo).
    Copia as imagens para docs/assets/images/ durante o processo.

    Parâmetros:
        content (str): Conteúdo markdown do arquivo.
        dest_file (Path): Caminho de destino do arquivo .md em docs/.
        docs_root (Path): Raiz de docs/ (para calcular caminhos relativos).
        image_index (dict): Índice nome→caminho construído por build_image_index().

    Retorno:
        str: Conteúdo com os links reescritos.
    """
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    # Calcula quantos níveis acima de docs_root está o dest_file
    depth = len(dest_file.relative_to(docs_root).parts) - 1
    prefix = '../' * depth + 'assets/images/'

    def replace_link(match):
        original_name = match.group(1).strip()

        if original_name not in image_index:
            # Imagem não encontrada: mantém como texto de aviso
            return f'*[imagem não encontrada: {original_name}]*'

        src_path = image_index[original_name]
        dest_name = slugify_image(original_name)
        dest_img = IMAGES_DIR / dest_name

        if not dest_img.exists():
            shutil.copy2(src_path, dest_img)

        alt = Path(original_name).stem
        return f'![{alt}]({prefix}{dest_name})'

    return re.sub(r'!\[\[([^\]]+)\]\]', replace_link, content)


def rewrite_obsidian_links(content: str, dest_file: Path, docs_root: Path,
                            md_index: dict) -> str:
    """
    Substitui links internos Obsidian [[Página]] e [[Página|Alias]] por
    markdown padrão [Alias](caminho/relativo.md).

    Links para páginas inexistentes ficam como texto em itálico.

    Parâmetros:
        content (str): Conteúdo markdown do arquivo.
        dest_file (Path): Caminho do arquivo .md em docs/.
        docs_root (Path): Raiz de docs/.
        md_index (dict): Índice stem→caminho gerado por build_md_index().

    Retorno:
        str: Conteúdo com os links reescritos.
    """
    def replace_link(match):
        inner = match.group(1).strip()

        # Separa target e alias: [[Target|Alias]] ou [[Target]]
        if '|' in inner:
            target, alias = inner.split('|', 1)
            target = target.strip()
            alias = alias.strip()
        else:
            target, alias = inner, None

        if target not in md_index:
            # Página não existe no GDD — exibe como texto
            display = alias or clean_display(target) or target
            return f'*{display}*'

        target_rel = md_index[target]
        target_abs = docs_root / target_rel
        rel = os.path.relpath(target_abs, dest_file.parent).replace('\\', '/')

        display = alias or clean_display(target) or target
        return f'[{display}]({rel})'

    # (?<!!) garante que ![[img]] já tratado não seja reprocessado
    return re.sub(r'(?<!!)(?<!\[)\[\[([^\]]+)\]\]', replace_link, content)


# ─── Cópia de arquivos ────────────────────────────────────────────────────────

def walk_and_copy(gdd_path: Path, docs_path: Path,
                  image_index: dict, md_index: dict) -> list:
    """
    Percorre o GDD, copia todos os .md para docs/ com nomes slugificados,
    reescreve links Obsidian de imagens e páginas, e retorna a navegação.

    Parâmetros:
        gdd_path (Path): Pasta raiz do GDD (advento-gdd/src/ADVENTO).
        docs_path (Path): Pasta de destino (advento-journey/docs/).
        image_index (dict): Índice de imagens gerado por build_image_index().
        md_index (dict): Índice de páginas gerado por build_md_index().

    Retorno:
        list: Lista de nav nodes.
    """
    nav = []

    for entry in sorted(gdd_path.iterdir()):
        if entry.name.startswith('.'):
            continue

        if entry.is_dir():
            node = _process_dir(entry, docs_path, docs_path, gdd_path, image_index, md_index)
            if node:
                nav.append(node)

        elif entry.is_file() and entry.suffix == '.md':
            if entry.name == 'ADVENTO.md':
                dest = docs_path / 'index.md'
                _copy_md(entry, dest, docs_path, image_index, md_index)
                print(f"  {entry.name} -> index.md")
                nav.insert(0, {'label': 'Home', 'file': 'index.md'})

    return nav


def _copy_md(src: Path, dest: Path, docs_root: Path,
             image_index: dict, md_index: dict):
    """
    Copia um arquivo .md reescrevendo links Obsidian de imagens e páginas.

    Parâmetros:
        src (Path): Arquivo de origem no GDD.
        dest (Path): Arquivo de destino em docs/.
        docs_root (Path): Raiz de docs/.
        image_index (dict): Índice de imagens.
        md_index (dict): Índice de páginas markdown.
    """
    content = src.read_text(encoding='utf-8', errors='replace')
    content = rewrite_obsidian_images(content, dest, docs_root, image_index)
    content = rewrite_obsidian_links(content, dest, docs_root, md_index)
    dest.write_text(content, encoding='utf-8')


def _process_dir(src_dir: Path, dest_base: Path, docs_root: Path,
                 gdd_root: Path, image_index: dict, md_index: dict):
    """
    Processa um diretório do GDD recursivamente: cria pasta slugificada,
    copia arquivos .md (com reescrita de imagens e links) e retorna o nav node.

    Parâmetros:
        src_dir (Path): Pasta de origem no GDD.
        dest_base (Path): Pasta de destino atual em docs/.
        docs_root (Path): Raiz de docs/.
        gdd_root (Path): Raiz do GDD (para log).
        image_index (dict): Índice de imagens.
        md_index (dict): Índice de páginas markdown.

    Retorno:
        dict | None: Nav node com 'label' e 'children', ou None se vazio.
    """
    label = clean_display(src_dir.name)
    slug = slugify(src_dir.name)
    dest_dir = dest_base / slug
    dest_dir.mkdir(parents=True, exist_ok=True)

    children = []

    for entry in sorted(src_dir.iterdir()):
        if entry.name.startswith('.'):
            continue

        if entry.is_dir():
            child = _process_dir(entry, dest_dir, docs_root, gdd_root, image_index, md_index)
            if child:
                children.append(child)

        elif entry.is_file() and entry.suffix == '.md':
            file_label = clean_display(entry.stem)
            file_slug = slugify(entry.stem)
            dest_file = dest_dir / f"{file_slug}.md"
            _copy_md(entry, dest_file, docs_root, image_index, md_index)
            rel = str(dest_file.relative_to(docs_root)).replace('\\', '/')
            children.append({'label': file_label, 'file': rel})
            src_rel = str(entry.relative_to(gdd_root)).replace('\\', '/')
            print(f"  {src_rel.encode('ascii', 'replace').decode()} -> {rel}")

    if not children:
        return None

    return {'label': label, 'children': children}


# ─── Geração do mkdocs.yml ────────────────────────────────────────────────────

def nav_to_yaml(nav: list, depth: int = 1) -> str:
    """
    Converte lista de nav nodes em YAML indentado para mkdocs.yml.

    Parâmetros:
        nav (list): Lista de nav nodes.
        depth (int): Nível de indentação (começa em 1).

    Retorno:
        str: Bloco YAML da seção `nav:`.
    """
    lines = []
    pad = '  ' * depth
    for node in nav:
        label = node['label'].replace("'", "\\'")
        if 'file' in node:
            lines.append(f"{pad}- '{label}': {node['file']}")
        elif 'children' in node:
            lines.append(f"{pad}- '{label}':")
            lines.append(nav_to_yaml(node['children'], depth + 1))
    return '\n'.join(lines)


MKDOCS_TEMPLATE = """\
site_name: "Advento"
site_description: "Lore e documentação oficial do MMORPG cristão Advento"
site_url: "https://{github_user}.github.io/advento-journey/"
repo_url: "https://github.com/{github_user}/advento-journey"
repo_name: "advento-journey"

theme:
  name: material
  language: pt-BR
  palette:
    - scheme: slate
      primary: light green
      accent: brown
      toggle:
        icon: material/brightness-4
        name: Modo claro
    - scheme: default
      primary: deep purple
      accent: cyan
      toggle:
        icon: material/brightness-7
        name: Modo escuro
  features:
    - navigation.tabs
    - navigation.tabs.sticky
    - navigation.sections
    - navigation.expand
    - navigation.top
    - navigation.indexes
    - search.highlight
    - search.suggest
    - search.share
    - content.code.copy
    - toc.follow

plugins:
  - search:
      lang: pt

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.emoji:
      emoji_index: !!python/name:material.extensions.emoji.twemoji
      emoji_generator: !!python/name:material.extensions.emoji.to_svg
  - toc:
      permalink: true
  - tables
  - attr_list
  - md_in_html

extra:
  social:
    - icon: fontawesome/brands/github
      link: "https://github.com/{github_user}/advento-journey"

nav:
{nav_yaml}
"""


def write_mkdocs(nav: list, github_user: str):
    """
    Escreve o mkdocs.yml com a navegação gerada.

    Parâmetros:
        nav (list): Estrutura de navegação.
        github_user (str): Usuário GitHub para as URLs do site.
    """
    nav_yaml = nav_to_yaml(nav)
    content = MKDOCS_TEMPLATE.format(github_user=github_user, nav_yaml=nav_yaml)
    MKDOCS_YML.write_text(content, encoding='utf-8')
    print(f"  mkdocs.yml atualizado.")


# ─── Entrypoint ───────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description='Sincroniza advento-gdd/src/ADVENTO -> advento-journey/docs/'
    )
    parser.add_argument(
        '--gdd-path', type=Path, default=GDD_DEFAULT,
        metavar='CAMINHO',
        help=f'Pasta ADVENTO do GDD (padrao: {GDD_DEFAULT})'
    )
    parser.add_argument(
        '--gdd-root', type=Path, default=GDD_ROOT_DEFAULT,
        metavar='RAIZ',
        help=f'Raiz do repositorio GDD para busca de imagens (padrao: {GDD_ROOT_DEFAULT})'
    )
    parser.add_argument(
        '--github-user', default='SEU_USUARIO',
        metavar='USUARIO',
        help='Usuario GitHub (usado nas URLs do site)'
    )
    args = parser.parse_args()

    if not args.gdd_path.exists():
        print(f"ERRO: GDD nao encontrado em: {args.gdd_path}")
        print("Use --gdd-path para apontar para advento-gdd/src/ADVENTO")
        return 1

    print(f"Fonte : {args.gdd_path}")
    print(f"Destino: {DOCS_DIR}")
    print()

    # Limpa e recria docs/
    if DOCS_DIR.exists():
        shutil.rmtree(DOCS_DIR)
    DOCS_DIR.mkdir()

    print("Indexando imagens...")
    image_index = build_image_index(args.gdd_root)
    print(f"  {len(image_index)} imagem(ns) encontrada(s).")

    print("Indexando paginas...")
    md_index = build_md_index(args.gdd_path)
    print(f"  {len(md_index)} pagina(s) indexada(s).")

    print("\nCopiando arquivos...")
    nav = walk_and_copy(args.gdd_path, DOCS_DIR, image_index, md_index)

    img_count = sum(1 for _ in IMAGES_DIR.rglob('*') if _.is_file()) if IMAGES_DIR.exists() else 0
    print(f"\n  {img_count} imagem(ns) copiada(s) para docs/assets/images/")

    print("\nGerando mkdocs.yml...")
    write_mkdocs(nav, args.github_user)

    md_count = sum(1 for _ in DOCS_DIR.rglob('*.md'))
    print(f"\n{md_count} arquivo(s) .md copiado(s) para docs/")
    print("\nProximos passos:")
    print("  git add docs/ mkdocs.yml")
    print("  git commit -m 'sync: atualiza docs do GDD'")
    print("  git push")
    return 0


if __name__ == '__main__':
    exit(main())
