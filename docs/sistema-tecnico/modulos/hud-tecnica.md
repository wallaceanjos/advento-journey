# 🎛 HUD Técnica

> [!ABSTRACT] 💡 Em uma frase
> A HUD de **Advento** utiliza uma **Dual Nomenclatura**: termos técnicos no display principal para clareza (UX) e nomes de Lore em tooltips para imersão no **Realismo Espiritual** de **Advenia**.

---

## Mapeamento de Elementos (Técnico ↔ Lore)

| Elemento | Termo Técnico | Termo de Lore | Contexto de Realismo Espiritual |
|---|---|---|---|
| **Barra Vermelha** | HP / Health Points | **Integridade do Vaso** | Vigor físico e resistência do corpo (2Co 4:7). |
| **Barra Azul** | SP / Skill Points | **Unção / Fluxo** | Energia espiritual para manifestar Dons. |
| **Nível Base** | Level | **Santidade** | Grau de autoridade e maturidade ministerial. |
| **Nível Classe** | Job Level | **Maturidade Ministerial**| Competência técnica na vocação escolhida. |
| **Barra de EXP** | Experience | **Revelação** | Conhecimento prático acumulado na Guerra. |
| **Peso** | Weight | **Fardo** | Capacidade de carga sem comprometer o vigor. |
| **Skill Bar** | Skills | **Dons e Autoridade** | Manifestações d'O Livro no campo. |

---

## 🎮 Regra de Dual Nomenclatura (UX)

Para equilibrar veteranos de rAthena e a imersão de novos Discípulos:

1. **HUD Visível:** Exibe termos técnicos padrão (`HP`, `SP`, `LV`, `EXP`) para leitura rápida em combate.
2. **Hover / Tooltip:** Ao passar o mouse, o termo de Lore é revelado.
    - *Exemplo:* Hover no 'LV 50' mostra: *"Santidade: 50 — Sua autoridade sobre as trevas de Advenia cresceu."*
3. **Diálogos de NPCs:** Usam exclusivamente os termos de Lore.
4. **Sistema de Tradução:** O módulo `advento_translations` injeta as strings de Lore no `TranslationServer` do Godot.

---

## 🌑 HUD sob Visão Verdadeira

Quando a **Visão Verdadeira** é ativada em combate:
- A HUD mantém sua saturação normal para garantir legibilidade absoluta.
- Um indicador sutil (Ícone d'O Livro aberto) aparece no topo da tela.
- Os Tiers Espirituais dos inimigos tornam-se visíveis como barras de cor (Cinza, Âmbar, Vermelho) integradas ao mundo 3D, não à HUD 2D.

## 🔗 Conexões Relacionadas
- ⬅️ **Pai:** [Sistema Técnico](../05-sistema-tecnico.md)
- 🏠 **Home:** [ADVENTO](../../index.md)
- 📖 **Glossário:** [Glossário Base](../../lore/glossario-e-termos/glossario-base.md)
- ⚙️ **Técnico:** [Comunicação Client-Server](../arquitetura/comunicacao-client-server.md)

---
## 🧠 Análise do Agente
> A HUD Técnica é onde o "Realismo" do Realismo Espiritual encontra o "Espiritual". Ao manter o HP visível como "Integridade do Vaso" no tooltip, lembramos ao jogador que sua vida em Advenia é um recurso sagrado que deve ser zelado, não apenas um contador de dano.

*Última atualização: 2026-05-01*
