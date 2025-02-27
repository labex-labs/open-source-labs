# Aliasing

Daten können beliebig oft unverändert entliehen werden, aber während sie unverändert entliehen sind, können sie nicht veränderlich entliehen werden. Andererseits ist nur _ein_ veränderlicher Entleihe zu einem Zeitpunkt erlaubt. Die ursprünglichen Daten können erst _nach_ der letzten Verwendung der veränderlichen Referenz erneut entliehen werden.

```rust
struct Point { x: i32, y: i32, z: i32 }

fn main() {
    let mut point = Point { x: 0, y: 0, z: 0 };

    let borrowed_point = &point;
    let another_borrow = &point;

    // Daten können über die Referenzen und den ursprünglichen Besitzer zugegriffen werden
    println!("Point hat Koordinaten: ({}, {}, {})",
                borrowed_point.x, another_borrow.y, point.z);

    // Fehler! `point` kann nicht als veränderlich entliehen werden, da es derzeit
    // als unveränderlich entliehen ist.
    // let mutable_borrow = &mut point;
    // TODO ^ Versuchen Sie, diese Zeile auszukommentieren

    // Die entliehenen Werte werden hier erneut verwendet
    println!("Point hat Koordinaten: ({}, {}, {})",
                borrowed_point.x, another_borrow.y, point.z);

    // Die unveränderlichen Referenzen werden für den Rest des Codes nicht mehr verwendet, sodass
    // es möglich ist, mit einer veränderlichen Referenz erneut zu entleihen.
    let mutable_borrow = &mut point;

    // Daten über die veränderliche Referenz ändern
    mutable_borrow.x = 5;
    mutable_borrow.y = 2;
    mutable_borrow.z = 1;

    // Fehler! `point` kann nicht als unveränderlich entliehen werden, da es derzeit
    // als veränderlich entliehen ist.
    // let y = &point.y;
    // TODO ^ Versuchen Sie, diese Zeile auszukommentieren

    // Fehler! Es kann nicht gedruckt werden, da `println!` eine unveränderliche Referenz erwartet.
    // println!("Point Z-Koordinate ist {}", point.z);
    // TODO ^ Versuchen Sie, diese Zeile auszukommentieren

    // Ok! Veränderliche Referenzen können als unveränderlich an `println!` übergeben werden
    println!("Point hat Koordinaten: ({}, {}, {})",
                mutable_borrow.x, mutable_borrow.y, mutable_borrow.z);

    // Die veränderliche Referenz wird für den Rest des Codes nicht mehr verwendet, sodass es
    // möglich ist, erneut zu entleihen
    let new_borrowed_point = &point;
    println!("Point hat jetzt Koordinaten: ({}, {}, {})",
             new_borrowed_point.x, new_borrowed_point.y, new_borrowed_point.z);
}
```
