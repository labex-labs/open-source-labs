# `map` für `Result`

Das Abfangen von Fehlern im vorherigen Beispiel in der `multiply`-Funktion macht den Code nicht robust. Im Allgemeinen möchten wir den Fehler an den Aufrufer zurückgeben, damit dieser entscheiden kann, wie er am besten auf den Fehler reagieren soll.

Wir müssen zunächst wissen, welchen Fehlertyp wir behandeln. Um den `Err`-Typ zu bestimmen, schauen wir uns `parse()` an, das mit dem `FromStr`-Trait für `i32` implementiert ist. Folglich ist der `Err`-Typ als `ParseIntError` angegeben.

Im folgenden Beispiel führt der einfache `match`-Ausdruck zu einem insgesamt umständlicheren Code.

```rust
use std::num::ParseIntError;

// Nachdem der Rückgabetyp geändert wurde, verwenden wir die Mustermatching ohne `unwrap()`.
fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {
    match first_number_str.parse::<i32>() {
        Ok(first_number)  => {
            match second_number_str.parse::<i32>() {
                Ok(second_number)  => {
                    Ok(first_number * second_number)
                },
                Err(e) => Err(e),
            }
        },
        Err(e) => Err(e),
    }
}

fn print(result: Result<i32, ParseIntError>) {
    match result {
        Ok(n)  => println!("n ist {}", n),
        Err(e) => println!("Fehler: {}", e),
    }
}

fn main() {
    // Dies liefert immer noch eine vernünftige Antwort.
    let twenty = multiply("10", "2");
    print(twenty);

    // Dies liefert jetzt eine viel hilfreichere Fehlermeldung.
    let tt = multiply("t", "2");
    print(tt);
}
```

Zum Glück sind auch `map`, `and_then` und viele andere Kombinatoren von `Option` auch für `Result` implementiert. `Result` enthält eine vollständige Liste.

```rust
use std::num::ParseIntError;

// Wie bei `Option` können wir Kombinatoren wie `map()` verwenden.
// Diese Funktion ist ansonsten identisch zur obigen und lautet:
// Multipliziere, wenn beide Werte aus einem String geparst werden können, andernfalls übergebe den Fehler.
fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {
    first_number_str.parse::<i32>().and_then(|first_number| {
        second_number_str.parse::<i32>().map(|second_number| first_number * second_number)
    })
}

fn print(result: Result<i32, ParseIntError>) {
    match result {
        Ok(n)  => println!("n ist {}", n),
        Err(e) => println!("Fehler: {}", e),
    }
}

fn main() {
    // Dies liefert immer noch eine vernünftige Antwort.
    let twenty = multiply("10", "2");
    print(twenty);

    // Dies liefert jetzt eine viel hilfreichere Fehlermeldung.
    let tt = multiply("t", "2");
    print(tt);
}
```
