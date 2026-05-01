# 🖥 05 - Sistema Técnico

> [!ABSTRACT] 💡 Em uma frase
> Stack pragmática para **Advenia**: rAthena (servidor) + Godot (cliente) + MySQL — um back-end testado que permite foco total na personalização de Lore e na experiência visual de **Realismo Espiritual**.

---

## 🏗 Arquitetura de Conexão

```
Cliente (Godot 4.x)             Servidor (rAthena - C)
─────────────────────────      ─────────────────────────
- Renderização Stylized Anime   - Cálculo de Autoridade (Dano)
- Shaders de Visão Verdadeira   - Validação de Santidade (Level)
- UI / HUD Dual Nomenclatura    - Persistência de Advenia (MySQL)
- Processamento de Votos/Dons   - Spawn de Entidades (Principados)
- Feedback Visual Shekinah      - Controle de Tiers Espirituais
```

---

## 📁 Documentos de Arquitetura

1. [Arquitetura Geral](arquitetura/arquitetura-geral.md) — Diagrama completo do fluxo de dados.
2. [Comunicação Client-Server](arquitetura/comunicacao-client-server.md) — Protocolos e pacotes customizados (ex: `tier_espiritual`).
3. [Sistema de Login](modulos/sistema-de-login.md) — Fluxo de autenticação e seleção do **Grau de Ministério**.
4. [HUD Técnica](modulos/hud-tecnica.md) — Implementação da interface técnica com tooltips de Lore.

---

## 🛠️ Sistemas Customizados Prioritários

| Sistema | Fase do Roadmap | Objetivo de Realismo Espiritual |
|---|---|---|
| **Shader Visão Verdadeira** | Fase 2 | Materializar a transição da Visão Natural para a Realidade Superior. |
| **Pacote `tier_espiritual`**| Fase 2 | Enviar do servidor a autoridade relativa do mob (Cinza/Âmbar/Vermelho). |
| **Sistema de Analogias** | Fase 5 | Tradução sistemática de termos rAthena para Advenia (SQL + Godot). |
| **Integridade do Vaso (HP)** | Fase 3 | Reinterpretação visual do vigor físico sob a opressão espiritual. |

---

## 🗺️ Roadmap de Desenvolvimento

| Fase | Marco Técnico | Foco Narrativo |
|---|---|---|
| 1 | Login + Movimentação | Despertar em **Primórdia**. |
| 2 | Combate + Entidades | Primeira manifestação da **Visão Verdadeira**. |
| 3 | Inventário + DB | Purificação de **Matéria Sequestrada**. |
| 4 | NPCs + Interação | O Chamado e a recepção d'**O Livro**. |
| 5 | Primeira Cidade (Orizon)| Abertura da **Guerra Invisível** global. |
| 6 | Beta Fechado | Teste de Comunhão e Resistência. |

## 🔗 Conexões Relacionadas
- ⬅️ **Pai:** [ADVENTO](../index.md)
- 🏠 **Home:** [ADVENTO](../index.md)
- ⚙️ **Mecânica:** [Abordagem Técnica](../visao-geral/estrutura-e-tecnica/abordagem-tecnica.md); [Sistema de Combate](../gameplay/sistema-de-combate.md)
- 📖 **Glossário:** [Glossário Base](../lore/glossario-e-termos/glossario-base.md)

---
## 🧠 Análise do Agente
> A escolha da stack (rAthena + Godot) é a decisão técnica mais madura do projeto. Ao usar um servidor de C legado extremamente estável para a lógica de MMO, liberamos o Godot para focar no que realmente diferencia Advenia: os shaders complexos de desaturação e os efeitos visuais que vendem a ideia do Realismo Espiritual.

*Última atualização: 2026-05-01*
