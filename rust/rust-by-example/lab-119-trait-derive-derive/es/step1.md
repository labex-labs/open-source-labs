# Derive

El compilador es capaz de proporcionar implementaciones básicas para algunos tratos a través del atributo `#[derive]`. Estos tratos todavía se pueden implementar manualmente si se requiere un comportamiento más complejo.

Lo siguiente es una lista de tratos derivables:

- Tratos de comparación: `Eq`, `PartialEq`, `Ord`, `PartialOrd`.
- `Clone`, para crear `T` a partir de `&T` a través de una copia.
- `Copy`, para dar a un tipo'semántica de copia' en lugar de'semántica de movimiento'.
- `Hash`, para calcular un hash a partir de `&T`.
- `Default`, para crear una instancia vacía de un tipo de datos.
- `Debug`, para formatear un valor usando el formateador `{:?}`.

```rust
// `Centimeters`, un struct de tupla que se puede comparar
#[derive(PartialEq, PartialOrd)]
struct Centimeters(f64);

// `Inches`, un struct de tupla que se puede imprimir
#[derive(Debug)]
struct Inches(i32);

impl Inches {
    fn to_centimeters(&self) -> Centimeters {
        let &Inches(inches) = self;

        Centimeters(inches as f64 * 2.54)
    }
}

// `Seconds`, un struct de tupla sin atributos adicionales
struct Seconds(i32);

fn main() {
    let _one_second = Seconds(1);

    // Error: `Seconds` no se puede imprimir; no implementa el trato `Debug`
    //println!("One second looks like: {:?}", _one_second);
    // TODO ^ Intenta descomentar esta línea

    // Error: `Seconds` no se puede comparar; no implementa el trato `PartialEq`
    //let _this_is_true = (_one_second == _one_second);
    // TODO ^ Intenta descomentar esta línea

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
