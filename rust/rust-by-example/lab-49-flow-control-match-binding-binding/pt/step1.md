# Ligação

O acesso indireto a uma variável torna impossível ramificar e usar essa variável sem uma nova ligação. `match` fornece o símbolo `@` para vincular valores a nomes:

```rust
// Uma função `age` que retorna um `u32`.
fn age() -> u32 {
    15
}

fn main() {
    println!("Diga-me que tipo de pessoa você é");

    match age() {
        0             => println!("Ainda não celebrei meu primeiro aniversário"),
        // Poderíamos usar `match` 1 ..= 12 diretamente, mas qual seria a idade
        // da criança? Em vez disso, vincule a `n` para a sequência de 1 ..= 12.
        // Agora a idade pode ser relatada.
        n @ 1  ..= 12 => println!("Sou uma criança com {} anos de idade", n),
        n @ 13 ..= 19 => println!("Sou um adolescente com {} anos de idade", n),
        // Nada vinculado. Retorne o resultado.
        n             => println!("Sou uma pessoa mais velha com {} anos de idade", n),
    }
}
```

Também é possível usar ligação para "desestruturar" variantes de `enum`, como `Option`:

```rust
fn some_number() -> Option<u32> {
    Some(42)
}

fn main() {
    match some_number() {
        // Obteve a variante `Some`, verifique se seu valor, vinculado a `n`,
        // é igual a 42.
        Some(n @ 42) => println!("A Resposta: {}!", n),
        // Verifique qualquer outro número.
        Some(n)      => println!("Não é interessante... {}", n),
        // Verifique qualquer outra coisa (variante `None`).
        _            => (),
    }
}
```
