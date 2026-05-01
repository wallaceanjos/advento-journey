# 🧱 Arquitetura Geral

> [!ABSTRACT] 💡 Em uma frase
> A fundação técnica de **Advento** separa a percepção visual (Godot) da autoridade e estado global (rAthena), permitindo que o **Realismo Espiritual** seja processado de forma eficiente.

---

## 🎮 Engine: Godot 4.x (C#)

O cliente é responsável por materializar a experiência de **Advenia**:
- **Renderização:** Estilo Stylized Anime para a **Visão Natural**; desaturação e shaders para a **Visão Verdadeira**.
- **Sistemas Locais:** Gerenciamento de Cenas (Scene Manager), VFX de Shekinah, Interpolação de movimento e HUD Dual.
- **Lógica de Visão:** Aplicação dos Tiers de Cor recebidos pelo servidor nos materiais dos modelos 3D.

---

## 🔌 Servidor: rAthena (C / MySQL)

O servidor é a âncora de autoridade espiritual e lógica:
- **Lógica de Jogo:** Cálculos de autoridade (dano), progressão de **Santidade** (base_level) e gestão de **Unção** (SP).
- **Entidades:** IA de Principados e Corrompidos, controle de spawn e respawn justificado pela Lore.
- **Banco de Dados:** Persistência MySQL para personagens, inventários de **Matéria Sequestrada** e progressão de missões.

---

## 🗄️ Fluxo de Integração

1. **Autenticação:** [Sistema de Login](../modulos/sistema-de-login.md) valida o acesso ao Reino.
2. **Handshake:** Sincronização de pacotes entre Godot e rAthena via [Comunicação Client-Server](comunicacao-client-server.md).
3. **Loop:** O servidor envia o estado do mundo; o cliente traduz esse estado em beleza (Visão Natural) ou verdade (Visão Verdadeira).

## 🔗 Relacionado
- ⬅️ **Pai:** [Sistema Técnico](../05-sistema-tecnico.md)
- 🏠 **Home:** [ADVENTO](../../index.md)
- ⚙️ **Módulo:** [HUD Técnica](../modulos/hud-tecnica.md)

---
## 🧠 Análise do Agente
> A arquitetura cliente-servidor é o que permite a Advenia ser um MMORPG escalável. Ao delegar a "maquiagem" visual (Visão Natural) totalmente ao Godot, garantimos que o rAthena permaneça leve, processando apenas os números puros da autoridade espiritual que regem o combate.

*Última atualização: 2026-05-01*