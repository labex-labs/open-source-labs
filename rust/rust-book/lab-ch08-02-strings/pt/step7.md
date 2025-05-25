# Indexação em Strings

Em muitas outras linguagens de programação, acessar caracteres individuais em uma string referenciando-os por índice é uma operação válida e comum. No entanto, se você tentar acessar partes de uma `String` usando a sintaxe de indexação em Rust, você receberá um erro. Considere o código inválido na Listagem 8-19.

```rust
let s1 = String::from("hello");
let h = s1[0];
```

Listagem 8-19: Tentando usar a sintaxe de indexação com uma `String`

Este código resultará no seguinte erro:

```bash
error[E0277]: the type `String` cannot be indexed by `{integer}`
 --> src/main.rs:3:13
  |
3 |     let h = s1[0];
  |             ^^^^^ `String` cannot be indexed by `{integer}`
  |
  = help: the trait `Index<{integer}>` is not implemented for
`String`
```

O erro e a nota contam a história: strings Rust não suportam indexação. Mas por quê? Para responder a essa pergunta, precisamos discutir como o Rust armazena strings na memória.
