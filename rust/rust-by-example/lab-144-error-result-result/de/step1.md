# `Result`

`Result` ist eine erweiterte Version des `Option`-Typs, der möglicherweise _Fehler_ statt möglicherweise _Fehlens_ beschreibt.

Das heißt, `Result<T, E>` kann eines von zwei Ergebnissen haben:

- `Ok(T)`: Ein Element `T` wurde gefunden
- `Err(E)`: Ein Fehler mit Element `E` wurde gefunden

Konventionell ist das erwartete Ergebnis `Ok`, während das unerwartete Ergebnis `Err` ist.

Wie `Option` hat `Result` viele ihm zugeordnete Methoden. `unwrap()`, zum Beispiel, liefert entweder das Element `T` oder `panic`s. Für den Fallhandhabung gibt es viele Kombinatoren zwischen `Result` und `Option`, die überlappen.

Beim Arbeiten mit Rust werden Sie wahrscheinlich Methoden finden, die den `Result`-Typ zurückgeben, wie z. B. die `parse()`-Methode. Es ist nicht immer möglich, einen String in den anderen Typ zu parsen, daher gibt `parse()` ein `Result`, das einen möglichen Fehler angibt.

Schauen wir uns an, was passiert, wenn wir einen String erfolgreich und erfolglos `parse()`:

```rust
fn multiply(first_number_str: &str, second_number_str: &str) -> i32 {
    // Versuchen wir, `unwrap()` zu verwenden, um die Zahl herauszubekommen. Wird es uns wehtun?
    let first_number = first_number_str.parse::<i32>().unwrap();
    let second_number = second_number_str.parse::<i32>().unwrap();
    first_number * second_number
}

fn main() {
    let twenty = multiply("10", "2");
    println!("double is {}", twenty);

    let tt = multiply("t", "2");
    println!("double is {}", tt);
}
```

Im erfolglosen Fall lässt `parse()` uns mit einem Fehler zurück, auf den `unwrap()` `panic`ieren kann. Darüber hinaus beendet der `panic` unseren Programm und gibt eine unangenehme Fehlermeldung aus.

Um die Qualität unserer Fehlermeldung zu verbessern, sollten wir den Rückgabetyp genauer definieren und den Fehler explizit behandeln.

## Verwendung von `Result` in `main`

Der `Result`-Typ kann auch der Rückgabetyp der `main`-Funktion sein, wenn er explizit angegeben wird. Typischerweise hat die `main`-Funktion die folgende Form:

```rust
fn main() {
    println!("Hello World!");
}
```

Allerdings kann `main` auch einen Rückgabetyp von `Result` haben. Wenn ein Fehler innerhalb der `main`-Funktion auftritt, wird ein Fehlercode zurückgegeben und eine Debug-Darstellung des Fehlers (mit dem \[`Debug`\]-Trait) ausgegeben. Im folgenden Beispiel wird ein solches Szenario gezeigt und Aspekte aus \[dem folgenden Abschnitt\] angesprochen.

```rust
use std::num::ParseIntError;

fn main() -> Result<(), ParseIntError> {
    let number_str = "10";
    let number = match number_str.parse::<i32>() {
        Ok(number)  => number,
        Err(e) => return Err(e),
    };
    println!("{}", number);
    Ok(())
}
```
