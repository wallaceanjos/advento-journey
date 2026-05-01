# 🗺 08 - Roadmap

> [!ABSTRACT] 💡 Em uma frase
> Planejamento técnico e narrativo para a sincronização entre o servidor rAthena e o cliente Godot, visando a materialização de **Advenia**.

---

## 🏗️ Fases de Desenvolvimento

O projeto segue uma ordem de construção pragmática, priorizando a estabilidade de rede antes da expansão de conteúdo:

### 🛠️ Fase 1: Sincronização Base (O Despertar)
- **Objetivo:** Login e movimentação sem latência perceptível.
- **Técnico:** Handshake rAthena; Interpolação de movimento no Godot; Pathfinding validado por GAT.
- **Narrativo:** O Discípulo acorda em **Primórdia** (Orizon) sob a **Visão Natural**.

### ⚔️ Fase 2: Ecossistema e Visão (A Realidade)
- **Objetivo:** Spawn de entidades e ativação da **Visão Verdadeira**.
- **Técnico:** Implementação do pacote `tier_espiritual`; **Shader de Desaturação Global**; Gerenciador de Entidades.
- **Narrativo:** O rasgar da Visão Natural e a detecção de ameaças espirituais.

### 🎒 Fase 3: Dados e Reivindicação (O Coração)
- **Objetivo:** Inventário reativo e banco de dados SQL.
- **Técnico:** Sincronização do `item_db`; UI de **Fardo** e **Integridade do Vaso** (HP/SP).
- **Narrativo:** Coleta de **Matéria Sequestrada** e gestão de recursos.

### 🎇 Fase 4: Combate e Dons (A Guerra)
- **Objetivo:** Skills funcionais e fórmulas de dano baseadas em **Santidade**.
- **Técnico:** Sistema de Timers (Animação vs Pacote de Dano); VFX de Shekinah; Customização de `battle.conf`.
- **Narrativo:** O exercício da autoridade ministerial através d'**O Livro**.

### 🌐 Fase 5: Tradução e Identidade (A Ponte)
- **Objetivo:** Implementação da **Dual Nomenclatura** e primeira cidade completa.
- **Técnico:** `advento_translations` SQL; `TranslationServer` da Godot; Finalização da UI Mobile/PC.
- **Narrativo:** Consolidação da cultura e terminologia de **Advenia**.

### 🧪 Fase 6: Beta Fechado (A Comunhão)
- **Objetivo:** Teste de estresse e balanceamento de **Comunhão** (Party) e **Resistência** (Guilda).

## 🔗 Conexões Relacionadas
- ⬅️ **Pai:** [ADVENTO](../index.md)
- 🏠 **Home:** [ADVENTO](../index.md)
- ⚙️ **Técnico:** [Sistema Técnico](../sistema-tecnico/05-sistema-tecnico.md)
- ⚙️ **Arquitetura:** [Arquitetura Geral](../sistema-tecnico/arquitetura/arquitetura-geral.md)

---
## 🧠 Análise do Agente
> Este roadmap garante que a "mágica" visual da Visão Verdadeira (Fase 2) seja construída sobre uma base de rede sólida (Fase 1). Ao focar na tradução e UI Dual apenas na Fase 5, permitimos que o desenvolvimento técnico flua com nomes padrão rAthena antes da "maquiagem" final da Lore ser aplicada sistematicamente.

*Última atualização: 2026-05-01*
