# Implementando la Función `search_case_insensitive`

La función `search_case_insensitive`, mostrada en la Lista 12-21, será casi igual que la función `search`. La única diferencia es que convertiremos a minúsculas la `query` y cada `línea` para que, independientemente del caso de los argumentos de entrada, tengan el mismo caso cuando comprobamos si la línea contiene la consulta.

Nombre de archivo: `src/lib.rs`

```rust
pub fn search_case_insensitive<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
  1 let query = query.to_lowercase();
    let mut results = Vec::new();

    for line in contents.lines() {
        if 2 line.to_lowercase().contains(3 &query) {
            results.push(line);
        }
    }

    results
}
```

Lista 12-21: Definiendo la función `search_case_insensitive` para convertir a minúsculas la consulta y la línea antes de compararlas

Primero convertimos a minúsculas la cadena `query` y la almacenamos en una variable con el mismo nombre que la sombreada \[1\]. Llamar a `to_lowercase` en la consulta es necesario para que, independientemente de si la consulta del usuario es `"rust"`, `"RUST"`, `"Rust"` o `"rUsT"`, tratemos la consulta como si fuera `"rust"` y no distingamos entre mayúsculas y minúsculas. Si bien `to_lowercase` manejará los caracteres Unicode básicos, no será del 100% exacto. Si estuviéramos escribiendo una aplicación real, habría que hacer un poco más de trabajo aquí, pero esta sección es sobre variables de entorno, no sobre Unicode, así que lo dejaremos así por ahora.

Tenga en cuenta que `query` ahora es una `String` en lugar de una porción de cadena, porque llamar a `to_lowercase` crea nuevos datos en lugar de referenciar datos existentes. Digamos que la consulta es `"rUsT"`, por ejemplo: esa porción de cadena no contiene una `u` o `t` minúsculas para que podamos usarlas, así que tenemos que asignar una nueva `String` que contenga `"rust"`. Cuando pasamos `query` como argumento al método `contains` ahora, necesitamos agregar un signo de comercial \[3\] porque la firma de `contains` está definida para tomar una porción de cadena.

Luego, agregamos una llamada a `to_lowercase` en cada `línea` para convertir todos los caracteres a minúsculas \[2\]. Ahora que hemos convertido `línea` y `query` a minúsculas, encontraremos coincidencias independientemente del caso de la consulta.

Veamos si esta implementación pasa las pruebas:

    running 2 tests
    test tests::case_insensitive... ok
    test tests::case_sensitive... ok

    test result: ok. 2 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

Genial! Pasaron. Ahora, llamemos a la nueva función `search_case_insensitive` desde la función `run`. Primero agregaremos una opción de configuración al struct `Config` para alternar entre búsquedas sensibles y no sensibles a las mayúsculas y minúsculas. Agregar este campo causará errores del compilador porque aún no estamos inicializando este campo en ningún lugar:

Nombre de archivo: `src/lib.rs`

```rust
pub struct Config {
    pub query: String,
    pub file_path: String,
    pub ignore_case: bool,
}
```

Agregamos el campo `ignore_case` que contiene un booleano. A continuación, necesitamos que la función `run` compruebe el valor del campo `ignore_case` y use eso para decidir si llamar a la función `search` o la función `search_case_insensitive`, como se muestra en la Lista 12-22. Esto todavía no se compilará.

Nombre de archivo: `src/lib.rs`

```rust
pub fn run(config: Config) -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string(config.file_path)?;

    let results = if config.ignore_case {
        search_case_insensitive(&config.query, &contents)
    } else {
        search(&config.query, &contents)
    };

    for line in results {
        println!("{line}");
    }

    Ok(())
}
```

Lista 12-22: Llamando a `search` o `search_case_insensitive` según el valor en `config.ignore_case`

Finalmente, necesitamos comprobar la variable de entorno. Las funciones para trabajar con variables de entorno se encuentran en el módulo `env` de la biblioteca estándar, así que traemos ese módulo al ámbito en la parte superior de `src/lib.rs`. Luego usaremos la función `var` del módulo `env` para comprobar si se ha establecido algún valor para una variable de entorno llamada `IGNORE_CASE`, como se muestra en la Lista 12-23.

