# 🛡️ Classes e Evoluções (Graus de Ministério)

> [!ABSTRACT] 💡 Em uma frase
> As classes no Advento não são profissões — são **Graus de Ministério**: formas distintas de manifestar os dons e autoridade do Rei contra a corrupção do Véu.

---

## 🔝 Estrutura de Progressão

Os Discípulos progridem por dois tiers de evolução, especializando sua função no campo de batalha:

| Classe Primária (Tier I) | Evolução A: ST / Burst (Alvo Único) | Evolução B: AoE / Farm (Área) |
|---|---|---|
| [Guerreiro](classes/guerreiro.md) | **Cavaleiro** | **Paladino** |
| *Clérigo* | **Sacerdote** | **Monge** |
| [Caçador](classes/cacador.md) | **Elite** | **Guardião** |
| [Sábio](classes/sabio.md) | **Profeta** | **Mártir** |
| [Justiceiro](classes/justiceiro.md) | **Executor** | **Inquisitor** |

---

## 🌿 A Lógica dos Graus de Ministério

Cada classe reflete uma forma bíblica de servir ao Rei:

| Classe | Base bíblica | Papel na guerra |
|---|---|---|
| **Guerreiro** | *"Revesti-vos de toda a armadura de Deus"* (Ef 6:11) | Linha de frente; proteção |
| **Clérigo** | *"Curava toda sorte de doenças"* (Mt 4:23) | Suporte; restauração; combate sagrado |
| **Caçador** | *"Olhos como chamas de fogo"* (Ap 1:14) | Vigilância; precisão; distância |
| **Sábio** | *"A espada do Espírito, que é a Palavra de Deus"* (Ef 6:17) | Dano mágico; revelação; área |
| **Justiceiro** | *"A vingança é minha, diz o Senhor"* (Rm 12:19) | Velocidade; purificação; retribuição |

---

## 🎨 Identidade Visual e 3D (Godot)

Diretrizes para modelagem e shaders:

![base-male-female-front](../assets/images/base-male-female-front.png)

### ⚔️ Linhagem do Guerreiro
- **Cavaleiro:** Armaduras de placas polidas, lanças longas, penachos majestosos. Movimento rápido e agressivo.
- **Paladino:** Escudos imensos, detalhes em ouro e prata, auras de luz protetora ao redor do corpo.

### 🛐 Linhagem do Clérigo
- **Sacerdote:** Batas longas, estolas, cruzes e tons de branco e azul. Estilo litúrgico clássico.
- **Monge:** Faixas de combate, vestes curtas ágeis, calçados leves. Estilo de artes marciais sagradas.

### 🏹 Linhagem do Caçador
- **Elite:** Arcos longos recurvos, insígnias de comando, armaduras leves de couro tratado.
- **Guardião:** Capuzes, peles e camuflagem natural. Quase invisível no ambiente.

### 📖 Linhagem do Sábio
- **Profeta:** Cajados de madeira antiga, olhos brilhantes (shader de Revelação), mantos fluidos.
- **Mártir:** Livros abertos flutuando ao redor, auras de luz intensa, símbolos de abnegação.

### ⚖️ Linhagem do Justiceiro
- **Executor:** Lâminas duplas finas, visores místicos/tecnológicos, trajes escuros ajustados.
- **Inquisitor:** Capas pesadas de julgamento, sombras ou chamas nos pés (shader de purificação).

---

## ⚙️ Notas Técnicas (rAthena)

- **Classe base (Novice):** Discípulo recém-chamado; sem especialização. Corresponde ao `Novice` do rAthena.
- **Tier I:** 5 classes primárias = `1st Job Classes`.
- **Tier II (ST/AoE):** 10 evoluções = `2nd Job Classes`.
- **Grau de Ministério** = `job_level` no rAthena, renomeado para o termo de lore.
- `job_change_require` configurado com requisitos de Santidade (base_level) e missões de A Ordem.

---

## 🔗 Conexões Relacionadas

- ⬅️ **Pai:** [Gameplay](04-gameplay.md)
- 🏠 **Home:** [ADVENTO](../index.md)
- 📄 **Detalhes por classe:** [Guerreiro](classes/guerreiro.md); [Clerigo](classes/clerigo.md); [Caçador](classes/cacador.md); [Sábio](classes/sabio.md); [Justiceiro](classes/justiceiro.md)
- 🎬 **Cena:** [O Despertar](../lore/cenas/o-despertar.md) (escolha de classe no prólogo)
- 📖 **Lore:** [O Chamado](../lore/capitulos/05-o-chamado.md) (O Livro revela o Grau de Ministério)

---
## 🧠 Análise do Agente
> A divisão ST/AoE é fundamental para o balanceamento do rAthena. Cada evolução com identidade visual distinta melhora a legibilidade em PvP e instâncias. O fato de cada classe ter uma âncora bíblica garante que o design de novas habilidades sempre tenha um norte temático claro.

*Última atualização: 2026-04-19*
