# Testfall: leere Schranken

Eine Folge davon, wie Schranken funktionieren, ist, dass Sie auch dann einen `trait` als Schranke verwenden können, wenn er keine Funktionalität enthält. `Eq` und `Copy` sind Beispiele für solche `trait`s aus der `std`-Bibliothek.

```rust
struct Cardinal;
struct BlueJay;
struct Turkey;

trait Red {}
trait Blue {}

impl Red for Cardinal {}
impl Blue for BlueJay {}

// Diese Funktionen sind nur gültig für Typen, die diese
// Traits implementieren. Dass die Traits leer sind, ist irrelevant.
fn red<T: Red>(_: &T)   -> &'static str { "rot" }
fn blue<T: Blue>(_: &T) -> &'static str { "blau" }

fn main() {
    let cardinal = Cardinal;
    let blue_jay = BlueJay;
    let _turkey   = Turkey;

    // `red()` funktioniert nicht für einen Blaumeise, und umgekehrt
    // wegen der Schranken.
    println!("Eine Kardinalen ist {}", red(&cardinal));
    println!("Eine Blaumeise ist {}", blue(&blue_jay));
    //println!("Eine Truthahn ist {}", red(&_turkey));
    // ^ TODO: Versuchen Sie, diese Zeile auszulassen.
}
```
