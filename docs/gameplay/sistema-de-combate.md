# ⚔️ Sistema de Combate

> [!ABSTRACT] 💡 Em uma frase
> O combate em **Advenia** não é aniquilação física — é **Expulsão**. O Discípulo nunca mata; ele liberta territórios e devolve a distorção espiritual ao lugar de onde veio (lugares áridos), aguardando a Parusia.

---

## 🌿 Fundamento do Realismo Espiritual

> *"Quando o espírito imundo sai do homem, anda por lugares áridos, procurando repouso, e não encontra."* — Mt 12:43  

**Conclusão teológica:** O mal em Advenia não é destruído agora, mas expulso até o Juízo Final. Portanto, o jogador nunca "mata" — ele exerce autoridade para remover a distorção da **Visão Natural**. O inimigo retorna (respawn) porque a purificação definitiva é uma promessa futura (Parusia).

---

## 🎮 A Experiência do Combate

**Fluxo Momento a Momento:**

1. **Detecção:** A **Visão Verdadeira** ativa-se automaticamente ao entrar em combate. O cenário (Visão Natural) sofre desaturação, e a Realidade Superior torna-se nítida.
2. **Avaliação:** O Discípulo enxerga o **Tier de Cor** do inimigo (Cinza, Âmbar ou Vermelho), indicando o nível de autoridade necessária para a expulsão.
3. **Ação:** O jogador utiliza seus **Dons e Autoridade** (Skills) d'O Livro. O combate é fluido e em tempo real.
4. **Expulsão:** Ao ser "derrotado", o inimigo dissolve-se em partículas (luz para o que foi liberto, sombra para o que foi expulso). A UI registra: *"Expulsão Confirmada"*.
5. **Retorno:** Ao fim do combate, a **Visão Natural** (cores vibrantes) reinicia suavemente conforme o Discípulo baixa sua guarda espiritual.

---

## 🌑 A Lente da Verdade (Tiers de Cor)

| Tier | Cor | Significado Espiritual | Estratégia de Combate |
|---|---|---|---|
| **Tier 0** | ⚪ Cinza | Sem autoridade sobre o Discípulo. | Farm rápido; baixo risco. |
| **Tier 1** | 🟡 Âmbar | Equivalente em maturidade. | Combate estratégico; uso de recursos. |
| **Tier 2** | 🔴 Vermelho | Autoridade maligna superior. | Fuga ou necessidade de Comunhão (Party). |

**Implementação Técnica (rAthena + Godot):**
- O servidor calcula a diferença de **Santidade** (`base_level`) e envia um byte `tier_espiritual`.
- O cliente Godot aplica o shader de overlay correspondente ao mob em tempo real.

---

## 💀 Integridade do Vaso (Morte) e Ressurreição

Ao ter a **Integridade do Vaso** (HP) zerada:
1. **Espaço de Paz:** A tela transiciona para uma dimensão de luz plena (saturação 100%).
2. **O Encontro:** **A Presença** manifesta-se: *"A sua missão ainda não acabou."*
3. **Sopro de Vida:** O jogador recebe a restauração e retorna ao ponto de santuário mais próximo.

---

## 🚫 Regras de UX e Terminologia

Para manter a imersão no Realismo Espiritual:
- **❌ Proibido:** "Kill count", "Você matou X monstros", "Morte".
- **✅ Obrigatório:** "Expulsões realizadas", "Influência reduzida", "Integridade comprometida".
- **Visual:** Inimigos nunca deixam "sangue" ou "cadáveres" persistentes; eles se dissipam, restando apenas a **Matéria Sequestrada** (drops).

## 🔗 Conexões Relacionadas
- ⬅️ **Pai:** [Gameplay](04-gameplay.md)
- 🏠 **Home:** [ADVENTO](../index.md)
- 📖 **Lore:** [A Visão Natural](../lore/capitulos/01-a-visao-natural.md); [Principados](../lore/capitulos/02-principados.md); [A Guerra Invisível](../lore/capitulos/06-a-guerra-invisivel.md)

---
## 🧠 Análise do Agente
> O sistema de expulsão é o que diferencia o Advento de um clone de Ragnarok. Ao transformar a morte do mob em uma "dissolução espiritual", resolvemos o problema da violência gratuita e reforçamos o papel do jogador como um agente de ordem e luz. A "Lente da Verdade" (Tiers) torna o nível do mob uma informação narrativa, não apenas um número.

*Última atualização: 2026-05-01*
