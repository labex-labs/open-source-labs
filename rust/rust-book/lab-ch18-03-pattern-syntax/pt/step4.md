# Múltiplos Padrões (Multiple Patterns)

Em expressões `match`, você pode corresponder a múltiplos padrões usando a sintaxe `|`, que é o operador _or_ (ou) de padrão. Por exemplo, no código a seguir, comparamos o valor de `x` com os braços do match, o primeiro dos quais tem uma opção _or_, significando que se o valor de `x` corresponder a qualquer um dos valores naquele braço, o código desse braço será executado:

Nome do arquivo: `src/main.rs`

```rust
let x = 1;

match x {
    1 | 2 => println!("one or two"),
    3 => println!("three"),
    _ => println!("anything"),
}
```

Este código imprime `one or two`.
