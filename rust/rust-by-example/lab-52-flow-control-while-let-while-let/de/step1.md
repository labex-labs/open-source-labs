# while let

Ähnlich wie `if let` kann `while let` unbequeme `match`-Sequenzen erträglicher machen. Betrachten Sie die folgende Sequenz, die `i` inkrementiert:

```rust
// Erstellt eine `Option<i32>`-Variable `optional` mit dem Wert `Some(0)`
let mut optional = Some(0);

// Wiederholt diesen Test.
loop {
    match optional {
        // Wenn `optional` zerlegt werden kann, wird der Block ausgewertet.
        Some(i) => {
            if i > 9 {
                println!("Größer als 9, abbrechen!");
                optional = None;
            } else {
                println!("`i` ist `{:?}`. Noch einmal versuchen.", i);
                optional = Some(i + 1);
            }
            // ^ Benötigt 3 Einzüge!
        },
        // Beendet die Schleife, wenn die Zerlegung fehlschlägt:
        _ => { break; }
        // ^ Warum sollte dies erforderlich sein? Es muss eine bessere Möglichkeit geben!
    }
}
```

Mit `while let` wird diese Sequenz viel schöner:

```rust
fn main() {
    // Erstellt eine `Option<i32>`-Variable `optional` mit dem Wert `Some(0)`
    let mut optional = Some(0);

    // Dies liest: "Solange `let` `optional` in `Some(i)` zerlegt,
    // wird der Block (`{}`) ausgewertet. Andernfalls `break`."
    while let Some(i) = optional {
        if i > 9 {
            println!("Größer als 9, abbrechen!");
            optional = None;
        } else {
            println!("`i` ist `{:?}`. Noch einmal versuchen.", i);
            optional = Some(i + 1);
        }
        // ^ Weniger Rechtsverschiebung und erfordert nicht,
        // den fehlgeschlagenen Fall explizit zu behandeln.
    }
    // ^ `if let` hatte zusätzliche optionale `else`/`else if`
    // Klauseln. `while let` hat diese nicht.
}
```
