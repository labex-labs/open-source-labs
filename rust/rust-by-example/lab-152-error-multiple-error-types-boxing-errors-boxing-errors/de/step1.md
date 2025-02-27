# Fehler in eine `Box` packen

Ein Weg, einfachen Code zu schreiben, während man die ursprünglichen Fehler beibehält, besteht darin, sie in eine `Box` zu packen. Der Nachteil ist, dass der zugrunde liegende Fehlertyp nur zur Laufzeit bekannt ist und nicht statisch bestimmt werden kann.

Die Standardbibliothek hilft uns dabei, unsere Fehler in eine `Box` zu packen, indem `Box` die Umwandlung von jedem Typ, der das `Error`-Attribut implementiert, in das Attributobjekt `Box<Error>` über `From` implementiert.

```rust
use std::error;
use std::fmt;

// Ändern Sie den Alias in `Box<error::Error>`.
type Result<T> = std::result::Result<T, Box<dyn error::Error>>;

#[derive(Debug, Clone)]
struct EmptyVec;

impl fmt::Display for EmptyVec {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "ungültiges erstes Element zum Verdoppeln")
    }
}

impl error::Error for EmptyVec {}

fn double_first(vec: Vec<&str>) -> Result<i32> {
    vec.first()
     .ok_or_else(|| EmptyVec.into()) // Konvertiert in Box
     .and_then(|s| {
            s.parse::<i32>()
             .map_err(|e| e.into()) // Konvertiert in Box
             .map(|i| 2 * i)
        })
}

fn print(result: Result<i32>) {
    match result {
        Ok(n) => println!("Das erste verdoppelt ist {}", n),
        Err(e) => println!("Fehler: {}", e),
    }
}

fn main() {
    let numbers = vec!["42", "93", "18"];
    let empty = vec![];
    let strings = vec!["tofu", "93", "18"];

    print(double_first(numbers));
    print(double_first(empty));
    print(double_first(strings));
}
```
