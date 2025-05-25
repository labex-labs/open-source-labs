# Caso de Teste: Limites Vazios

Uma consequência de como os limites funcionam é que, mesmo que um `trait` não inclua nenhuma funcionalidade, você ainda pode usá-lo como um limite. `Eq` e `Copy` são exemplos de tais `traits` da biblioteca `std`.

```rust
struct Cardinal;
struct BlueJay;
struct Turkey;

trait Red {}
trait Blue {}

impl Red for Cardinal {}
impl Blue for BlueJay {}

// Essas funções só são válidas para tipos que implementam esses
// traits. O fato de os traits serem vazios é irrelevante.
fn red<T: Red>(_: &T)   -> &'static str { "red" }
fn blue<T: Blue>(_: &T) -> &'static str { "blue" }

fn main() {
    let cardinal = Cardinal;
    let blue_jay = BlueJay;
    let _turkey   = Turkey;

    // `red()` não funcionará em um blue jay nem vice-versa
    // devido aos limites.
    println!("Um cardinal é {}", red(&cardinal));
    println!("Um blue jay é {}", blue(&blue_jay));
    //println!("Uma turkey é {}", red(&_turkey));
    // ^ TODO: Tente descomentar esta linha.
}
```
