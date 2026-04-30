# 🛠 Abordagem Técnica

> [!ABSTRACT] 💡 Em uma frase
> rAthena + Godot + MySQL — pragmatismo técnico que entrega um back-end testado e um cliente customizável, permitindo que o brilho do projeto esteja na escrita e na ambientação.

---

## 📝 Stack Técnico

| Componente | Tecnologia | Função |
|---|---|---|
| **Servidor** | rAthena | Cálculo de dano, validação de ações, estado global, persistência |
| **Cliente** | Godot Engine | Renderização, input, UI/HUD, feedback visual, shaders |
| **Banco de Dados** | MySQL | Persistência de personagens, inventário, progresso |

**Engine canônica: Godot** (referência a Unity em um rascunho antigo foi descartada).

---

## 🎯 Filosofia de Desenvolvimento

- **Estabilidade acima de inovação excessiva:** rAthena garante um back-end sólido e testado. Não reinventamos o que já funciona.
- **Customização focada:** Foco em lore, reinterpretação de assets (mobs/MVPs), eventos e sistemas de narração. Não em sistemas mecânicos inéditos.
- **Visual com propósito:** Client customizado para identidade única sem quebrar a mecânica base. Arte 3D Stylized; câmera isométrica; **Pixel Art descartado** (razão: escalabilidade, animações de troca de equipamento, suporte a shaders de Visão Verdadeira).
- **Cross-play:** HUD adaptada para mobile e PC. Mesma base de servidor.

---

## 🔧 Sistemas Customizados Prioritários

1. **Shader de Visão Verdadeira:** Desaturação global do cenário + overlay de tier de cor por entidade.
2. **Pacote `clif_spawn_unit` estendido:** Byte customizado `tier_cor` (0, 1, 2) enviado pelo servidor ao cliente.
3. **Sistema de Analogias de Lore:** Módulo `advento_translations` para injeção de nomes de lore em toda a UI (Fase 5 do Roadmap).
4. **HUD Dual:** Termos técnicos no display + nomes de lore em tooltips e descrições.

---

## 🔗 Conexões Relacionadas

- ⬅️ **Pai:** [Visão Geral](../01-visao-geral.md)
- 🏠 **Home:** [ADVENTO](../../index.md)
- ⚙️ **Detalhes:** [Sistema Técnico](../../sistema-tecnico/05-sistema-tecnico.md); [Arquitetura Geral](../../sistema-tecnico/arquitetura/arquitetura-geral.md); [Comunicação Client-Server](../../sistema-tecnico/arquitetura/comunicacao-client-server.md)
- ⚙️ **Mecânica:** [Sistema de Combate](../../gameplay/sistema-de-combate.md) (shader de Visão Verdadeira)

*Última atualização: 2026-04-19*
