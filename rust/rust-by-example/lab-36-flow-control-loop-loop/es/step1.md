# loop

Rust proporciona la palabra clave `loop` para indicar un bucle infinito.

La declaración `break` se puede utilizar para salir de un bucle en cualquier momento, mientras que la declaración `continue` se puede utilizar para omitir el resto de la iteración y comenzar una nueva.

```rust
fn main() {
    let mut count = 0u32;

    println!("Vamos a contar hasta el infinito!");

    // Bucle infinito
    loop {
        count += 1;

        if count == 3 {
            println!("tres");

            // Omite el resto de esta iteración
            continue;
        }

        println!("{}", count);

        if count == 5 {
            println!("OK, eso es suficiente");

            // Sale de este bucle
            break;
        }
    }
}
```
