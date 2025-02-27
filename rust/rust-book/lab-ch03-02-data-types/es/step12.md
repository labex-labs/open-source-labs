# Acceso a Elementos de Array Inválido

Veamos qué pasa si intentas acceder a un elemento de un array que está más allá del final del array. Digamos que ejecutas este código, similar al juego de adivinanza del Capítulo 2, para obtener un índice de array del usuario:

Nombre del archivo: `src/main.rs`

```rust
use std::io;

fn main() {
    let a = [1, 2, 3, 4, 5];

    println!("Please enter an array index.");

    let mut index = String::new();

    io::stdin()
     .read_line(&mut index)
     .expect("Failed to read line");

    let index: usize = index
     .trim()
     .parse()
     .expect("Index entered was not a number");

    let element = a[index];

    println!(
        "The value of the element at index {index} is: {element}"
    );
}
```

Este código se compila correctamente. Si ejecutas este código usando `cargo run` y ingresas `0`, `1`, `2`, `3` o `4`, el programa imprimirá el valor correspondiente en ese índice del array. Si en cambio ingresas un número más allá del final del array, como `10`, verás una salida como esta:

    thread'main' panicked at 'index out of bounds: the len is 5 but the index is
    10', src/main.rs:19:19
    note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

El programa resultó en un error _en tiempo de ejecución_ en el momento de usar un valor inválido en la operación de indexación. El programa salió con un mensaje de error y no ejecutó la última declaración `println!`. Cuando intentas acceder a un elemento usando indexación, Rust verificará que el índice que has especificado sea menor que la longitud del array. Si el índice es mayor o igual que la longitud, Rust se detendrá abruptamente. Esta comprobación tiene que ocurrir en tiempo de ejecución, especialmente en este caso, porque el compilador no puede posiblemente saber qué valor un usuario ingresará cuando ejecute el código más adelante.

Este es un ejemplo de cómo se aplican los principios de seguridad de memoria de Rust. En muchos lenguajes de bajo nivel, este tipo de comprobación no se realiza, y cuando se proporciona un índice incorrecto, se puede acceder a memoria no válida. Rust te protege contra este tipo de error saliendo inmediatamente en lugar de permitir el acceso a la memoria y continuar. El Capítulo 9 discute más sobre el manejo de errores de Rust y cómo puedes escribir código legible y seguro que no se detenga abruptamente ni permita el acceso a memoria no válida.
