# Imprimir errores en el error estándar

Usaremos el código de la Lista 12-24 para cambiar cómo se imprimen los mensajes de error. Debido a la refactorización que hicimos al principio de este capítulo, todo el código que imprime mensajes de error está en una función, `main`. La biblioteca estándar proporciona la macro `eprintln!` que imprime en el flujo de error estándar, así que cambiemos los dos lugares donde estábamos llamando a `println!` para imprimir errores y usemos `eprintln!` en su lugar.

Nombre del archivo: `src/main.rs`

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

    let config = Config::build(&args).unwrap_or_else(|err| {
        eprintln!("Problem parsing arguments: {err}");
        process::exit(1);
    });

    if let Err(e) = minigrep::run(config) {
        eprintln!("Application error: {e}");
        process::exit(1);
    }
}
```

Lista 12-24: Escribir mensajes de error en el error estándar en lugar de la salida estándar usando `eprintln!`

Ahora ejecutemos el programa de nuevo de la misma manera, sin ningún argumento y redirigiendo la salida estándar con `>`:

```bash
$ cargo run > output.txt
Problem parsing arguments: not enough arguments
```

Ahora vemos el error en pantalla y _output.txt_ no contiene nada, que es el comportamiento que esperamos de los programas de línea de comandos.

Ejecutemos el programa de nuevo con argumentos que no causen un error pero sigan redirigiendo la salida estándar a un archivo, así:

```bash
cargo run -- to poem.txt > output.txt
```

No veremos ninguna salida en la terminal, y _output.txt_ contendrá nuestros resultados:

Nombre del archivo: output.txt

```rust
Are you nobody, too?
How dreary to be somebody!
```

Esto demuestra que ahora estamos usando la salida estándar para la salida exitosa y el error estándar para la salida de error, según corresponda.
