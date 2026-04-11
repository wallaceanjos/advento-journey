#!/usr/bin/env python3
"""
sync_gdd.py — Sincroniza advento-gdd/src/ADVENTO → advento-journey/docs/
e regenera o mkdocs.yml com a navegação atualizada.

Uso:
    python sync_gdd.py
    python sync_gdd.py --gdd-path ../advento-gdd/src/ADVENTO
    python sync_gdd.py --github-user meu_usuario_github
"""

import os
import re
import shutil
import argparse
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
GDD_DEFAULT = SCRIPT_DIR.parent / "advento-gdd" / "src" / "ADVENTO"
DOCS_DIR = SCRIPT_DIR / "docs"
MKDOCS_YML = SCRIPT_DIR / "mkdocs.yml"


# ─── Helpers ──────────────────────────────────────────────────────────────────

def clean_display(name: str) -> str:
    """
    Remove emojis e prefixos numéricos do nome, preservando acentos portugueses.

    Parâmetros:
        name (str): Nome bruto do arquivo ou pasta.

    Retorno:
        str: Nome limpo para exibição na navegação.
    """
    # Remove qualquer caractere acima de U+024F (emojis, símbolos especiais)
    # U+0000–U+024F cobre ASCII + Latin-1 + Latin Extended (inclui todos acentos PT)
    name = re.sub(r'[^\u0000-\u024F\s\-_.()\[\]]', '', name).strip()
    # Remove prefixo numérico "01 - ", "02 - ", etc.
    name = re.sub(r'^\d+\s*[-–]\s*', '', name).strip()
    return name or 'Sem Título'


def slugify(text: str) -> str:
    """
    Converte texto em slug ASCII URL-safe para uso em nomes de arquivo/pasta.
    Transliteração de acentos: 'ã' → 'a', 'ç' → 'c', etc.

    Parâmetros:
        text (str): Texto original (pode conter emojis, acentos, espaços).

    Retorno:
        str: Slug minúsculo com hífens, ex: 'visao-geral'.
    """
    import unicodedata
    # Remove prefixo numérico
    text = re.sub(r'^\d+\s*[-–]\s*', '', text).strip()
    text = text.lower().replace('&', 'e')
    # Remove emojis (acima de U+024F) antes de decompor
    text = re.sub(r'[^\u0000-\u024F\s\-_]', '', text)
    # Decompõe acentos: 'ã' → 'a' + combining tilde, depois descarta combining
    text = unicodedata.normalize('NFKD', text)
    text = text.encode('ascii', 'ignore').decode()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    return re.sub(r'-+', '-', text).strip('-') or 'pagina'


# ─── Cópia de arquivos ────────────────────────────────────────────────────────

def walk_and_copy(gdd_path: Path, docs_path: Path) -> list:
    """
    Percorre o GDD, copia todos os .md para docs/ com nomes slugificados
    e retorna a estrutura de navegação como lista de nós.

    Parâmetros:
        gdd_path (Path): Pasta raiz do GDD (advento-gdd/src/ADVENTO).
        docs_path (Path): Pasta de destino (advento-journey/docs/).

    Retorno:
        list: Lista de nav nodes — cada nó é {'label': str, 'file': str}
              ou {'label': str, 'children': list}.
    """
    nav = []

    for entry in sorted(gdd_path.iterdir()):
        if entry.name.startswith('.'):
            continue

        if entry.is_dir():
            node = _process_dir(entry, docs_path, docs_path, gdd_path)
            if node:
                nav.append(node)

        elif entry.is_file() and entry.suffix == '.md':
            if entry.name == 'ADVENTO.md':
                dest = docs_path / 'index.md'
                shutil.copy2(entry, dest)
                print(f"  {entry.name} -> index.md")
                nav.insert(0, {'label': 'Home', 'file': 'index.md'})

    return nav


