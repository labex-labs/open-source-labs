# `Result`s aus `Option`s extrahieren

Der einfachste Weg, gemischte Fehlerarten zu behandeln, besteht darin, sie einfach ineinander zu schließen.

```rust
use std::num::ParseIntError;

fn double_first(vec: Vec<&str>) -> Option<Result<i32, ParseIntError>> {
    vec.first().map(|first| {
        first.parse::<i32>().map(|n| 2 * n)
    })
}

fn main() {
    let numbers = vec!["42", "93", "18"];
    let empty = vec![];
    let strings = vec!["tofu", "93", "18"];

    println!("The first doubled is {:?}", double_first(numbers));

    println!("The first doubled is {:?}", double_first(empty));
    // Error 1: die Eingabevektor ist leer

    println!("The first doubled is {:?}", double_first(strings));
    // Error 2: das Element kann nicht in eine Zahl umgewandelt werden
}
```

Es gibt Situationen, in denen wir bei einem Fehler die Verarbeitung abbrechen möchten (wie mit `?`), aber bei `None` des `Option`-Typs weiter machen möchten. Einige Kombinatoren helfen dabei, das `Result` und das `Option` zu tauschen.

```rust
use std::num::ParseIntError;

fn double_first(vec: Vec<&str>) -> Result<Option<i32>, ParseIntError> {
    let opt = vec.first().map(|first| {
        first.parse::<i32>().map(|n| 2 * n)
    });

    opt.map_or(Ok(None), |r| r.map(Some))
}

fn main() {
    let numbers = vec!["42", "93", "18"];
    let empty = vec![];
    let strings = vec!["tofu", "93", "18"];

    println!("The first doubled is {:?}", double_first(numbers));
    println!("The first doubled is {:?}", double_first(empty));
    println!("The first doubled is {:?}", double_first(strings));
}
```
