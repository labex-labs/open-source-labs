# Testcase : bornes vides

Une conséquence de la manière dont les bornes fonctionnent est que même si un `trait` ne contient aucune fonctionnalité, vous pouvez toujours l'utiliser comme une borne. `Eq` et `Copy` sont des exemples de tels `trait` de la bibliothèque `std`.

```rust
struct Cardinal;
struct BlueJay;
struct Turkey;

trait Red {}
trait Blue {}

impl Red for Cardinal {}
impl Blue for BlueJay {}

// Ces fonctions ne sont valides que pour les types qui implémentent ces
// traits. Le fait que les traits soient vides est sans importance.
fn red<T: Red>(_: &T)   -> &'static str { "red" }
fn blue<T: Blue>(_: &T) -> &'static str { "blue" }

fn main() {
    let cardinal = Cardinal;
    let blue_jay = BlueJay;
    let _turkey   = Turkey;

    // `red()` ne fonctionnera pas sur un geai bleu, ni vice versa
    // en raison des bornes.
    println!("Un cardinal est {}", red(&cardinal));
    println!("Un geai bleu est {}", blue(&blue_jay));
    //println!("Un dindon est {}", red(&_turkey));
    // ^ TODO : Essayez de décommenter cette ligne.
}
```
