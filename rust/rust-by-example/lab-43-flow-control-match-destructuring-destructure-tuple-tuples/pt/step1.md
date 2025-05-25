# Tuplas

Tuplas podem ser desestruturadas em um `match` da seguinte forma:

```rust
fn main() {
    let triple = (0, -2, 3);
    // TODO ^ Tente diferentes valores para `triple`

    println!("Conte-me sobre {:?}", triple);
    // Match pode ser usado para desestruturar uma tupla
    match triple {
        // Desestruture o segundo e terceiro elementos
        (0, y, z) => println!("O primeiro é `0`, `y` é {:?}, e `z` é {:?}", y, z),
        (1, ..)  => println!("O primeiro é `1` e o resto não importa"),
        (.., 2)  => println!("O último é `2` e o resto não importa"),
        (3, .., 4)  => println!("O primeiro é `3`, o último é `4`, e o resto não importa"),
        // `..` pode ser usado para ignorar o resto da tupla
        _      => println!("Não importa quais são"),
        // `_` significa não vincular o valor a uma variável
    }
}
```
