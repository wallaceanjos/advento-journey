# 🛠 Abordagem Técnica

> [!ABSTRACT] 💡 Em uma frase
> rAthena + Godot + MySQL: pragmatismo técnico no back-end para permitir inovação visual e narrativa no front-end através do Realismo Espiritual.

---

## 📝 Stack Técnica

| Componente | Tecnologia | Função |
|---|---|---|
| **Servidor** | rAthena (C/C++) | Lógica de combate, validação, persistência e IA. |
| **Cliente** | Godot Engine (C#) | Renderização Stylized Anime, Shaders de Visão Verdadeira, UI/HUD. |
| **Banco de Dados** | MySQL | Dados de personagens, inventário e logs de Santificação. |

---

## 🎯 Filosofia de Desenvolvimento

- **Visual com Propósito:** Arte 3D **Stylized Anime** (estética Genshin/Zelda) com câmera isométrica fixa ou livre. Pixel art descartado para permitir escalabilidade visual e uso intensivo de Shaders.
- **Realismo Espiritual (Shader Tech):**
    - **Visão Verdadeira:** Implementada via Post-Processing Shader que altera a saturação do mundo e destaca a "assinatura espiritual" de cada entidade.
    - **Palavra como Código-Fonte:** Uso de *Decals* e *Emissive Maps* para projetar versículos bíblicos diretamente na geometria do cenário (pedras, árvores, paredes) apenas quando a Visão Verdadeira está ativa.
- **Estabilidade:** rAthena fornece um core testado há décadas, permitindo que a equipe foque na customização da Lore e dos Sistemas de Santidade.

---

## 🔧 Sistemas Customizados Prioritários

1. **Protocolo de Visão:** Extensão do pacote de spawn do rAthena para enviar o `tier_espiritual` do monstro/NPC ao Godot.
2. **Shader de Revelação:** Algoritmo de "dissolve" ou "transition" que permite ao jogador alternar suavemente entre a **Visão Natural** e a **Visão Verdadeira**.
3. **Módulo de Terminologia:** Sistema que injeta nomes duais em toda a interface (Ex: Nome Geográfico no Mapa / Nome de Revelação no Livro).
4. **Cross-Play Otimizado:** Assets 3D com LOD (Level of Detail) agressivo para garantir fluidez em dispositivos mobile sem perder a Glória visual no PC.

## 🔗 Conexões Relacionadas
- ⬅️ **Pai:** [Visão Geral](../01-visao-geral.md)
- 🏠 **Home:** [ADVENTO](../../index.md)
- ⚙️ **Detalhes:** [Sistema Técnico](../../sistema-tecnico/05-sistema-tecnico.md); [Arquitetura Geral](../../sistema-tecnico/arquitetura/arquitetura-geral.md)
- 🎨 **Arte:** *wiki/style-guide.md*

---
## 🧠 Análise do Agente
> A abordagem técnica é "serva" da experiência. O uso de Godot para shaders emissivos e rAthena para a robustez de dados cria o equilíbrio perfeito: um jogo que funciona como um relógio suíço, mas brilha como uma obra de arte sacra.

*Última atualização: 2026-05-01*
