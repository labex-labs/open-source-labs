# Extracción del Analizador de Argumentos

Extraeremos la funcionalidad para analizar los argumentos en una función que `main` llamará para prepararnos para mover la lógica de análisis de línea de comandos a `src/lib.rs`. La Lista 12-5 muestra el nuevo comienzo de `main` que llama a una nueva función `parse_config`, que definiremos en `src/main.rs` por el momento.

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

    let (query, file_path) = parse_config(&args);

    --snip--
}

fn parse_config(args: &[String]) -> (&str, &str) {
    let query = &args[1];
    let file_path = &args[2];

    (query, file_path)
}
```

Lista 12-5: Extracción de una función `parse_config` de `main`

Todavía estamos recopilando los argumentos de línea de comandos en un vector, pero en lugar de asignar el valor del argumento en el índice 1 a la variable `query` y el valor del argumento en el índice 2 a la variable `file_path` dentro de la función `main`, pasamos todo el vector a la función `parse_config`. La función `parse_config` luego contiene la lógica que determina a qué variable va cada argumento y devuelve los valores a `main`. Todavía creamos las variables `query` y `file_path` en `main`, pero `main` ya no tiene la responsabilidad de determinar cómo se corresponden los argumentos de línea de comandos y las variables.

Este rehacer puede parecer un exceso para nuestro pequeño programa, pero estamos refactorizando en pasos pequeños e incrementales. Después de hacer este cambio, ejecute el programa nuevamente para verificar que el análisis de argumentos todavía funcione. Es bueno revisar tu progreso con frecuencia, para ayudar a identificar la causa de los problemas cuando ocurran.
