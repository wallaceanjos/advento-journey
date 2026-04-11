# 🗺 08 - Roadmap

> [!ABSTRACT] 💡 Em uma frase
> Ordem de construção e planejamento técnico para a sincronização entre o rAthena e a Godot Engine.

---

## 📝 Descrição
Este documento descreve as fases de desenvolvimento do projeto Advento, unindo os marcos de progresso do jogo com a implementação técnica necessária para o cliente.

### 📅 Marcos de Desenvolvimento
1. **Fase 1** – Login + andar no mapa (Sincronização Base)
2. **Fase 2** – Combate básico + Entidades
3. **Fase 3** – Inventário + Banco de Dados
4. **Fase 4** – NPC funcional + Interação
5. **Fase 5** – Primeira cidade jogável + Tradução
6. **Fase 6** – Beta fechado

---

## 🏗️ Detalhamento Técnico

### 🛠️ Fase 1: Sincronização e Movimentação (O Essencial)
Antes de itens ou monstros, o personagem precisa se mover sem desincronizar.
- **rAthena**: Configurar `speed` no `char_db` e pacotes `0x85` (walk request).
- **Godot**:
    - **Input Handling**: Capturar o clique no chão.
    - **Pathfinding**: NavigationAgent validado com dados de GAT do rAthena.
    - **Interpolação**: Suavizar o movimento (ler posição do servidor e interpolar localmente).

### ⚔️ Fase 2: Entidades e Unidades (O Ecossistema)
Visualização de outros jogadores e NPCs.
- **rAthena**: Entender `clif_spawn_unit` (Range de Visão).
- **Godot**: Gerenciador de Entidades (`units = {}`) e Pooling de cenas.

### 🎒 Fase 3: Dados e Inventário (O Coração)
União do MySQL com a UI.
- **rAthena**: Manipular `item_db.conf` e pacotes `0xa0` (inventory list).
- **Godot**: UI Reativa e Dicionário Local (JSON/Resource) para tradução de IDs em sprites/nomes.

### 🎇 Fase 4: Combate e Habilidades (A Alma)
- **rAthena**: Customizar `battle.conf` para fórmulas de dano.
- **Godot**: Sistema de Timers (Animação Visual vs Pacote `0x8a` de dano real) e VFX.

### 🌐 Fase 5: Sistema de Tradução (A Ponte)
- **Backend**: Tabelas SQL (`advento_translations`) e funções de script.
- **Frontend**: `TranslationServer` da Godot com arquivos `.csv`/.po mapeando chaves como `ITM_NAME_501`.

---

## 🔗 Conexões Relacionadas
- ⬅️ **Pai:** [ADVENTO](../index.md)
- 🏠 **Home:** [ADVENTO](../index.md)

---
## 🧠 Análise do Agente
> O roadmap técnico está bem estruturado, priorizando os fundamentos de rede (movimentação e sincronia) antes dos sistemas de dados. A principal barreira será a latência na interpolação, que deve ser tratada com cuidado no cliente para evitar o efeito de "Rubber Banding".

*Última atualização: 12/03/2026*
