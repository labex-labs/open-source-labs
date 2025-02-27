# Argumentos del programa

## Biblioteca estándar

Los argumentos de línea de comandos se pueden acceder utilizando `std::env::args`, que devuelve un iterador que produce una `String` para cada argumento:

```rust
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    // El primer argumento es la ruta que se utilizó para llamar al programa.
    println!("Mi ruta es {}.", args[0]);

    // El resto de los argumentos son los parámetros de línea de comandos pasados.
    // Llame al programa de la siguiente manera:
    //   $./args arg1 arg2
    println!("Recibí {:?} argumentos: {:?}.", args.len() - 1, &args[1..]);
}
```

```shell
$./args 1 2 3
Mi ruta es./args.
Recibí 3 argumentos: ["1", "2", "3"].
```

## Cajas

Alternativamente, hay numerosas cajas que pueden proporcionar funcionalidad adicional al crear aplicaciones de línea de comandos. El \[Rust Cookbook\] muestra las mejores prácticas sobre cómo utilizar una de las cajas de argumentos de línea de comandos más populares, `clap`.
