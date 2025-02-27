# Frühe Rückgaben

Im vorherigen Beispiel haben wir die Fehler explizit mit Kombinatoren behandelt. Ein anderer Weg, um mit dieser Fallunterscheidung umzugehen, ist die Verwendung einer Kombination von `match`-Anweisungen und _frühen Rückgaben_.

Das heißt, wir können einfach die Ausführung der Funktion abbrechen und den Fehler zurückgeben, wenn ein Fehler auftritt. Für manche kann diese Form von Code sowohl einfacher zu lesen als auch zu schreiben sein. Betrachten Sie diese Version des vorherigen Beispiels, das mit frühen Rückgaben umgeschrieben wurde:

```rust
use std::num::ParseIntError;

fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {
    let first_number = match first_number_str.parse::<i32>() {
        Ok(first_number)  => first_number,
        Err(e) => return Err(e),
    };

    let second_number = match second_number_str.parse::<i32>() {
        Ok(second_number)  => second_number,
        Err(e) => return Err(e),
    };

    Ok(first_number * second_number)
}

fn print(result: Result<i32, ParseIntError>) {
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

An diesem Punkt haben wir gelernt, Fehler explizit mit Kombinatoren und frühen Rückgaben zu behandeln. Während wir im Allgemeinen Paniks vermeiden möchten, ist es umständlich, alle unsere Fehler explizit zu behandeln.

Im nächsten Abschnitt werden wir `?` für die Fälle einführen, in denen wir einfach `unwrap` benötigen, ohne möglicherweise einen `Panik` auszulösen.
