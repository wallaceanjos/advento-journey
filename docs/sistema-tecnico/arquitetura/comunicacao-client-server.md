# 🧠 Comunicação Client-Server

> [!ABSTRACT] 💡 Em uma frase
> O modelo de comunicação de **Advento** utiliza o protocolo rAthena padrão com extensões customizadas para materializar a **Visão Verdadeira** e o sistema de Tiers Espirituais em **Advenia**.

---

## Modelo de Dados

O fluxo de informação segue a estrutura de autoridade do **Realismo Espiritual**:

```
Cliente (Godot 4.x)             Servidor (rAthena - C)
      ↕ (TCP/UDP — Protocolo rAthena Estendido)
```

1. **Servidor (Autoridade):** Calcula se o Discípulo tem autoridade sobre a entidade (Diferença de **Santidade**).
2. **Cliente (Percepção):** Recebe os dados de autoridade e aplica os Shaders de desaturação e overlay correspondentes à **Visão Verdadeira**.

---

## 📦 Pacote Customizado: `tier_espiritual`

Para suportar a **Visão Verdadeira**, adicionamos um campo de 1 byte ao pacote de spawn de unidades do rAthena:

```c
// Extensão do pacote clif_spawn_unit (rAthena)
// Byte customizado injetado para definir a percepção do Discípulo
struct packet_spawn_unit_advento {
    // [...campos padrão rAthena...]
    uint8_t tier_espiritual;  // 0 = Cinza, 1 = Âmbar, 2 = Vermelho
};
```

**Lógica de Autoridade no Servidor:**
```c
// Cálculo baseado na Santidade (base_level)
int santidade_mob = mob->level;
int santidade_discípulo = sd->status.base_level;
int delta = santidade_mob - santidade_discípulo;

if (delta <= -10)      tier_espiritual = 0;  // Cinza (Matéria Liberta)
else if (delta <= 10)  tier_espiritual = 1;  // Âmbar (Conflito Equilibrado)
else                   tier_espiritual = 2;  // Vermelho (Opressão Superior)
```

**Processamento Visual no Godot (C#):**
```csharp
// Aplicar o Tier Espiritual ao material 3D da entidade
public void ApplySpiritualTier(int tier) {
    var shaderMaterial = meshInstance.GetSurfaceOverrideMaterial(0) as ShaderMaterial;
    if (shaderMaterial != null) {
        shaderMaterial.SetShaderParameter("spiritual_tier", tier);
    }
}
```

---

## 🔄 Fluxo de Revelação em Combate

1. **Entrada em Conflito:** O jogador engaja um monstro ou entra em uma Fissura.
2. **Ativação da Lente:** O cliente Godot ativa o shader de desaturação global da **Visão Natural**.
3. **Sincronização de Tiers:** O servidor envia o pacote `tier_espiritual` para todas as entidades visíveis.
4. **Revelação:** O Discípulo enxerga as cores espirituais dos inimigos sobre o mundo nítido e sem a "maquiagem" das cores saturadas.

## 🔗 Relacionado
- [Arquitetura Geral](arquitetura-geral.md)
- [Sistema de Combate](../../gameplay/sistema-de-combate.md) (Lógica de Tiers)
- [Roadmap](../../roadmap/08-roadmap.md) (Fase 2)

---
## 🧠 Análise do Agente
> O pacote `tier_espiritual` é o elo técnico que une a teologia ao código. Ao mover o cálculo de "cor" para o servidor (autoridade), garantimos que o sistema seja seguro contra trapaças e que a percepção do jogador seja sempre um reflexo fiel da sua maturidade espiritual (Santidade).

*Última atualização: 2026-05-01*
