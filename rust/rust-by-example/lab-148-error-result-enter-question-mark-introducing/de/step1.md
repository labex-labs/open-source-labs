# Einführung des `?`

Manchmal möchten wir einfach die Einfachheit von `unwrap` ohne die Möglichkeit eines `panic`. Bislang hat `unwrap` uns gezwungen, immer tiefer zu verschachteln, wenn wir eigentlich nur die Variable _herausholen_ wollten. Dies ist genau der Zweck von `?`.

Wenn ein `Err` gefunden wird, gibt es zwei gültige Aktionen:

1.  `panic!`, das wir bereits entschieden haben, möglichst zu vermeiden
2.  `return`, da ein `Err` bedeutet, dass es nicht behandelt werden kann

`?` ist _fast_\[\^†\] genau gleichwertig zu einem `unwrap`, das `return` statt `panic` bei `Err`s aufruft. Schauen wir uns an, wie wir das frühere Beispiel, das Kombinatoren verwendete, vereinfachen können:

```rust
use std::num::ParseIntError;

fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {
    let first_number = first_number_str.parse::<i32>()?;
    let second_number = second_number_str.parse::<i32>()?;

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

## Das `try!`-Makro

Bevor `?` existierte, wurde die gleiche Funktionalität mit dem `try!`-Makro erreicht. Der `?`-Operator wird jetzt empfohlen, aber Sie werden ihn möglicherweise immer noch in älterem Code finden. Die gleiche `multiply`-Funktion aus dem vorherigen Beispiel würde mit `try!` so aussehen:

```rust
// Um dieses Beispiel ohne Fehler zu kompilieren und auszuführen, während Sie Cargo verwenden, ändern Sie den Wert
// des `edition`-Felds im `[package]`-Abschnitt der `Cargo.toml`-Datei in "2015".

use std::num::ParseIntError;

fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {
    let first_number = try!(first_number_str.parse::<i32>());
    let second_number = try!(second_number_str.parse::<i32>());

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
