# Crear rutas `use` idiómáticas

En la Lista 7-11, es posible que te hayas preguntado por qué especificamos `use crate::front_of_house::hosting` y luego llamamos a `hosting::add_to_waitlist` en `eat_at_restaurant`, en lugar de especificar la ruta `use` hasta la función `add_to_waitlist` para obtener el mismo resultado, como en la Lista 7-13.

Nombre del archivo: `src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

use crate::front_of_house::hosting::add_to_waitlist;

pub fn eat_at_restaurant() {
    add_to_waitlist();
}
```

Lista 7-13: Traer la función `add_to_waitlist` al alcance con `use`, lo cual no es idiómático

Aunque tanto la Lista 7-11 como la Lista 7-13 realizan la misma tarea, la Lista 7-11 es la forma idiómática de traer una función al alcance con `use`. Traer el módulo padre de la función al alcance con `use` significa que tenemos que especificar el módulo padre cuando llamamos a la función. Especificar el módulo padre cuando llamamos a la función hace que quede claro que la función no está definida localmente, mientras que minimiza la repetición de la ruta completa. El código de la Lista 7-13 no es claro sobre dónde está definida `add_to_waitlist`.

Por otro lado, cuando se traen structs, enums y otros elementos con `use`, es idiómático especificar la ruta completa. La Lista 7-14 muestra la forma idiómática de traer la struct `HashMap` de la biblioteca estándar al alcance de un crat binario.

Nombre del archivo: `src/main.rs`

```rust
use std::collections::HashMap;

fn main() {
    let mut map = HashMap::new();
    map.insert(1, 2);
}
```

Lista 7-14: Traer `HashMap` al alcance de una forma idiómática

No hay una razón fuerte detrás de este idioma: simplemente es la convención que ha surgido, y la gente se ha acostumbrado a leer y escribir código Rust de esta manera.

La excepción a este idioma es si estamos trayendo dos elementos con el mismo nombre al alcance con declaraciones `use`, porque Rust no lo permite. La Lista 7-15 muestra cómo traer dos tipos `Result` al alcance que tienen el mismo nombre pero módulos padres diferentes, y cómo hacer referencia a ellos.

Nombre del archivo: `src/lib.rs`

```rust
use std::fmt;
use std::io;

fn function1() -> fmt::Result {
    --snip--
}

fn function2() -> io::Result<()> {
    --snip--
}
```

Lista 7-15: Traer dos tipos con el mismo nombre al mismo alcance requiere usar sus módulos padres.

Como puedes ver, usar los módulos padres distingue los dos tipos `Result`. Si en cambio especificáramos `use std::fmt::Result` y `use std::io::Result`, tendríamos dos tipos `Result` en el mismo alcance, y Rust no sabría cuál de ellos queremos decir cuando usamos `Result`.
