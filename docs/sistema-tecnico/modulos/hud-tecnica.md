# 🎛 HUD Técnica

> [!ABSTRACT] 💡 Em uma frase
> A HUD do Advento segue o padrão rAthena de elementos visíveis, com dual nomenclatura: termos técnicos na interface principal + nomes de lore em tooltips e descrições.

---

## Elementos Principais da HUD

| Elemento | Termo técnico | Termo de Lore | Notas |
|---|---|---|---|
| Barra de HP | HP / Health Points | Integridade do Vaso | "Representa o vigor físico e espiritual do Discípulo" |
| Barra de SP | SP / Skill Points | Unção / Fluxo | "Energia espiritual disponível para manifestar dons" |
| Skill bar | Skill Bar | Barra de Dons/Autoridade | Skills = Dons/Autoridade |
| Minimapa | Minimap | Visão do Campo | Muda de visual em Visão Verdadeira |
| Chat | Chat | Comunicação da Comunhão | Sem mudança visual |
| Inventário | Inventory | Fardos da Jornada | Peso = Fardo |
| EXP Bar | Experience | Revelação / Vivência | Tooltip explica o nome de lore |
| Level | Base Level | Alinhamento Espiritual | Hover mostra termo de lore |
| Job Level | Job Level | Grau de Ministério | — |
| Peso | Weight | Fardo | 100% = "Fardo excessivo — incapaz de avançar" |

---

## 🎮 Regra de Dual Nomenclatura (UX)

Para não confundir jogadores veteranos de MMORPG:

1. **HUD visível:** Usa termos técnicos padrão (`HP`, `SP`, `Level`, `EXP`).
2. **Hover/Tooltip:** Exibe nome de lore com descrição. Ex: *"Integridade do Vaso: Representa o vigor físico e espiritual do Discípulo sob o Véu."*
3. **Diálogos de NPC:** Usam exclusivamente termos de lore. O sistema injeta a tradução via `advento_translations`.
4. **Mensagens de sistema:** Mistas — termos técnicos para clareza, lore para imersão.

---

## 🌑 Visão Verdadeira (HUD em Combate)

Quando a Visão Verdadeira está ativa:
- Shader de desaturação global aplica-se ao cenário (não à HUD).
- A HUD mantém saturação normal para legibilidade.
- Overlays de tier de cor nos inimigos ficam visíveis.
- Indicador sutil no canto da tela: ícone de "olho aberto" indica que a Visão Verdadeira está ativa.

---

## Integração Técnica

- Dados vindos do servidor via pacotes rAthena padrão.
- Atualização em tempo real via sinais do Godot (`hp_changed`, `sp_changed`, etc.).
- `advento_translations` SQL injetado no `TranslationServer` do Godot (Fase 5 do Roadmap).
- HUD adaptada para mobile (toque) e PC (mouse/teclado) — mesma base, layouts distintos.

---

## 🔗 Relacionado

- [Sistema Técnico](../05-sistema-tecnico.md)
- [Glossário Base](../../lore/glossario-e-termos/glossario-base.md) (tabela completa de analogias)
- [Sistema de Combate](../../gameplay/sistema-de-combate.md) (Visão Verdadeira ativa)
- [Roadmap](../../roadmap/08-roadmap.md) (Fase 3 — UI reativa; Fase 5 — tradução)

*Última atualização: 2026-04-19*
