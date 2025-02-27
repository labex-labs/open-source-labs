# Enumerados (`enums`)

La palabra clave `enum` permite crear un tipo que puede ser una de varias variantes diferentes. Cualquier variante que sea válida como un `struct` también es válida en un `enum`.

```rust
// Crea un `enum` para clasificar un evento web. Observe cómo tanto
// los nombres como la información de tipo juntos especifican la variante:
// `PageLoad!= PageUnload` y `KeyPress(char)!= Paste(String)`.
// Cada una es diferente e independiente.
enum WebEvent {
    // Una variante de `enum` puede ser `sin campos`,
    PageLoad,
    PageUnload,
    // como structs tupla,
    KeyPress(char),
    Paste(String),
    // o estructuras similares a las de C.
    Click { x: i64, y: i64 },
}

// Una función que toma un `enum` WebEvent como argumento y
// no devuelve nada.
fn inspect(event: WebEvent) {
    match event {
        WebEvent::PageLoad => println!("página cargada"),
        WebEvent::PageUnload => println!("página descargada"),
        // Desestructura `c` desde dentro de la variante del `enum`.
        WebEvent::KeyPress(c) => println!("presionado '{}'.", c),
        WebEvent::Paste(s) => println!("pegado \"{}\".", s),
        // Desestructura `Click` en `x` e `y`.
        WebEvent::Click { x, y } => {
            println!("click en x={}, y={}.", x, y);
        },
    }
}

fn main() {
    let presionado = WebEvent::KeyPress('x');
    // `to_owned()` crea una `String` con propiedad a partir de una porción de cadena.
    let pegado  = WebEvent::Paste("mi texto".to_owned());
    let click   = WebEvent::Click { x: 20, y: 80 };
    let carga   = WebEvent::PageLoad;
    let descarga = WebEvent::PageUnload;

    inspect(presionado);
    inspect(pegado);
    inspect(click);
    inspect(carga);
    inspect(descarga);
}
```

## Alias de tipo

Si se utiliza un alias de tipo, se puede referir a cada variante de enumerado a través de su alias. Esto puede ser útil si el nombre del enumerado es demasiado largo o demasiado genérico y se desea cambiar su nombre.

```rust
enum VeryVerboseEnumOfThingsToDoWithNumbers {
    Add,
    Subtract,
}

// Crea un alias de tipo
type Operations = VeryVerboseEnumOfThingsToDoWithNumbers;

fn main() {
    // Podemos referirnos a cada variante a través de su alias, no su nombre
    // largo e incómodo.
    let x = Operations::Add;
}
```

El lugar más común donde se verá esto es en bloques `impl` que usan el alias `Self`.

```rust
enum VeryVerboseEnumOfThingsToDoWithNumbers {
    Add,
    Subtract,
}

impl VeryVerboseEnumOfThingsToDoWithNumbers {
    fn run(&self, x: i32, y: i32) -> i32 {
        match self {
            Self::Add => x + y,
            Self::Subtract => x - y,
        }
    }
}
```

Para aprender más sobre enumerados y alias de tipo, puede leer el informe de estabilización de cuando esta característica se estabilizó en Rust.
