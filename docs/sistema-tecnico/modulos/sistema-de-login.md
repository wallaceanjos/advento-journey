# 🔐 Sistema de Login

> [!ABSTRACT] 💡 Em uma frase
> O fluxo de autenticação de **Advento** segue o padrão rAthena, transformando o acesso técnico em um compromisso narrativo de vigilância em **Advenia**.

---

## Componentes do Fluxo

O login em Advenia é dividido em três camadas de autoridade:
1. **Autenticação (Login Server):** Validação de conta e token de sessão.
2. **Identidade (Char Server):** Recuperação da lista de Discípulos vinculados à conta.
3. **Presença (Map Server):** Inserção do Discípulo no território de **Advenia** onde ele parou sua última vigília.

---

## 🎨 Tela de Seleção de Personagem (Narrativa)

A interface de seleção de personagem materializa a responsabilidade da missão:

- **Cenário de Fundo:** A silhueta de **Advenia** sob a luz do entardecer — o mundo que aguarda pela Parusia.
- **Destaque do Discípulo:** O personagem aparece com as vestes do seu **Grau de Ministério** e animações de prontidão.
- **Texto de Introdução:** A página d'**O Livro** correspondente à vocação do Discípulo selecionado é exibida lateralmente.
- **Ação Principal:** O botão de entrada não diz "Jogar", mas sim **"Responder ao Chamado"**.

---

## ⚙️ Especificações Técnicas

- **rAthena:** Utiliza os pacotes padrão de login e seleção de personagem (`0x64`, `0x65`, `0x6b`).
- **Godot:** UI responsiva que suporta resoluções mobile e PC, com transições suaves de fade-in para a **Visão Natural** ao entrar no mundo.
- **Segurança:** Senhas criptografadas no banco de dados MySQL de Advenia.

## 🔗 Conexões Relacionadas
- ⬅️ **Pai:** [Sistema Técnico](../05-sistema-tecnico.md)
- 🏠 **Home:** [ADVENTO](../../index.md)
- 👤 **Início:** [Criação de Personagem](../../gameplay/criacao-de-personagem.md)
- 🧠 **Protocolo:** [Comunicação Client-Server](../arquitetura/comunicacao-client-server.md)

---
## 🧠 Análise do Agente
> O login é o primeiro ponto de contato com o **Realismo Espiritual**. Ao transformar a seleção de personagem em um "Responder ao Chamado", preparamos o psicológico do jogador para que ele entre no mundo não para "matar tempo", mas para exercer seu ministério em Advenia.

*Última atualização: 2026-05-01*
