# match

Rust proporciona coincidencia de patrones a través de la palabra clave `match`, que se puede utilizar como un `switch` en C. La primera rama de coincidencia se evalúa y todos los valores posibles deben estar cubiertos.

```rust
fn main() {
    let number = 13;
    // TODO ^ Intenta diferentes valores para `number`

    println!("Dime algo sobre {}", number);
    match number {
        // Coincide con un solo valor
        1 => println!("Uno!"),
        // Coincide con varios valores
        2 | 3 | 5 | 7 | 11 => println!("Este es un número primo"),
        // TODO ^ Intenta agregar 13 a la lista de valores primos
        // Coincide con un rango inclusivo
        13..=19 => println!("Un adolescente"),
        // Maneja el resto de los casos
        _ => println!("No es especial"),
        // TODO ^ Intenta comentar esta rama general
    }

    let boolean = true;
    // Match es una expresión también
    let binary = match boolean {
        // Las ramas de un match deben cubrir todos los valores posibles
        false => 0,
        true => 1,
        // TODO ^ Intenta comentar una de estas ramas
    };

    println!("{} -> {}", boolean, binary);
}
```
