# Entleihen

In den meisten Fällen möchten wir auf Daten zugreifen, ohne die Eigentumsgewalt darüber zu übernehmen. Um dies zu erreichen, verwendet Rust ein _Entleihmechanismus_. Anstatt Objekte per Wert (`T`) zu übergeben, können Objekte per Referenz (`&T`) übergeben werden.

Der Compiler gewährleistet statisch (mittels seines Entleihprüfungsmechanismus), dass Referenzen _immer_ auf gültige Objekte verweisen. Das heißt, solange Referenzen auf ein Objekt existieren, kann das Objekt nicht zerstört werden.

```rust
// Diese Funktion übernimmt die Eigentumsgewalt an einer Box und zerstört sie
fn eat_box_i32(boxed_i32: Box<i32>) {
    println!("Zerstöre Box, die enthält {}", boxed_i32);
}

// Diese Funktion entleiht ein i32
fn borrow_i32(borrowed_i32: &i32) {
    println!("Dieser int ist: {}", borrowed_i32);
}

fn main() {
    // Erzeuge eine boxingtes i32 und ein stapelgespeichertes i32
    let boxed_i32 = Box::new(5_i32);
    let stacked_i32 = 6_i32;

    // Entleihe den Inhalt der Box. Die Eigentumsgewalt wird nicht übernommen,
    // sodass der Inhalt erneut entliehen werden kann.
    borrow_i32(&boxed_i32);
    borrow_i32(&stacked_i32);

    {
        // Nehme eine Referenz auf den Inhalt der Box
        let _ref_to_i32: &i32 = &boxed_i32;

        // Fehler!
        // Kann `boxed_i32` nicht zerstören, solange der innere Wert später im Gültigkeitsbereich entliehen wird.
        eat_box_i32(boxed_i32);
        // FIXME ^ Kommentiere diese Zeile aus

        // Versuche, `_ref_to_i32` nach dem Zerstören des inneren Werts zu entleihen
        borrow_i32(_ref_to_i32);
        // `_ref_to_i32` verlässt den Gültigkeitsbereich und wird nicht mehr entliehen.
    }

    // `boxed_i32` kann jetzt die Eigentumsgewalt an `eat_box` übergeben und zerstört werden
    eat_box_i32(boxed_i32);
}
```
