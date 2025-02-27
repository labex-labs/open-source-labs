# Enlace

Acceder indirectamente a una variable hace imposible bifurcar y utilizar esa variable sin volver a enlazarla. `match` proporciona el símbolo `@` para enlazar valores a nombres:

```rust
// Una función `age` que devuelve un `u32`.
fn age() -> u32 {
    15
}

fn main() {
    println!("Dime de qué tipo de persona eres");

    match age() {
        0             => println!("Todavía no he celebrado mi primer cumpleaños"),
        // Podría `match` 1..= 12 directamente, pero entonces, ¿qué edad
        // tendría el niño? En cambio, enlaza a `n` para la
        // secuencia de 1..= 12. Ahora se puede informar la edad.
        n @ 1 ..= 12 => println!("Soy un niño de {:?} años", n),
        n @ 13..= 19 => println!("Soy un adolescente de {:?} años", n),
        // No se enlaza nada. Devuelve el resultado.
        n             => println!("Soy una persona mayor de {:?} años", n),
    }
}
```

También se puede usar el enlace para "desestructurar" variantes de `enum`, como `Option`:

```rust
fn some_number() -> Option<u32> {
    Some(42)
}

fn main() {
    match some_number() {
        // Obtuvo la variante `Some`, coincide si su valor, enlazado a `n`,
        // es igual a 42.
        Some(n @ 42) => println!("La respuesta: {}!", n),
        // Coincide con cualquier otro número.
        Some(n)      => println!("No es interesante... {}", n),
        // Coincide con cualquier otra cosa (`None` variante).
        _            => (),
    }
}
```
