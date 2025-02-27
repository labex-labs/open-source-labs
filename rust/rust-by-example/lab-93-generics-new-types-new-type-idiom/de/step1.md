# Newtype-Idiom

Das Newtype-Idiom bietet Kompilierzeitgarantien dafür, dass der richtige Werttyp an ein Programm übergeben wird.

Beispielsweise muss einer Altersüberprüfungsfunktion, die das Alter in Jahren überprüft, ein Wert vom Typ `Years` übergeben werden.

```rust
struct Years(i64);

struct Days(i64);

impl Years {
    pub fn to_days(&self) -> Days {
        Days(self.0 * 365)
    }
}


impl Days {
    /// kürzt unvollständige Jahre ab
    pub fn to_years(&self) -> Years {
        Years(self.0 / 365)
    }
}

fn old_enough(age: &Years) -> bool {
    age.0 >= 18
}

fn main() {
    let age = Years(5);
    let age_days = age.to_days();
    println!("Alt genug {}", old_enough(&age));
    println!("Alt genug {}", old_enough(&age_days.to_years()));
    // println!("Alt genug {}", old_enough(&age_days));
}
```

Entkommentieren Sie die letzte Print-Anweisung, um zu beobachten, dass der übergebene Typ `Years` sein muss.

Um den Wert des Newtypes als Basistyp zu erhalten, können Sie die Tuple- oder Destrukturierungsyntax wie folgt verwenden:

```rust
struct Years(i64);

fn main() {
    let years = Years(42);
    let years_as_primitive_1: i64 = years.0; // Tuple
    let Years(years_as_primitive_2) = years; // Destructuring
}
```
