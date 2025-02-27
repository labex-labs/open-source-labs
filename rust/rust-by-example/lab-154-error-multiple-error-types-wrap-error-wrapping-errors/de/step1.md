# Fehler umschließen

Eine Alternative zur Boxing von Fehlern besteht darin, sie in einem eigenen Fehlertyp zu verpacken.

```rust
use std::error;
use std::error::Error;
use std::num::ParseIntError;
use std::fmt;

type Result<T> = std::result::Result<T, DoubleError>;

#[derive(Debug)]
enum DoubleError {
    EmptyVec,
    // Wir werden uns auf die Fehlermeldung der Parse-Funktion verlassen.
    // Zusätzliche Informationen erfordern die Hinzufügung von Daten zum Typ.
    Parse(ParseIntError),
}

impl fmt::Display for DoubleError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match *self {
            DoubleError::EmptyVec =>
                write!(f, "verwenden Sie bitte einen Vektor mit mindestens einem Element"),
            // Der umschlossene Fehler enthält zusätzliche Informationen und ist über die
            // source()-Methode verfügbar.
            DoubleError::Parse(..) =>
                write!(f, "der bereitgestellte String konnte nicht als Ganzzahl interpretiert werden"),
        }
    }
}

impl error::Error for DoubleError {
    fn source(&self) -> Option<&(dyn error::Error + 'static)> {
        match *self {
            DoubleError::EmptyVec => None,
            // Die Ursache ist der zugrunde liegende Implementierungsfehlertyp. Wird implizit
            // in das Trait-Objekt `&error::Error` umgewandelt. Dies funktioniert, da der
            // zugrunde liegende Typ bereits das `Error`-Trait implementiert.
            DoubleError::Parse(ref e) => Some(e),
        }
    }
}

// Implementieren Sie die Umwandlung von `ParseIntError` in `DoubleError`.
// Dies wird automatisch von `?` aufgerufen, wenn ein `ParseIntError`
// in einen `DoubleError` umgewandelt werden muss.
impl From<ParseIntError> for DoubleError {
    fn from(err: ParseIntError) -> DoubleError {
        DoubleError::Parse(err)
    }
}

fn double_first(vec: Vec<&str>) -> Result<i32> {
    let first = vec.first().ok_or(DoubleError::EmptyVec)?;
    // Hier verwenden wir implizit die `ParseIntError`-Implementierung von `From` (die wir
    // oben definiert haben), um einen `DoubleError` zu erstellen.
    let parsed = first.parse::<i32>()?;

    Ok(2 * parsed)
}

fn print(result: Result<i32>) {
    match result {
        Ok(n)  => println!("Das erste Element verdoppelt ist {}", n),
        Err(e) => {
            println!("Fehler: {}", e);
            if let Some(source) = e.source() {
                println!("  Ursache: {}", source);
            }
        },
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

Dies bringt etwas mehr Boilerplate für die Fehlerbehandlung mit sich und kann in allen Anwendungen möglicherweise nicht erforderlich sein. Es gibt einige Bibliotheken, die das Boilerplate für Sie übernehmen können.