def _process_dir(src_dir: Path, dest_base: Path, docs_root: Path, gdd_root: Path) -> dict:
    """
    Processa um diretório do GDD recursivamente: cria pasta slugificada em docs/,
    copia os arquivos .md e retorna o nav node da seção.

    Parâmetros:
        src_dir (Path): Pasta de origem no GDD.
        dest_base (Path): Pasta de destino atual em docs/.
        docs_root (Path): Raiz de docs/ (para calcular caminhos relativos).
        gdd_root (Path): Raiz do GDD (para exibir caminhos no log).

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
            child = _process_dir(entry, dest_dir, docs_root, gdd_root)
            if child:
                children.append(child)

        elif entry.is_file() and entry.suffix == '.md':
            file_label = clean_display(entry.stem)
            file_slug = slugify(entry.stem)
            dest_file = dest_dir / f"{file_slug}.md"
            shutil.copy2(entry, dest_file)
            rel = str(dest_file.relative_to(docs_root)).replace('\\', '/')
            children.append({'label': file_label, 'file': rel})
            src_rel = str(entry.relative_to(gdd_root)).replace('\\', '/')
            src_safe = src_rel.encode('ascii', 'replace').decode()
            print(f"  {src_safe} -> {rel}")

    if not children:
        return None

    return {'label': label, 'children': children}


# ─── Geração do mkdocs.yml ────────────────────────────────────────────────────

def nav_to_yaml(nav: list, depth: int = 1) -> str:
    """
    Converte lista de nav nodes em YAML indentado compatível com mkdocs.yml.

    Parâmetros:
        nav (list): Lista de nav nodes.
        depth (int): Nível de indentação atual (começa em 1).

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
      primary: deep purple
      accent: amber
      toggle:
        icon: material/brightness-4
        name: Modo claro
    - scheme: default
      primary: deep purple
      accent: amber
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
    Escreve o arquivo mkdocs.yml completo com navegação gerada.

    Parâmetros:
        nav (list): Estrutura de navegação gerada por walk_and_copy().
        github_user (str): Usuário GitHub para compor as URLs do site.
    """
    nav_yaml = nav_to_yaml(nav)
    content = MKDOCS_TEMPLATE.format(github_user=github_user, nav_yaml=nav_yaml)
    MKDOCS_YML.write_text(content, encoding='utf-8')
    print(f"  mkdocs.yml atualizado.")


# ─── Entrypoint ───────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description='Sincroniza advento-gdd/src/ADVENTO → advento-journey/docs/'
    )
    parser.add_argument(
        '--gdd-path', type=Path, default=GDD_DEFAULT,
        metavar='CAMINHO',
        help=f'Caminho para a pasta ADVENTO do GDD (padrão: {GDD_DEFAULT})'
    )
    parser.add_argument(
        '--github-user', default='SEU_USUARIO',
        metavar='USUARIO',
        help='Seu usuário GitHub (usado nas URLs do site)'
    )
    args = parser.parse_args()

    if not args.gdd_path.exists():
        print(f"ERRO: GDD não encontrado em: {args.gdd_path}")
        print("Use --gdd-path para apontar para advento-gdd/src/ADVENTO")
        return 1

    print(f"Fonte : {args.gdd_path}")
    print(f"Destino: {DOCS_DIR}")
    print()

    # Limpa e recria docs/
    if DOCS_DIR.exists():
        shutil.rmtree(DOCS_DIR)
    DOCS_DIR.mkdir()

    print("Copiando arquivos...")
    nav = walk_and_copy(args.gdd_path, DOCS_DIR)

    print("\nGerando mkdocs.yml...")
    write_mkdocs(nav, args.github_user)

    count = sum(1 for _ in DOCS_DIR.rglob('*.md'))
    print(f"\n{count} arquivo(s) copiado(s) para docs/")
    print("\nPróximos passos:")
    print("  git add docs/ mkdocs.yml")
    print("  git commit -m 'sync: atualiza docs do GDD'")
    print("  git push")
    return 0


if __name__ == '__main__':
    exit(main())
