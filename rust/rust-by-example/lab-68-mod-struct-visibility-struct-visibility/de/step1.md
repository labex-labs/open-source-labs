# Sichtbarkeit von Structs

Structs haben eine zusätzliche Ebene der Sichtbarkeit für ihre Felder. Die Sichtbarkeit standardmäßig auf privat gesetzt und kann mit dem `pub`-Modifizierer überschrieben werden. Diese Sichtbarkeit spielt nur eine Rolle, wenn ein Struct von außerhalb des Moduls, in dem es definiert ist, zugegriffen wird, und hat das Ziel, Informationen zu verstecken (Kapselung).

```rust
mod my {
    // Ein öffentlicher Struct mit einem öffentlichen Feld vom generischen Typ `T`
    pub struct OpenBox<T> {
        pub contents: T,
    }

    // Ein öffentlicher Struct mit einem privaten Feld vom generischen Typ `T`
    pub struct ClosedBox<T> {
        contents: T,
    }

    impl<T> ClosedBox<T> {
        // Eine öffentliche Konstruktor-Methode
        pub fn new(contents: T) -> ClosedBox<T> {
            ClosedBox {
                contents: contents,
            }
        }
    }
}

fn main() {
    // Öffentliche Structs mit öffentlichen Feldern können wie üblich konstruiert werden
    let open_box = my::OpenBox { contents: "public information" };

    // und ihre Felder können normalerweise zugegriffen werden.
    println!("The open box contains: {}", open_box.contents);

    // Öffentliche Structs mit privaten Feldern können nicht mit Feldnamen konstruiert werden.
    // Fehler! `ClosedBox` hat private Felder
    //let closed_box = my::ClosedBox { contents: "classified information" };
    // TODO ^ Versuchen Sie, diese Zeile zu entsperren

    // Allerdings können Structs mit privaten Feldern mit
    // öffentlichen Konstruktoren erstellt werden
    let _closed_box = my::ClosedBox::new("classified information");

    // und die privaten Felder eines öffentlichen Structs können nicht zugegriffen werden.
    // Fehler! Das `contents`-Feld ist privat
    //println!("The closed box contains: {}", _closed_box.contents);
    // TODO ^ Versuchen Sie, diese Zeile zu entsperren
}
```