Nombre de archivo: `src/lib.rs`

```rust
use std::env;
--snip--

impl Config {
    pub fn build(
        args: &[String]
    ) -> Result<Config, &'static str> {
        if args.len() < 3 {
            return Err("not enough arguments");
        }

        let query = args[1].clone();
        let file_path = args[2].clone();

        let ignore_case = env::var("IGNORE_CASE").is_ok();

        Ok(Config {
            query,
            file_path,
            ignore_case,
        })
    }
}
```

Lista 12-23: Comprobando si hay algún valor en una variable de entorno llamada `IGNORE_CASE`

Aquí, creamos una nueva variable, `ignore_case`. Para establecer su valor, llamamos a la función `env::var` y le pasamos el nombre de la variable de entorno `IGNORE_CASE`. La función `env::var` devuelve un `Result` que será la variante exitosa `Ok` que contiene el valor de la variable de entorno si la variable de entorno está establecida con cualquier valor. Devolverá la variante `Err` si la variable de entorno no está establecida.

Estamos usando el método `is_ok` en el `Result` para comprobar si la variable de entorno está establecida, lo que significa que el programa debe realizar una búsqueda sin distinguir mayúsculas y minúsculas. Si la variable de entorno `IGNORE_CASE` no está establecida en nada, `is_ok` devolverá `false` y el programa realizará una búsqueda sensible a las mayúsculas y minúsculas. No nos importa el _valor_ de la variable de entorno, solo si está establecida o no, así que estamos comprobando `is_ok` en lugar de usar `unwrap`, `expect` o cualquiera de los otros métodos que hemos visto en `Result`.

Pasamos el valor de la variable `ignore_case` a la instancia de `Config` para que la función `run` pueda leer ese valor y decidir si llamar a `search_case_insensitive` o `search`, como implementamos en la Lista 12-22.

¡Intentémoslo! Primero ejecutaremos nuestro programa sin la variable de entorno establecida y con la consulta `to`, que debería coincidir con cualquier línea que contenga la palabra _to_ en minúsculas:

```bash
$ cargo run -- to poem.txt
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep to poem.txt`
Are you nobody, too?
How dreary to be somebody!
```

Parece que eso todavía funciona! Ahora ejecutemos el programa con `IGNORE_CASE` establecido en `1` pero con la misma consulta `to`:

```bash
IGNORE_CASE=1 cargo run -- to poem.txt
```

Si estás usando PowerShell, necesitarás establecer la variable de entorno y ejecutar el programa como comandos separados:

```rust
PS> $Env:IGNORE_CASE=1; cargo run -- to poem.txt
```

Esto hará que `IGNORE_CASE` persista durante el resto de tu sesión de shell. Puedes eliminar la variable con el cmdlet `Remove-Item`:

```rust
PS> Remove-Item Env:IGNORE_CASE
```

Deberíamos obtener líneas que contengan _to_ que pueden tener letras mayúsculas:

    Are you nobody, too?
    How dreary to be somebody!
    To tell your name the livelong day
    To an admiring bog!

Excelente, ¡también obtuvimos líneas que contienen _To_! Nuestro programa `minigrep` ahora puede realizar búsquedas sin distinguir mayúsculas y minúsculas controladas por una variable de entorno. Ahora sabes cómo manejar opciones configuradas mediante argumentos de línea de comandos o variables de entorno.

Algunos programas permiten argumentos _y_ variables de entorno para la misma configuración. En esos casos, los programas deciden que uno u otro tiene prioridad. Para otro ejercicio por tu cuenta, intenta controlar la sensibilidad a las mayúsculas y minúsculas a través de un argumento de línea de comandos o una variable de entorno. Decide si el argumento de línea de comandos o la variable de entorno debería tener prioridad si el programa se ejecuta con uno configurado para ser sensible a las mayúsculas y minúsculas y el otro configurado para ignorar el caso.

El módulo `std::env` contiene muchas más características útiles para trabajar con variables de entorno: consulta su documentación para ver lo que está disponible.
