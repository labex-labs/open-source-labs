# Llamada a Config::build y Manejo de Errores

Para manejar el caso de error y mostrar un mensaje amigable para el usuario, necesitamos actualizar `main` para manejar el `Result` que está siendo devuelto por `Config::build`, como se muestra en la Lista 12-10. También tomaremos la responsabilidad de salir de la herramienta de línea de comandos con un código de error no nulo alejándonos de `panic!` y en su lugar lo implementaremos a mano. Un estado de salida no nulo es una convención para señalar al proceso que llamó a nuestro programa que el programa salió con un estado de error.

Nombre de archivo: `src/main.rs`

```rust
1 use std::process;

fn main() {
    let args: Vec<String> = env::args().collect();

  2 let config = Config::build(&args).3 unwrap_or_else(|4 err| {
      5 println!("Problema al analizar los argumentos: {err}");
      6 process::exit(1);
    });

    --snip--
```

Lista 12-10: Salir con un código de error si la construcción de un `Config` falla

En esta lista, hemos usado un método que no hemos cubierto en detalle todavía: `unwrap_or_else`, que está definido en `Result<T, E>` por la biblioteca estándar \[2\]. Usar `unwrap_or_else` nos permite definir un manejo de errores personalizado, no basado en `panic!`. Si el `Result` es un valor `Ok`, el comportamiento de este método es similar a `unwrap`: devuelve el valor interno que está envolviendo `Ok`. Sin embargo, si el valor es un valor `Err`, este método llama al código en la _clausura_, que es una función anónima que definimos y pasamos como argumento a `unwrap_or_else` \[3\]. Cubriremos las clausuras en más detalle en el Capítulo 13. Por ahora, solo necesitas saber que `unwrap_or_else` pasará el valor interno de `Err`, que en este caso es la cadena estática `"no hay suficientes argumentos"` que agregamos en la Lista 12-9, a nuestra clausura en el argumento `err` que aparece entre los tubos verticales \[4\]. El código en la clausura puede entonces usar el valor `err` cuando se ejecuta.

Hemos agregado una nueva línea `use` para traer `process` de la biblioteca estándar al alcance \[1\]. El código en la clausura que se ejecutará en el caso de error solo tiene dos líneas: imprimimos el valor `err` \[5\] y luego llamamos a `process::exit` \[6\]. La función `process::exit` detendrá el programa inmediatamente y devolverá el número que se pasó como código de estado de salida. Esto es similar al manejo basado en `panic!` que usamos en la Lista 12-8, pero ya no obtenemos toda la salida extra. Intentemoslo:

```bash
$ cargo run
   Compilando minigrep v0.1.0 (file:///projects/minigrep)
    Terminada la compilación en modo desarrollo [no optimizada + información de depuración] en 0.48s
     Ejecutando `target/debug/minigrep`
Problema al analizar los argumentos: no hay suficientes argumentos
```

¡Excelente! Esta salida es mucho más amigable para nuestros usuarios.
