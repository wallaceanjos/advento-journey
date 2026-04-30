# 🖥 05 - Sistema Técnico

> [!ABSTRACT] 💡 Em uma frase
> Stack pragmática: rAthena (servidor) + Godot (cliente) + MySQL — back-end testado que permite foco total na personalização de lore e na experiência visual.

---

## 🏗 Arquitetura

```
Cliente (Godot)                Servidor (rAthena)
─────────────────────────      ─────────────────────────
- Renderização 3D Stylized     - Cálculo de dano
- Input do jogador             - Validação de ações
- UI / HUD (com nomes lore)    - Persistência (MySQL)
- Shaders (Visão Verdadeira)   - Controle de estado global
- Feedback visual / VFX        - Spawn de entidades
```

**Engine: Godot** (decisão canônica — referência a Unity em rascunho antigo descartada).

---

## 📁 Documentos de Arquitetura

1. [Arquitetura Geral](arquitetura/arquitetura-geral.md) — Stack completo, diagrama cliente/servidor
2. [Comunicação Client-Server](arquitetura/comunicacao-client-server.md) — Protocolos, pacotes customizados (`tier_cor`)

## 📦 Módulos Técnicos

3. [Sistema de Login](modulos/sistema-de-login.md) — Fluxo de autenticação e seleção de personagem
4. [HUD Técnica](modulos/hud-tecnica.md) — Elementos de HUD com nomes de lore; dual nomenclatura

---

## 🛠️ Sistemas Customizados Prioritários

| Sistema | Fase do Roadmap | Descrição |
|---|---|---|
| Shader de Visão Verdadeira | Fase 2 | Desaturação global + overlay de tier de cor (cinza/âmbar/vermelho) |
| Pacote `tier_cor` | Fase 2 | Byte customizado em `clif_spawn_unit` enviado pelo servidor |
| Sistema de Analogias | Fase 5 | `advento_translations` SQL + `TranslationServer` Godot |
| HUD Dual | Fase 3–5 | Termos técnicos no display; nomes de lore em tooltips |

---

## 🗺️ Roadmap

Ver: [Roadmap](../roadmap/08-roadmap.md)

| Fase | Conteúdo | Prioridade técnica |
|---|---|---|
| 1 | Login + movimentação | Sincronização base, pathfinding, interpolação |
| 2 | Combate básico + entidades | `clif_spawn_unit`, gerenciador de entidades, **shader Visão Verdadeira** |
| 3 | Inventário + banco de dados | `item_db.conf`, UI reativa, nomes de lore |
| 4 | NPC funcional + interação | `battle.conf`, VFX de combate, timers |
| 5 | Primeira cidade jogável + tradução | `advento_translations` SQL, `TranslationServer` Godot |
| 6 | Beta fechado | — |

---

## 🔗 Conexões Relacionadas

- ⬅️ **Pai:** [ADVENTO](../index.md)
- 🏠 **Home:** [ADVENTO](../index.md)
- ⚙️ **Design:** [Abordagem Técnica](../visao-geral/estrutura-e-tecnica/abordagem-tecnica.md); [Sistema de Combate](../gameplay/sistema-de-combate.md) (shader)
- 📖 **Glossário:** [Glossário Base](../lore/glossario-e-termos/glossario-base.md) (tabela de analogias rAthena↔lore)

*Última atualização: 2026-04-19*
