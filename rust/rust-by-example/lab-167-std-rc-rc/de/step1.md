# `Rc`

Wenn mehrfachige Besitzership erforderlich ist, kann `Rc` (Reference Counting) verwendet werden. `Rc` verfolgt die Anzahl der Referenzen, was die Anzahl der Besitzer des in einem `Rc` eingeschlossenen Werts bedeutet.

Der Referenzzähler eines `Rc` erhöht sich um 1, wenn ein `Rc` kloniert wird, und verringert sich um 1, wenn ein klonierter `Rc` außerhalb des Gültigkeitsbereichs fällt. Wenn der Referenzzähler eines `Rc` auf Null fällt (was bedeutet, dass keine Besitzer mehr vorhanden sind), werden sowohl der `Rc` als auch der Wert gelöscht.

Beim Klonen eines `Rc` wird nie eine Tiefenkopie durchgeführt. Klonen erstellt lediglich einen weiteren Zeiger auf den eingeschlossenen Wert und erhöht den Zähler.

```rust
use std::rc::Rc;

fn main() {
    let rc_examples = "Rc examples".to_string();
    {
        println!("--- rc_a wird erstellt ---");

        let rc_a: Rc<String> = Rc::new(rc_examples);
        println!("Referenzzähler von rc_a: {}", Rc::strong_count(&rc_a));

        {
            println!("--- rc_a wird zu rc_b kloniert ---");

            let rc_b: Rc<String> = Rc::clone(&rc_a);
            println!("Referenzzähler von rc_b: {}", Rc::strong_count(&rc_b));
            println!("Referenzzähler von rc_a: {}", Rc::strong_count(&rc_a));

            // Zwei `Rc`s sind gleich, wenn ihre inneren Werte gleich sind
            println!("rc_a und rc_b sind gleich: {}", rc_a.eq(&rc_b));

            // Wir können direkt Methoden eines Werts verwenden
            println!("Länge des Werts in rc_a: {}", rc_a.len());
            println!("Wert von rc_b: {}", rc_b);

            println!("--- rc_b fällt außerhalb des Gültigkeitsbereichs ---");
        }

        println!("Referenzzähler von rc_a: {}", Rc::strong_count(&rc_a));

        println!("--- rc_a fällt außerhalb des Gültigkeitsbereichs ---");
    }

    // Fehler! `rc_examples` wurde bereits in `rc_a` bewegt
    // Und wenn `rc_a` gelöscht wird, wird `rc_examples` ebenfalls gelöscht
    // println!("rc_examples: {}", rc_examples);
    // TODO ^ Versuchen Sie, diese Zeile auszukommentieren
}
```
