# Testfall: Verkettete Liste

Eine übliche Methode, um eine verkettete Liste zu implementieren, ist über `Enum`s:

```rust
use crate::List::*;

enum List {
    // Cons: Tupelstruktur, die ein Element und einen Zeiger auf den nächsten Knoten umschließt
    Cons(u32, Box<List>),
    // Nil: Ein Knoten, der das Ende der verketteten Liste angibt
    Nil,
}

// Methoden können an ein Enum angehängt werden
impl List {
    // Erstellt eine leere Liste
    fn new() -> List {
        // `Nil` hat den Typ `List`
        Nil
    }

    // Verbraucht eine Liste und gibt die gleiche Liste zurück, mit einem neuen Element am Anfang
    fn prepend(self, elem: u32) -> List {
        // `Cons` hat auch den Typ List
        Cons(elem, Box::new(self))
    }

    // Gibt die Länge der Liste zurück
    fn len(&self) -> u32 {
        // `self` muss abgeglichen werden, da sich das Verhalten dieser Methode
        // nach der Variante von `self` richtet
        // `self` hat den Typ `&List`, und `*self` hat den Typ `List`, ein Abgleich
        // auf einen konkreten Typ `T` ist bevorzugt gegenüber einem Abgleich auf eine Referenz `&T`
        // Nach Rust 2018 können Sie hier auch `self` verwenden und unten `tail` (ohne `ref`),
        // Rust wird die `&`s und `ref tail` ableiten.
        // Siehe https://doc.rust-lang.org/edition-guide/rust-2018/ownership-and-lifetimes/default-match-bindings.html
        match *self {
            // Kann die Besitzüberschrift des Schwanzes nicht ergreifen, da `self` entliehen ist;
            // stattdessen nehme eine Referenz auf den Schwanz
            Cons(_, ref tail) => 1 + tail.len(),
            // Basisfall: Eine leere Liste hat die Länge null
            Nil => 0
        }
    }

    // Gibt die Darstellung der Liste als (im Heap zugeordnete) Zeichenkette zurück
    fn stringify(&self) -> String {
        match *self {
            Cons(head, ref tail) => {
                // `format!` ist ähnlich zu `print!`, gibt jedoch eine im Heap zugeordnete Zeichenkette zurück
                // anstatt auf die Konsole zu drucken
                format!("{}, {}", head, tail.stringify())
            },
            Nil => {
                format!("Nil")
            },
        }
    }
}

fn main() {
    // Erstellt eine leere verkettete Liste
    let mut list = List::new();

    // Fügt einige Elemente am Anfang hinzu
    list = list.prepend(1);
    list = list.prepend(2);
    list = list.prepend(3);

    // Zeigt den Endzustand der Liste an
    println!("verkettete Liste hat die Länge: {}", list.len());
    println!("{}", list.stringify());
}
```
