# Derive (Derivação)

O compilador é capaz de fornecer implementações básicas para alguns traits (características) através do atributo `#[derive]`. Estes traits ainda podem ser implementados manualmente se um comportamento mais complexo for necessário.

A seguir, uma lista de traits deriváveis:

- Traits de comparação: `Eq`, `PartialEq`, `Ord`, `PartialOrd`.
- `Clone`, para criar `T` a partir de `&T` via uma cópia.
- `Copy`, para dar a um tipo 'semântica de cópia' em vez de 'semântica de movimento'.
- `Hash`, para calcular um hash a partir de `&T`.
- `Default`, para criar uma instância vazia de um tipo de dado.
- `Debug`, para formatar um valor usando o formatador `{:?}`.

```rust
// `Centimeters`, uma struct de tupla que pode ser comparada
#[derive(PartialEq, PartialOrd)]
struct Centimeters(f64);

// `Inches`, uma struct de tupla que pode ser impressa
#[derive(Debug)]
struct Inches(i32);

impl Inches {
    fn to_centimeters(&self) -> Centimeters {
        let &Inches(inches) = self;

        Centimeters(inches as f64 * 2.54)
    }
}

// `Seconds`, uma struct de tupla sem atributos adicionais
struct Seconds(i32);

fn main() {
    let _one_second = Seconds(1);

    // Error: `Seconds` can't be printed; it doesn't implement the `Debug` trait
    //println!("One second looks like: {:?}", _one_second);
    // TODO ^ Try uncommenting this line

    // Error: `Seconds` can't be compared; it doesn't implement the `PartialEq` trait
    //let _this_is_true = (_one_second == _one_second);
    // TODO ^ Try uncommenting this line

    let foot = Inches(12);

    println!("One foot equals {:?}", foot);

    let meter = Centimeters(100.0);

    let cmp =
        if foot.to_centimeters() < meter {
            "smaller"
        } else {
            "bigger"
        };

    println!("One foot is {} than one meter.", cmp);
}
```
