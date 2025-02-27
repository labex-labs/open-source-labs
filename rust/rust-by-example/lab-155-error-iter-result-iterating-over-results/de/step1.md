# Iterieren über `Result`s

Eine `Iter::map`-Operation kann fehlschlagen, z.B.:

```rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
    let numbers: Vec<_> = strings
     .into_iter()
     .map(|s| s.parse::<i32>())
     .collect();
    println!("Results: {:?}", numbers);
}
```

Schauen wir uns die Strategien an, um dies zu behandeln.

## Ignorieren Sie die fehlgeschlagenen Elemente mit `filter_map()`

`filter_map` ruft eine Funktion auf und filtert die Ergebnisse, die `None` sind.

```rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
    let numbers: Vec<_> = strings
     .into_iter()
     .filter_map(|s| s.parse::<i32>().ok())
     .collect();
    println!("Results: {:?}", numbers);
}
```

## Sammeln Sie die fehlgeschlagenen Elemente mit `map_err()` und `filter_map()`

`map_err` ruft eine Funktion mit dem Fehler auf, so dass wir sie, indem wir sie der vorherigen `filter_map`-Lösung hinzufügen, während des Iterierens beiseite legen können.

```rust
fn main() {
    let strings = vec!["42", "tofu", "93", "999", "18"];
    let mut errors = vec![];
    let numbers: Vec<_> = strings
     .into_iter()
     .map(|s| s.parse::<u8>())
     .filter_map(|r| r.map_err(|e| errors.push(e)).ok())
     .collect();
    println!("Numbers: {:?}", numbers);
    println!("Errors: {:?}", errors);
}
```

## Den gesamten Vorgang mit `collect()` abbrechen

`Result` implementiert `FromIterator`, sodass ein Vektor von Ergebnissen (`Vec<Result<T, E>>`) in ein Ergebnis mit einem Vektor (`Result<Vec<T>, E>`) umgewandelt werden kann. Sobald ein `Result::Err` gefunden wird, wird die Iteration abgebrochen.

```rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
    let numbers: Result<Vec<_>, _> = strings
     .into_iter()
     .map(|s| s.parse::<i32>())
     .collect();
    println!("Results: {:?}", numbers);
}
```

Dieselbe Technik kann mit `Option` verwendet werden.

## Sammeln Sie alle gültigen Werte und Fehler mit `partition()`

```rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
    let (numbers, errors): (Vec<_>, Vec<_>) = strings
     .into_iter()
     .map(|s| s.parse::<i32>())
     .partition(Result::is_ok);
    println!("Numbers: {:?}", numbers);
    println!("Errors: {:?}", errors);
}
```

Wenn Sie sich die Ergebnisse ansehen, werden Sie feststellen, dass alles immer noch in `Result` eingeschlossen ist. Dafür ist ein bisschen mehr Boilerplate erforderlich.

```rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
    let (numbers, errors): (Vec<_>, Vec<_>) = strings
     .into_iter()
     .map(|s| s.parse::<i32>())
     .partition(Result::is_ok);
    let numbers: Vec<_> = numbers.into_iter().map(Result::unwrap).collect();
    let errors: Vec<_> = errors.into_iter().map(Result::unwrap_err).collect();
    println!("Numbers: {:?}", numbers);
    println!("Errors: {:?}", errors);
}
```
