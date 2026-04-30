# 🎒 Inventário e Equipamentos

> [!ABSTRACT] 💡 Em uma frase
> O inventário do Discípulo é o testemunho material da guerra — cada item carrega um nome de lore que lembra ao jogador o que ele está fazendo e por quê.

---

## 🌿 Filosofia

Em um MMORPG baseado em rAthena, o inventário é um sistema técnico bem estabelecido. No Advento, cada slot, cada categoria de item e cada limitação de peso tem um nome de lore correspondente — para que o jogador nunca esqueça que está equipando um Discípulo em guerra, não um personagem genérico.

---

## 🗃️ Slots de Equipamento

| Slot técnico (rAthena) | Nome de Lore | Descrição |
|---|---|---|
| **Upper Headgear** | Coroa da Mente Renovada | Capuz, elmo, tiaras |
| **Middle Headgear** | Véu dos Olhos Abertos | Óculos, máscaras, visores |
| **Lower Headgear** | Selo da Boca | Adornos faciais inferiores |
| **Armor** | Vestes do Ministério | Armadura principal do corpo |
| **Weapon** | Instrumento do Rei | Arma principal |
| **Shield** | Escudo da Fé | Escudo (Ef 6:16) |
| **Garment** | Manto da Missão | Capa, manto, costas |
| **Shoes** | Sandálias do Evangelho | Calçados (Ef 6:15) |
| **Accessory (x2)** | Marca da Aliança | Anéis, brincos, amuletos |

---

## 📦 Categorias de Item

| Categoria técnica | Nome de Lore | Origem |
|---|---|---|
| **Healing Items** | Bálsamos de Provisão | Comprados, drops, craft |
| **Equipment** | Vestes e Instrumentos | Drops de MVPs, craft, loja |
| **Ammunition** | Flechas da Proclamação | Caçador; comprado / craft |
| **Etc Items** | Resíduos da Queda | Drops de monstros comuns |
| **Cards** | Ecos da Revelação | Drops raros de monstros específicos |
| **Quest Items** | Evidências da Guerra | Missões; não vendável |
| **Pet Eggs** | *(pendente de definição de lore)* | — |

---

## ⚖️ Sistema de Peso (O Fardo)

> *"Digno é o trabalhador do seu salário."* — 1 Tim 5:18

- **Fardo Máximo** = capacidade máxima de carga (`max_weight` no rAthena).
- Ao atingir 50% do Fardo: velocidade reduzida levemente (o peso da guerra pesa).
- Ao atingir 90% do Fardo: velocidade severamente reduzida + skills bloqueadas.
- Ao atingir 100%: incapaz de mover (o Discípulo foi sobrecarregado).
- **Narrativa:** Um Discípulo que carrega demais perde agilidade espiritual — lore para explicar a mecânica de peso.

---

## 💎 Sistema de Raridade

| Rarity | Cor do nome | Origem |
|---|---|---|
| Comum | Branco | Lojas, drops comuns |
| Incomum | Verde | Drops de dungeon |
| Raro | Azul | Drops de MVP; crafts de A Ordem |
| Épico | Roxo | Drops raros de bosses; missões de cadeia |
| Lendário | Dourado | Drops únicos; eventos especiais; Sacrário |

---

## 🃏 Cartas (Ecos da Revelação)

As Cartas encaixam em slots de Instrumento, Vestes ou Acessórios para conceder bônus especiais:

- Cada Carta representa **Autoridade espiritual sobre uma fraqueza específica** — o Discípulo aprendeu como aquele tipo de corrupção opera e agora pode explorá-la.
- Ex: Carta de Dragão/Fogo encaixada na arma → +15% dano contra raça Dragão elemento Fogo.
- Sistema de múltiplas cartas no mesmo item segue o padrão rAthena (1–4 slots dependendo do equipamento).

---

## 🔗 Conexões Relacionadas

- ⬅️ **Pai:** [Gameplay](04-gameplay.md)
- 🏠 **Home:** [ADVENTO](../index.md)
- 💰 **Economia:** [Economia Espiritual](../lore/bestiario-e-entidades/economia-espiritual.md) (drops como Matéria Sequestrada)
- 📖 **Glossário:** [Glossário Base](../lore/glossario-e-termos/glossario-base.md) (tabela de analogias rAthena↔lore)
- ⚙️ **Técnico:** [Sistema Técnico](../sistema-tecnico/05-sistema-tecnico.md) (item_db.conf — Fase 3 do roadmap)

*Última atualização: 2026-04-19*
