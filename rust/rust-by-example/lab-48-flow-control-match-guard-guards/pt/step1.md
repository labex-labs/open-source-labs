# Filtros (Guards)

Um filtro (`match guard`) pode ser adicionado para filtrar o ramo.

```rust
#[allow(dead_code)]
enum Temperature {
    Celsius(i32),
    Fahrenheit(i32),
}

fn main() {
    let temperature = Temperature::Celsius(35);
    // ^ TODO experimente diferentes valores para `temperature`

    match temperature {
        Temperature::Celsius(t) if t > 30 => println!("{}C está acima de 30 graus Celsius", t),
        // A parte `if condição` ^ é um filtro
        Temperature::Celsius(t) => println!("{}C está abaixo de 30 graus Celsius", t),

        Temperature::Fahrenheit(t) if t > 86 => println!("{}F está acima de 86 graus Fahrenheit", t),
        Temperature::Fahrenheit(t) => println!("{}F está abaixo de 86 graus Fahrenheit", t),
    }
}
```

Note que o compilador não levará em conta as condições de filtro ao verificar se todos os padrões estão cobertos pela expressão `match`.

```rust
fn main() {
    let number: u8 = 4;

    match number {
        i if i == 0 => println!("Zero"),
        i if i > 0 => println!("Maior que zero"),
        // _ => unreachable!("Deveria nunca acontecer."),
        // TODO ^ descomente para corrigir a compilação
    }
}
```
