# Caso de prueba: límites vacíos

Una consecuencia de cómo funcionan los límites es que incluso si un `trait` no incluye ninguna funcionalidad, aún puede utilizarse como límite. `Eq` y `Copy` son ejemplos de tales `trait`s de la biblioteca `std`.

```rust
struct Cardinal;
struct BlueJay;
struct Turkey;

trait Red {}
trait Blue {}

impl Red for Cardinal {}
impl Blue for BlueJay {}

// Estas funciones solo son válidas para los tipos que implementan estos
// traits. El hecho de que los traits estén vacíos es irrelevante.
fn red<T: Red>(_: &T)   -> &'static str { "red" }
fn blue<T: Blue>(_: &T) -> &'static str { "blue" }

fn main() {
    let cardinal = Cardinal;
    let blue_jay = BlueJay;
    let _turkey   = Turkey;

    // `red()` no funcionará en un jay azul ni viceversa
    // debido a los límites.
    println!("Un cardenal es {}", red(&cardinal));
    println!("Un jay azul es {}", blue(&blue_jay));
    //println!("Una pavo es {}", red(&_turkey));
    // ^ TODO: Intente descomentar esta línea.
}
```
