# Dividir el Código en un Caja de Librería

Hasta ahora, nuestro proyecto `minigrep` se ve muy bien. Ahora dividiremos el archivo `src/main.rs` y pondremos un poco de código en el archivo `src/lib.rs`. De esta manera, podemos probar el código y tener un archivo `src/main.rs` con menos responsabilidades.

Movamos todo el código que no está en la función `main` de `src/main.rs` a `src/lib.rs`:

- La definición de la función `run`
- Las declaraciones `use` relevantes
- La definición de `Config`
- La definición de la función `Config::build`

El contenido de `src/lib.rs` debería tener las firmas mostradas en la Lista 12-13 (hemos omitido los cuerpos de las funciones por brevedad). Tenga en cuenta que esto no se compilará hasta que modifiquemos `src/main.rs` en la Lista 12-14.

Nombre de archivo: `src/lib.rs`

```rust
use std::error::Error;
use std::fs;

pub struct Config {
    pub query: String,
    pub file_path: String,
}

impl Config {
    pub fn build(
        args: &[String],
    ) -> Result<Config, &'static str> {
        --snip--
    }
}

pub fn run(config: Config) -> Result<(), Box<dyn Error>> {
    --snip--
}
```

Lista 12-13: Moviendo `Config` y `run` a `src/lib.rs`

Hemos usado ampliamente la palabra clave `pub`: en `Config`, en sus campos y su método `build`, y en la función `run`. Ahora tenemos una caja de librería que tiene una API pública que podemos probar.

Ahora necesitamos traer el código que movimos a `src/lib.rs` al alcance de la caja binaria en `src/main.rs`, como se muestra en la Lista 12-14.

Nombre de archivo: `src/main.rs`

```rust
use std::env;
use std::process;

use minigrep::Config;

fn main() {
    --snip--
    if let Err(e) = minigrep::run(config) {
        --snip--
    }
}
```

Lista 12-14: Usando la caja de librería `minigrep` en `src/main.rs`

Agregamos una línea `use minigrep::Config` para traer el tipo `Config` de la caja de librería al alcance de la caja binaria, y le agregamos el nombre de nuestra caja como prefijo a la función `run`. Ahora todas las funcionalidades deberían estar conectadas y deberían funcionar. Ejecute el programa con `cargo run` y asegúrese de que todo funcione correctamente.

¡Uy! Eso fue mucho trabajo, pero nos hemos preparado para el éxito en el futuro. Ahora es mucho más fácil manejar errores y hemos hecho el código más modular. Casi todo nuestro trabajo se hará en `src/lib.rs` a partir de ahora.

Vamos a aprovechar esta nueva modularidad haciendo algo que habría sido difícil con el código antiguo pero es fácil con el nuevo código: ¡escribiremos algunas pruebas!
