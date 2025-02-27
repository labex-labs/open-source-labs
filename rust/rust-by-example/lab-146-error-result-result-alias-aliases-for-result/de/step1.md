# Aliase für `Result`

Was ist, wenn wir einen bestimmten `Result`-Typ oftmals wiederverwenden möchten? Denken Sie daran, dass Rust uns erlaubt, Aliase zu erstellen. Zufällig können wir eines für den spezifischen `Result` definieren, über den wir sprechen.

Auf Modul Ebene kann das Erstellen von Aliasen besonders hilfreich sein. Fehler, die in einem bestimmten Modul gefunden werden, haben oft den gleichen `Err`-Typ, sodass ein einzelnes Alias alle zugehörigen `Results` präzise definieren kann. Dies ist so nützlich, dass die `std`-Bibliothek sogar einen liefert: `io::Result`!

Hier ist ein kurzes Beispiel, um die Syntax zu demonstrieren:

```rust
use std::num::ParseIntError;

// Definiere einen generischen Alias für ein `Result` mit dem Fehlertyp `ParseIntError`.
type AliasedResult<T> = Result<T, ParseIntError>;

// Verwende das obige Alias, um auf unseren spezifischen `Result`-Typ zu verweisen.
fn multiply(first_number_str: &str, second_number_str: &str) -> AliasedResult<i32> {
    first_number_str.parse::<i32>().and_then(|first_number| {
        second_number_str.parse::<i32>().map(|second_number| first_number * second_number)
    })
}

// Hier erlaubt uns das Alias wiederum, etwas Platz zu sparen.
fn print(result: AliasedResult<i32>) {
    match result {
        Ok(n)  => println!("n ist {}", n),
        Err(e) => println!("Fehler: {}", e),
    }
}

fn main() {
    print(multiply("10", "2"));
    print(multiply("t", "2"));
}
```
