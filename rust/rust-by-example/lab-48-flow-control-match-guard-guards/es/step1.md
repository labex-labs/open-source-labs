# Filtros

Se puede agregar un _filtro_ (`guard`) a la coincidencia (`match`) para filtrar el brazo (`arm`).

```rust
#[allow(dead_code)]
enum Temperature {
    Celsius(i32),
    Fahrenheit(i32),
}

fn main() {
    let temperature = Temperature::Celsius(35);
    // ^ TODO probar diferentes valores para `temperature`

    match temperature {
        Temperature::Celsius(t) if t > 30 => println!("{}C está por encima de 30 grados Celsius", t),
        // La parte `if condition` ^ es un filtro
        Temperature::Celsius(t) => println!("{}C está por debajo de 30 grados Celsius", t),

        Temperature::Fahrenheit(t) if t > 86 => println!("{}F está por encima de 86 grados Fahrenheit", t),
        Temperature::Fahrenheit(t) => println!("{}F está por debajo de 86 grados Fahrenheit", t),
    }
}
```

Tenga en cuenta que el compilador no tomará en cuenta las condiciones de filtro al comprobar si todos los patrones están cubiertos por la expresión `match`.

```rust
fn main() {
    let number: u8 = 4;

    match number {
        i if i == 0 => println!("Cero"),
        i if i > 0 => println!("Mayor que cero"),
        // _ => unreachable!("Nunca debería suceder."),
        // TODO ^ descomentar para solucionar la compilación
    }
}
```
