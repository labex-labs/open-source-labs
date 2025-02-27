# Traits

Natürlich können auch `Trait`s generisch sein. Hier definieren wir eines, das das `Drop`-`Trait` als eine generische Methode neu implementiert, um sich selbst und einen Eingabeparameter zu `entfernen`.

```rust
// Nicht kopierbare Typen.
struct Empty;
struct Null;

// Ein Trait, das über `T` generisch ist.
trait DoubleDrop<T> {
    // Definiere eine Methode auf dem aufrufenden Typ, die einen
    // zusätzlichen einzelnen Parameter `T` annimmt und nichts damit macht.
    fn double_drop(self, _: T);
}

// Implementiere `DoubleDrop<T>` für jeden generischen Parameter `T` und
// aufrufenden Typ `U`.
impl<T, U> DoubleDrop<T> for U {
    // Diese Methode übernimmt die Besitznahme beider übergebenen Argumente
    // und entfernt beide.
    fn double_drop(self, _: T) {}
}

fn main() {
    let empty = Empty;
    let null  = Null;

    // Entferne `empty` und `null`.
    empty.double_drop(null);

    //empty;
    //null;
    // ^ TODO: Versuche, diese Zeilen auszukommentieren.
}
```
