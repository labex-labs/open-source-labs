# Ein Fehlertyp definieren

Manchmal vereinfacht es den Code, alle verschiedenen Fehler mit einem einzigen Fehlertyp zu maskieren. Wir werden dies anhand eines benutzerdefinierten Fehlers zeigen.

Rust ermöglicht es uns, unsere eigenen Fehlertypen zu definieren. Im Allgemeinen ist ein "guter" Fehlertyp:

- Stellt verschiedene Fehler mit demselben Typ dar
- Gibt nette Fehlermeldungen an den Benutzer aus
- Ist leicht mit anderen Typen zu vergleichen
  - Gut: `Err(EmptyVec)`
  - Schlecht: `Err("Please use a vector with at least one element".to_owned())`
- Kann Informationen über den Fehler speichern
  - Gut: `Err(BadChar(c, position))`
  - Schlecht: `Err("+ cannot be used here".to_owned())`
- Kombiniert sich gut mit anderen Fehlern

```rust
use std::fmt;

type Result<T> = std::result::Result<T, DoubleError>;

// Definieren Sie unsere Fehlertypen. Diese können für unsere Fehlerbehandlungsszenarien angepasst werden.
// Jetzt können wir unsere eigenen Fehler schreiben, uns auf eine zugrunde liegende Fehlerimplementierung stützen
// oder etwas dazwischen tun.
#[derive(Debug, Clone)]
struct DoubleError;

// Die Generierung eines Fehlers ist völlig getrennt von der Art, wie er angezeigt wird.
// Es ist nicht erforderlich, sich um die Verschmutzung komplexer Logik mit dem Anzeige Stil zu kümmern.
//
// Beachten Sie, dass wir keine zusätzlichen Informationen über die Fehler speichern. Dies bedeutet, dass wir nicht angeben können,
// welche Zeichenfolge fehlgeschlagen ist, ohne unsere Typen zu ändern, um diese Information zu übermitteln.
impl fmt::Display for DoubleError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "invalid first item to double")
    }
}

fn double_first(vec: Vec<&str>) -> Result<i32> {
    vec.first()
        // Ändern Sie den Fehler in unseren neuen Typ um.
     .ok_or(DoubleError)
     .and_then(|s| {
            s.parse::<i32>()
                // Aktualisieren Sie auch hier auf den neuen Fehlertyp.
             .map_err(|_| DoubleError)
             .map(|i| 2 * i)
        })
}

fn print(result: Result<i32>) {
    match result {
        Ok(n) => println!("The first doubled is {}", n),
        Err(e) => println!("Error: {}", e),
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
