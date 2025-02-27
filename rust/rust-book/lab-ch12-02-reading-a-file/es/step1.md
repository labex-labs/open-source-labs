# Leyendo un archivo

Ahora agregaremos funcionalidad para leer el archivo especificado en el argumento `file_path`. Primero necesitamos un archivo de muestra para probarlo: usaremos un archivo con un poco de texto en múltiples líneas con algunas palabras repetidas. La Lista 12-3 tiene un poema de Emily Dickinson que funcionará bien. Crea un archivo llamado _poema.txt_ en el nivel raíz de tu proyecto y escribe el poema "¡Soy nadie! ¿Quién eres tú?".

Nombre del archivo: poem.txt

    ¡Soy nadie! ¿Quién eres tú?
    ¿Eres nadie también?
    Entonces somos un par - ¡no lo cuentes!
    Sabes, nos expulsarían.

    ¡Qué aburrido ser alguien!
    ¡Qué público, como una rana
    Decir tu nombre durante todo el día
    A una pantano admirador!

Lista 12-3: Un poema de Emily Dickinson es un buen caso de prueba.

Con el texto en su lugar, edita `src/main.rs` y agrega código para leer el archivo, como se muestra en la Lista 12-4.

Nombre del archivo: `src/main.rs`

```rust
use std::env;
1 use std::fs;

fn main() {
    --snip--
    println!("In file {}", file_path);

  2 let contents = fs::read_to_string(file_path)
       .expect("Should have been able to read the file");

  3 println!("With text:\n{contents}");
}
```

Lista 12-4: Leyendo el contenido del archivo especificado por el segundo argumento

Primero traemos una parte relevante de la biblioteca estándar con una declaración `use`: necesitamos `std::fs` para manejar archivos \[1\].

En `main`, la nueva declaración `fs::read_to_string` toma el `file_path`, abre ese archivo y devuelve un `std::io::Result<String>` con el contenido del archivo \[2\].

Después de eso, agregamos nuevamente una declaración temporal `println!` que imprime el valor de `contents` después de leer el archivo, para que podamos comprobar que el programa está funcionando hasta ahora \[3\].

Ejecutemos este código con cualquier cadena como primer argumento de línea de comandos (porque aún no hemos implementado la parte de búsqueda) y el archivo _poema.txt_ como segundo argumento:

```bash
$ cargo run -- the poem.txt
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep the poem.txt`
Searching for the
In file poem.txt
With text:
¡Soy nadie! ¿Quién eres tú?
¿Eres nadie también?
Entonces somos un par - ¡no lo cuentes!
Sabes, nos expulsarían.

¡Qué aburrido ser alguien!
¡Qué público, como una rana
Decir tu nombre durante todo el día
A una pantano admirador!
```

¡Excelente! El código leyó y luego imprimió el contenido del archivo. Pero el código tiene algunos fallos. En este momento, la función `main` tiene múltiples responsabilidades: generalmente, las funciones son más claras y fáciles de mantener si cada función es responsable de solo una idea. El otro problema es que no estamos manejando los errores tan bien como podríamos. El programa todavía es pequeño, así que estos fallos no son un gran problema, pero a medida que el programa crece, será más difícil corregirlos de manera limpia. Es una buena práctica comenzar a refactorizar temprano durante el desarrollo de un programa porque es mucho más fácil refactorizar cantidades más pequeñas de código. Lo haremos a continuación.
