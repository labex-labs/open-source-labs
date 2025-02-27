# Andere Verwendung von `?`

Bemerken Sie im vorherigen Beispiel, dass unsere unmittelbare Reaktion auf das Aufrufen von `parse` darin besteht, den Fehler von einem Bibliotheksfehler in einen boxing-Fehler zu `map`:

```rust
.and_then(|s| s.parse::<i32>())
  .map_err(|e| e.into())
```

Da dies eine einfache und häufige Operation ist, wäre es praktisch, wenn sie weggelassen werden könnte. Leider kann dies nicht, weil `and_then` nicht ausreichend flexibel ist. Wir können jedoch stattdessen `?` verwenden.

`?` wurde zuvor als entweder `unwrap` oder `return Err(err)` erklärt. Dies ist nur größtenteils wahr. Es bedeutet tatsächlich `unwrap` oder `return Err(From::from(err))`. Da `From::from` ein Konversionswerkzeug zwischen verschiedenen Typen ist, bedeutet dies, dass, wenn Sie `?` verwenden, wo der Fehler in den Rückgabetyp umgewandelt werden kann, er automatisch konvertiert wird.

Hier überschreiben wir das vorherige Beispiel mit `?`. Dadurch wird der `map_err` wegfallen, wenn `From::from` für unseren Fehlertyp implementiert ist:

```rust
use std::error;
use std::fmt;

// Ändern Sie den Alias in `Box<dyn error::Error>`.
type Result<T> = std::result::Result<T, Box<dyn error::Error>>;

#[derive(Debug)]
struct EmptyVec;

impl fmt::Display for EmptyVec {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "ungültiges erstes Element zum Verdoppeln")
    }
}

impl error::Error for EmptyVec {}

// Die gleiche Struktur wie zuvor, aber anstatt alle `Result` und `Option`
// entlang zu ketten, verwenden wir `?`, um den inneren Wert sofort zu extrahieren.
fn double_first(vec: Vec<&str>) -> Result<i32> {
    let first = vec.first().ok_or(EmptyVec)?;
    let parsed = first.parse::<i32>()?;
    Ok(2 * parsed)
}

fn print(result: Result<i32>) {
    match result {
        Ok(n)  => println!("Das erste verdoppelt ist {}", n),
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

Dies ist jetzt tatsächlich ziemlich sauber. Im Vergleich zum ursprünglichen `panic` ist es sehr ähnlich, `unwrap`-Aufrufe mit `?` zu ersetzen, nur dass die Rückgabetypen `Result` sind. Daher müssen sie auf der obersten Ebene zerstückt werden.
