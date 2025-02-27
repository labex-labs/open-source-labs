# `open`

La función `open` se puede utilizar para abrir un archivo en modo de solo lectura.

Un objeto `File` posee un recurso, el descriptor de archivo, y se encarga de cerrar el archivo cuando se lo `drop`ea.

```rust
use std::fs::File;
use std::io::prelude::*;
use std::path::Path;

fn main() {
    // Crea una ruta al archivo deseado
    let path = Path::new("hello.txt");
    let display = path.display();

    // Abre la ruta en modo de solo lectura, devuelve `io::Result<File>`
    let mut file = match File::open(&path) {
        Err(why) => panic!("no se pudo abrir {}: {}", display, why),
        Ok(file) => file,
    };

    // Lee el contenido del archivo en una cadena, devuelve `io::Result<usize>`
    let mut s = String::new();
    match file.read_to_string(&mut s) {
        Err(why) => panic!("no se pudo leer {}: {}", display, why),
        Ok(_) => print!("{} contiene:\n{}", display, s),
    }

    // El objeto `file` sale del ámbito, y el archivo "hello.txt" se cierra
}
```

A continuación se muestra la salida exitosa esperada:

```shell
$ echo "Hello World!" > hello.txt
$ rustc open.rs && ./open
hello.txt contiene:
Hello World!
```

(Se le anima a probar el ejemplo anterior en diferentes condiciones de error: `hello.txt` no existe, o `hello.txt` no es legible, etc.)
