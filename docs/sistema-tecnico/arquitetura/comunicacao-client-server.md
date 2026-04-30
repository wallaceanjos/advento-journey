# 🧠 Comunicação Client-Server

> [!ABSTRACT] 💡 Em uma frase
> O modelo cliente/servidor do Advento segue o protocolo rAthena padrão com extensões customizadas para suportar a Visão Verdadeira (sistema de tiers de cor).

---

## Modelo

```
Cliente (Godot)
      ↕ (TCP/UDP — protocolo rAthena)
Servidor (rAthena)
```

**Nota:** Engine canônica é **Godot** — não Unity (referência a Unity em documentos antigos foi descartada).

---

## Responsabilidades do Cliente (Godot)

- Renderização (3D Stylized, câmera isométrica)
- Input do jogador (clique no chão, habilidades)
- UI / HUD (com dual nomenclatura: técnico + lore)
- Shaders: desaturação global (Visão Verdadeira) + overlay de cor por entidade
- Feedback visual (VFX de expulsão, partículas)
- Animações de personagem e entidades

## Responsabilidades do Servidor (rAthena)

- Cálculo de dano e validação de ações
- Controle de estado global e sincronização
- Persistência via MySQL (personagens, inventário, progresso)
- Spawn de entidades (monstros, NPCs, MVPs)
- Cálculo e envio do `tier_cor` para o cliente

---

## 📦 Pacote Customizado: `tier_cor`

O sistema de Visão Verdadeira requer um byte adicional no pacote de spawn de entidades:

```c
// Extensão do pacote clif_spawn_unit (rAthena)
// Byte customizado adicionado ao final do pacote padrão
struct packet_spawn_unit_advento {
    // [...campos padrão rAthena...]
    uint8_t tier_cor;  // 0 = cinza, 1 = âmbar, 2 = vermelho
};
```

**Cálculo de `tier_cor` no servidor:**
```c
// Pseudocódigo
int nivel_mob = mob->level;
int nivel_jogador = sd->status.base_level;
int delta = nivel_mob - nivel_jogador;

if (delta <= -10)      tier_cor = 0;  // Cinza — muito inferior
else if (delta <= 10)  tier_cor = 1;  // Âmbar — equivalente
else                   tier_cor = 2;  // Vermelho — superior
```

**No Godot:**
```gdscript
# Aplicar overlay ao mob baseado no tier_cor recebido
func set_tier_visual(tier: int):
    match tier:
        0: material.set_shader_param("overlay_color", Color(0.7, 0.7, 0.7))  # cinza
        1: material.set_shader_param("overlay_color", Color(1.0, 0.8, 0.0))  # âmbar
        2: material.set_shader_param("overlay_color", Color(1.0, 0.1, 0.1))  # vermelho
```

---

## 🔄 Fluxo Principal

```
Jogador entra em combate/Fissura
  → Cliente ativa shader de desaturação global
  → Servidor recalcula tier_cor para todos os mobs visíveis
  → Envia pacotes spawn (ou update) com tier_cor
  → Cliente aplica overlay de cor a cada entidade
  → Saída de combate → Cliente reverte desaturação
```

---

## 🔗 Relacionado

- [Arquitetura Geral](arquitetura-geral.md)
- [Sistema de Login](../modulos/sistema-de-login.md)
- [Sistema de Combate](../../gameplay/sistema-de-combate.md) (Visão Verdadeira)
- [Roadmap](../../roadmap/08-roadmap.md) (Fase 2 — implementação do sistema de entidades)

*Última atualização: 2026-04-19*
