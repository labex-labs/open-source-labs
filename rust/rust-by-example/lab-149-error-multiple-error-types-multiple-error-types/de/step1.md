# Mehrere Fehlertypen

Die vorherigen Beispiele waren immer sehr bequem; `Result`s interagieren mit anderen `Result`s und `Option`s interagieren mit anderen `Option`s.

Manchmal muss eine `Option` mit einem `Result` interagieren, oder ein `Result<T, Error1>` muss mit einem `Result<T, Error2>` interagieren. In diesen Fällen möchten wir unsere verschiedenen Fehlertypen auf eine Weise verwalten, die sie komposierbar und einfach zu interagieren macht.

Im folgenden Code erzeugen zwei Instanzen von `unwrap` verschiedene Fehlertypen. `Vec::first` gibt eine `Option` zurück, während `parse::<i32>` ein `Result<i32, ParseIntError>` zurückgibt:

```rust
fn double_first(vec: Vec<&str>) -> i32 {
    let first = vec.first().unwrap(); // Erzeugt Fehler 1
    2 * first.parse::<i32>().unwrap() // Erzeugt Fehler 2
}

fn main() {
    let numbers = vec!["42", "93", "18"];
    let empty = vec![];
    let strings = vec!["tofu", "93", "18"];

    println!("Das erste verdoppelt ist {}", double_first(numbers));

    println!("Das erste verdoppelt ist {}", double_first(empty));
    // Fehler 1: Der Eingabevektor ist leer

    println!("Das erste verdoppelt ist {}", double_first(strings));
    // Fehler 2: Das Element kann nicht in eine Zahl umgewandelt werden
}
```

In den nächsten Abschnitten werden wir mehrere Strategien kennenlernen, um solche Probleme zu behandeln.
