# Veränderbarkeit

Änderbare Daten können über `&mut T` änderbar entliehen werden. Dies wird als _änderbare Referenz_ bezeichnet und gibt dem Entleiher Lese-/Schreibzugang. Im Gegensatz dazu entleiht `&T` die Daten über eine nicht änderbare Referenz, und der Entleiher kann die Daten lesen, aber nicht modifizieren:

```rust
#[allow(dead_code)]
#[derive(Clone, Copy)]
struct Book {
    // `&'static str` ist eine Referenz auf einen in nur lesbarer Speicher zugewiesenen String
    author: &'static str,
    title: &'static str,
    year: u32,
}

// Diese Funktion nimmt eine Referenz auf ein Buch entgegen
fn borrow_book(book: &Book) {
    println!("Ich habe {} - {} Auflage unveränderlich entliehen", book.title, book.year);
}

// Diese Funktion nimmt eine Referenz auf ein änderbares Buch entgegen und ändert `year` auf 2014
fn new_edition(book: &mut Book) {
    book.year = 2014;
    println!("Ich habe {} - {} Auflage änderbar entliehen", book.title, book.year);
}

fn main() {
    // Erzeuge ein unveränderliches Buch namens `immutabook`
    let immutabook = Book {
        // Stringliterale haben den Typ `&'static str`
        author: "Douglas Hofstadter",
        title: "Gödel, Escher, Bach",
        year: 1979,
    };

    // Erzeuge eine änderbare Kopie von `immutabook` und nenne es `mutabook`
    let mut mutabook = immutabook;

    // Entleihe ein unveränderliches Objekt unveränderlich
    borrow_book(&immutabook);

    // Entleihe ein änderbares Objekt unveränderlich
    borrow_book(&mutabook);

    // Entleihe ein änderbares Objekt als änderbar
    new_edition(&mut mutabook);

    // Fehler! Ein unveränderliches Objekt kann nicht als änderbar entliehen werden
    new_edition(&mut immutabook);
    // FIXME ^ Kommentiere diese Zeile aus
}
```
