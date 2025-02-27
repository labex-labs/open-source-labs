# Veränderbarkeit

Die Veränderbarkeit von Daten kann sich ändern, wenn das Eigentum übertragen wird.

```rust
fn main() {
    let immutable_box = Box::new(5u32);

    println!("immutable_box enthält {}", immutable_box);

    // Veränderbarkeitsfehler
    //*immutable_box = 4;

    // *Verschieben* Sie die Box, um das Eigentum (und die Veränderbarkeit) zu ändern
    let mut mutable_box = immutable_box;

    println!("mutable_box enthält {}", mutable_box);

    // Ändern Sie den Inhalt der Box
    *mutable_box = 4;

    println!("mutable_box enthält jetzt {}", mutable_box);
}
```
