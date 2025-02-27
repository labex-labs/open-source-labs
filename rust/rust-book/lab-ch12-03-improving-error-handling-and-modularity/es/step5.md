# Creación de un Constructor para Config

Hasta ahora, hemos extraído la lógica responsable de analizar los argumentos de línea de comandos de `main` y la hemos colocado en la función `parse_config`. Hacer esto nos ayudó a ver que los valores `query` y `file_path` estaban relacionados, y esa relación debería transmitirse en nuestro código. Luego agregamos una estructura `Config` para nombrar el propósito relacionado de `query` y `file_path` y poder devolver los nombres de los valores como nombres de campos de estructura desde la función `parse_config`.

Entonces, ahora que el propósito de la función `parse_config` es crear una instancia de `Config`, podemos cambiar `parse_config` de una función simple a una función llamada `new` que está asociada con la estructura `Config`. Hacer este cambio hará que el código sea más idiómático. Podemos crear instancias de tipos en la biblioteca estándar, como `String`, llamando a `String::new`. Del mismo modo, al cambiar `parse_config` en una función `new` asociada con `Config`, podremos crear instancias de `Config` llamando a `Config::new`. La Lista 12-7 muestra los cambios que necesitamos hacer.

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

  1 let config = Config::new(&args);

    --snip--
}

--snip--

2 impl Config {
  3 fn new(args: &[String]) -> Config {
        let query = args[1].clone();
        let file_path = args[2].clone();

        Config { query, file_path }
    }
}
```

Lista 12-7: Cambio de `parse_config` a `Config::new`

Hemos actualizado `main` donde estábamos llamando a `parse_config` para llamar en su lugar a `Config::new` \[1\]. Hemos cambiado el nombre de `parse_config` a `new` \[3\] y lo hemos movido dentro de un bloque `impl` \[2\], lo que asocia la función `new` con `Config`. Intenta compilar este código nuevamente para asegurarte de que funcione.
