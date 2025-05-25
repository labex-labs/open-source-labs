# Matches São Exaustivos

Há um outro aspecto do `match` que precisamos discutir: os padrões dos braços devem cobrir todas as possibilidades. Considere esta versão de nossa função `plus_one`, que tem um bug e não compilará:

```rust
fn plus_one(x: Option<i32>) -> Option<i32> {
    match x {
        Some(i) => Some(i + 1),
    }
}
```

Não tratamos o caso `None`, então este código causará um bug. Felizmente, é um bug que o Rust sabe como detectar. Se tentarmos compilar este código, obteremos este erro:

```bash
error[E0004]: non-exhaustive patterns: `None` not covered
 --> src/main.rs:3:15
  |
3 |         match x {
  |               ^ pattern `None` not covered
  |
  note: `Option<i32>` defined here
      = note: the matched value is of type `Option<i32>`
help: ensure that all possible cases are being handled by adding
a match arm with a wildcard pattern or an explicit pattern as
shown
    |
4   ~             Some(i) => Some(i + 1),
5   ~             None => todo!(),
    |
```

O Rust sabe que não cobrimos todos os casos possíveis e até sabe qual padrão esquecemos! Os matches em Rust são _exaustivos_: devemos esgotar todas as últimas possibilidades para que o código seja válido. Especialmente no caso de `Option<T>`, quando o Rust nos impede de esquecer de lidar explicitamente com o caso `None`, ele nos protege de presumir que temos um valor quando podemos ter nulo, tornando assim o erro de um bilhão de dólares discutido anteriormente impossível.
