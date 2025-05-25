# Regras de Ownership

Primeiro, vamos dar uma olhada nas regras de _ownership_. Tenha estas regras em mente enquanto trabalhamos com os exemplos que as ilustram:

- Cada valor em Rust tem um _owner_ (proprietário).
- Pode haver apenas um proprietário por vez.
- Quando o proprietário sai do escopo, o valor será _dropped_ (liberado).
