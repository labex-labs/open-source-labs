# Display

`fmt::Debug` difícilmente parece compacto y limpio, por lo que a menudo es ventajoso personalizar la apariencia de salida. Esto se hace implementando manualmente `fmt::Display`, que utiliza el marcador de impresión `{}`. La implementación se ve así:

```rust
// Importa (a través de `use`) el módulo `fmt` para que esté disponible.
use std::fmt;

// Define una estructura para la cual se implementará `fmt::Display`. Esta es
// una struct tuple llamada `Structure` que contiene un `i32`.
struct Structure(i32);

// Para usar el marcador `{}`, el trato `fmt::Display` debe ser implementado
// manualmente para el tipo.
impl fmt::Display for Structure {
    // Este trato requiere `fmt` con esta firma exacta.
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        // Escribe estrictamente el primer elemento en el flujo de salida
        // suministrado: `f`. Devuelve `fmt::Result` que indica si la
        // operación tuvo éxito o fracasó. Tenga en cuenta que `write!` utiliza una sintaxis que
        // es muy similar a `println!`.
        write!(f, "{}", self.0)
    }
}
```

`fmt::Display` puede ser más limpio que `fmt::Debug`, pero esto presenta un problema para la biblioteca `std`. ¿Cómo se deben mostrar los tipos ambiguos? Por ejemplo, si la biblioteca `std` implementara un solo estilo para todos los `Vec<T>`, ¿cuál estilo debería ser? ¿Sería alguno de estos dos?

- `Vec<path>`: `/:/etc:/home/username:/bin` (dividido por `:`)
- `Vec<number>`: `1,2,3` (dividido por `,`)

No, porque no existe un estilo ideal para todos los tipos y la biblioteca `std` no presume dictar uno. `fmt::Display` no está implementado para `Vec<T>` ni para ningún otro contenedor genérico. Entonces, para estos casos genéricos, se debe utilizar `fmt::Debug`.

Sin embargo, esto no es un problema porque para cualquier nuevo tipo de _contenedor_ que _no_ sea genérico, se puede implementar `fmt::Display`.

```rust
use std::fmt; // Importa `fmt`

// Una estructura que contiene dos números. `Debug` se derivará para que los resultados puedan
// ser contrastados con `Display`.
#[derive(Debug)]
struct MinMax(i64, i64);

// Implementa `Display` para `MinMax`.
impl fmt::Display for MinMax {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        // Utiliza `self.number` para referirse a cada punto de datos posicional.
        write!(f, "({}, {})", self.0, self.1)
    }
}

// Define una estructura donde los campos son nombrables para la comparación.
#[derive(Debug)]
struct Point2D {
    x: f64,
    y: f64,
}

// Del mismo modo, implementa `Display` para `Point2D`.
impl fmt::Display for Point2D {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        // Personaliza para que solo se denoten `x` e `y`.
        write!(f, "x: {}, y: {}", self.x, self.y)
    }
}

fn main() {
    let minmax = MinMax(0, 14);

    println!("Compare structures:");
    println!("Display: {}", minmax);
    println!("Debug: {:?}", minmax);

    let big_range =   MinMax(-300, 300);
    let small_range = MinMax(-3, 3);

    println!("The big range is {big} and the small is {small}",
             small = small_range,
             big = big_range);

    let point = Point2D { x: 3.3, y: 7.2 };

    println!("Compare points:");
    println!("Display: {}", point);
    println!("Debug: {:?}", point);

    // Error. Tanto `Debug` como `Display` se implementaron, pero `{:b}`
    // requiere que se implemente `fmt::Binary`. Esto no funcionará.
    // println!("What does Point2D look like in binary: {:b}?", point);
}
```

Entonces, se ha implementado `fmt::Display` pero no `fmt::Binary`, y por lo tanto no se puede utilizar. `std::fmt` tiene muchos de estos `tratos` y cada uno requiere su propia implementación. Esto se detalla más en `std::fmt`.

## Actividad

Después de revisar la salida del ejemplo anterior, use la struct `Point2D` como guía para agregar una struct `Complex` al ejemplo. Cuando se imprima de la misma manera, la salida debe ser:

```txt
Display: 3.3 + 7.2i
Debug: Complex { real: 3.3, imag: 7.2 }
```
