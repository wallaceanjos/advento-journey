# ⚔️ Sistema de Combate

> [!ABSTRACT] 💡 Em uma frase
> O combate no Advento não é assassinato — é Expulsão. O jogador nunca mata; ele liberta territórios e devolve o mal ao lugar de onde veio, aguardando o Juízo Final.

---

## 🌿 Âncora Teológica

> *"Quando o espírito imundo sai do homem, anda por lugares áridos, procurando repouso, e não encontra."* — Mt 12:43  
> *"O diabo, que as enganava, foi lançado no lago de fogo e enxofre [...] e serão atormentados dia e noite pelos séculos dos séculos."* — Ap 20:10

**Conclusão teológica:** O mal não é destruído agora. Ele é expulso até o Juízo Final. Portanto, o jogador nunca "mata" — ele expulsa. O inimigo volta (respawn) porque a purificação definitiva só ocorre na Parusia.

---

## 🎮 O que o Jogador Faz

**Momento a momento no combate:**

1. **Detecção:** A Visão Verdadeira ativa automaticamente ao entrar em combate ou Fissura — shader de desaturação global no cenário; inimigos recebem overlay de tier de cor.
2. **Avaliação:** Tier do inimigo indica estratégia (cinza = farm rápido; âmbar = atenção; vermelho = cuidado extremo).
3. **Ação:** Ativar Dons/Autoridade (skills) específicos da classe. Combate em tempo real (MMORPG).
4. **Expulsão:** Inimigo derrotado = expulso para "lugares áridos". UI não mostra "Kill" — mostra "Expulsão confirmada" ou "Libertação" (Corrompidos).
5. **Coleta:** Matéria Sequestrada liberta cai no chão.
6. **Retorno ao Mundo de Ilusão:** Ao sair do combate, shader de desaturação reverte. O mundo "volta" à cor — o Véu se reinstala parcialmente.

---

## 🌑 A Visão Verdadeira (Sistema de Tiers de Cor)

| Tier | Cor | Condição | Estratégia |
|---|---|---|---|
| **Tier 0** | ⚪ Cinza | Inimigo muito inferior ao jogador | Farm eficiente; baixo risco |
| **Tier 1** | 🟡 Âmbar | Inimigo equivalente | Combate estratégico; use habilidades |
| **Tier 2** | 🔴 Vermelho | Inimigo superior | Fuga ou preparação intensa |

**Implementação técnica:**
- rAthena: pacote customizado `clif_spawn_unit` estendido com byte `tier_cor` (0, 1 ou 2).
- Godot: shader de overlay aplicado ao material do mob baseado no valor recebido.
- O cálculo de `tier_cor` é feito pelo servidor: `base_level` do mob vs. `base_level` do jogador.

---

## 🔄 Loop Central do Combate

```
Entrar na Fissura/Dungeon
  → Visão Verdadeira ativa (desaturação + overlay)
  → Avaliar tier dos inimigos
  → Expulsar mobs (Dons/Autoridade da classe)
    ↳ Tier 0: farm automático
    ↳ Tier 1: combate ativo
    ↳ Tier 2: skill rotations, party necessária
  → Coletar Matéria Sequestrada
  → Avançar para MVP (se dungeon)
  → Expulsar MVP → território temporariamente limpo
  → Retornar à cidade com drops
  → Repetir (Principado reconquistará o território)
```

---

## 💀 Morte e Ressurreição

Ao ter a Integridade do Vaso zerada:

1. Tela transiciona para espaço de paz (saturação 100% — o único momento fora do Véu).
2. A Presença aparece: *"A sua missão ainda não acabou, meu filho."*
3. Sopro de Vida (Resurrect) concedido.
4. Jogador retorna ao ponto de restauração mais próximo com penalidade de Unção (SP).
5. Alternativa: Sacerdote aliado pode executar Ressurreição em campo.

---

## 🚫 Regras de UX (o que NÃO mostrar)

- ❌ Nunca: "Monstros mortos", "Kill count", "Kills today"
- ✅ Sempre: "Expulsões confirmadas", "Libertações realizadas", "Influência reduzida em X%"
- ❌ Nunca mostrar "HP do inimigo = 0" como morte — mostrar como "Expulso"
- ✅ Animação de expulsão: mob se dissolve em partículas de luz ou sombra (dependendo do tipo)

---

## 🔗 Conexões Relacionadas

- ⬅️ **Pai:** [Gameplay](04-gameplay.md)
- 🏠 **Home:** [ADVENTO](../index.md)
- 📖 **Lore:** [O Véu](../lore/capitulos/01-o-veu.md) (Visão Verdadeira); [Principados](../lore/capitulos/02-principados.md) (respawn justificado); [A Guerra Invisível](../lore/capitulos/06-a-guerra-invisivel.md) (dungeons)
- ⚙️ **Técnico:** [Arquitetura Geral](../sistema-tecnico/arquitetura/arquitetura-geral.md) (implementação do shader); [Comunicação Client-Server](../sistema-tecnico/arquitetura/comunicacao-client-server.md) (pacote tier_cor)
- 🎬 **Cena:** [O Despertar](../lore/cenas/o-despertar.md) (primeira ativação da Visão Verdadeira)

*Última atualização: 2026-04-19*
