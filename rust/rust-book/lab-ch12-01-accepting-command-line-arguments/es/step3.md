# Guardando los Valores de los Argumentos en Variables

El programa actualmente es capaz de acceder a los valores especificados como argumentos de línea de comandos. Ahora necesitamos guardar los valores de los dos argumentos en variables para poder usar los valores en el resto del programa. Hacemos eso en la Lista 12-2.

Nombre del archivo: `src/main.rs`

```rust
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    let query = &args[1];
    let file_path = &args[2];

    println!("Searching for {}", query);
    println!("In file {}", file_path);
}
```

Lista 12-2: Creando variables para almacenar el argumento de consulta y el argumento de ruta de archivo

Como vimos cuando imprimimos el vector, el nombre del programa ocupa el primer valor en el vector en `args[0]`, por lo que comenzamos a tomar argumentos a partir del índice 1. El primer argumento que `minigrep` toma es la cadena que estamos buscando, por lo que ponemos una referencia al primer argumento en la variable `query`. El segundo argumento será la ruta del archivo, por lo que ponemos una referencia al segundo argumento en la variable `file_path`.

Imprimimos temporalmente los valores de estas variables para probar que el código está funcionando como esperamos. Vamos a ejecutar este programa nuevamente con los argumentos `test` y `sample.txt`:

```bash
$ cargo run -- test sample.txt
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep test sample.txt`
Searching for test
In file sample.txt
```

Excelente, el programa está funcionando! Los valores de los argumentos que necesitamos se están guardando en las variables correctas. Más adelante agregaremos algún manejo de errores para manejar ciertas situaciones potencialmente erróneas, como cuando el usuario no proporciona ningún argumento; por ahora, ignoraremos esa situación y trabajaremos en agregar capacidades de lectura de archivos en su lugar.
