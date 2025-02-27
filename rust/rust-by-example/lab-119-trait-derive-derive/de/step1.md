# Ableiten

Der Compiler kann grundlegende Implementierungen für einige Traits über das `#[derive]`-Attribut bereitstellen. Diese Traits können immer noch manuell implementiert werden, wenn ein komplexeres Verhalten erforderlich ist.

Das folgende ist eine Liste von ableitbaren Traits:

- Vergleichsmerkmale: `Eq`, `PartialEq`, `Ord`, `PartialOrd`.
- `Clone`, um `T` aus `&T` über eine Kopie zu erstellen.
- `Copy`, um einem Typ „Kopiersemantik“ statt „Move-Semantik“ zu geben.
- `Hash`, um einen Hash aus `&T` zu berechnen.
- `Default`, um eine leere Instanz eines Datentyps zu erstellen.
- `Debug`, um einen Wert mit dem `{:?}`-Formatierer zu formatieren.

```rust
// `Centimeters`, eine Tupelstruktur, die verglichen werden kann
#[derive(PartialEq, PartialOrd)]
struct Centimeters(f64);

// `Inches`, eine Tupelstruktur, die gedruckt werden kann
#[derive(Debug)]
struct Inches(i32);

impl Inches {
    fn to_centimeters(&self) -> Centimeters {
        let &Inches(inches) = self;

        Centimeters(inches as f64 * 2.54)
    }
}

// `Seconds`, eine Tupelstruktur ohne zusätzliche Attribute
struct Seconds(i32);

fn main() {
    let _one_second = Seconds(1);

    // Fehler: `Seconds` kann nicht gedruckt werden; es implementiert das `Debug`-Trait nicht
    //println!("One second looks like: {:?}", _one_second);
    // TODO ^ Versuchen Sie, diese Zeile zu entsperren

    // Fehler: `Seconds` kann nicht verglichen werden; es implementiert das `PartialEq`-Trait nicht
    //let _this_is_true = (_one_second == _one_second);
    // TODO ^ Versuchen Sie, diese Zeile zu entsperren

    let foot = Inches(12);

    println!("One foot equals {:?}", foot);

    let meter = Centimeters(100.0);

    let cmp =
        if foot.to_centimeters() < meter {
            "smaller"
        } else {
            "bigger"
        };

    println!("One foot is {} than one meter.", cmp);
}
```
