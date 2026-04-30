# 🔐 Sistema de Login

> [!ABSTRACT] 💡 Em uma frase
> O fluxo de autenticação segue o padrão rAthena com um fluxo de seleção de personagem integrado à narrativa do Chamado.

---

## Componentes

- Tela de login (Godot — UI responsiva mobile/PC)
- Comunicação com servidor (rAthena `login-server`)
- Autenticação de conta (usuário + senha)
- Retorno de lista de personagens (pacote `0x6b`)
- Seleção de personagem → carregamento de mapa inicial

---

## Fluxo Técnico

```
[Tela de Login]
    → Input: usuário + senha
    → Envio para login-server (rAthena)
    → Autenticação bem-sucedida → token de sessão
    → Requisição de lista de personagens ao char-server
    → [Tela de Seleção de Personagem]
        → Jogador seleciona personagem
        → Requisição de mapa inicial ao map-server
        → [Carregamento de Mapa]
            → [Jogo em andamento]
```

---

## 🎨 Tela de Seleção de Personagem (Narrativo)

A tela de seleção de personagem no Advento não é uma tela técnica fria — ela tem contexto narrativo:

- **Fundo:** Silhueta de Aethelgard ao entardecer — o mundo que o jogador protege.
- **Personagem em destaque:** Classe visível com animação idle.
- **Texto de introdução:** Frase do Livro correspondente à classe.
- **Botão "Entrar":** Texto: *"Responder ao Chamado"* (não "Jogar" ou "Entrar").

---

## 🔗 Relacionado

- [Arquitetura Geral](../arquitetura/arquitetura-geral.md)
- [Comunicação Client-Server](../arquitetura/comunicacao-client-server.md)
- [Criação de Personagem](../../gameplay/criacao-de-personagem.md) (primeiro acesso; criação de conta + personagem)

*Última atualização: 2026-04-19*
