# for-Schleifen

## for und Bereich

Der `for in`-Konstrukt kann verwendet werden, um über einen `Iterator` zu iterieren. Eine der einfachsten Möglichkeiten, einen Iterator zu erstellen, ist die Verwendung der Bereichsnotation `a..b`. Dies liefert Werte von `a` (inklusiv) bis `b` (exklusiv) in Schritten von eins.

Schreiben wir FizzBuzz mit `for` statt `while`.

```rust
fn main() {
    // `n` wird in jeder Iteration die Werte: 1, 2,..., 100 annehmen
    for n in 1..101 {
        if n % 15 == 0 {
            println!("fizzbuzz");
        } else if n % 3 == 0 {
            println!("fizz");
        } else if n % 5 == 0 {
            println!("buzz");
        } else {
            println!("{}", n);
        }
    }
}
```

Alternativ kann `a..=b` für einen Bereich verwendet werden, der an beiden Enden eingeschlossen ist. Das obige kann wie folgt geschrieben werden:

```rust
fn main() {
    // `n` wird in jeder Iteration die Werte: 1, 2,..., 100 annehmen
    for n in 1..=100 {
        if n % 15 == 0 {
            println!("fizzbuzz");
        } else if n % 3 == 0 {
            println!("fizz");
        } else if n % 5 == 0 {
            println!("buzz");
        } else {
            println!("{}", n);
        }
    }
}
```

## for und Iteratoren

Das `for in`-Konstrukt kann auf verschiedene Weise mit einem `Iterator` interagieren. Wie im Abschnitt über das Iterator-Trait diskutiert, wendet die `for`-Schleife standardmäßig die `into_iter`-Funktion auf die Sammlung an. Dies ist jedoch nicht die einzige Möglichkeit, um Sammlungen in Iteratoren umzuwandeln.

`into_iter`, `iter` und `iter_mut` behandeln alle die Umwandlung einer Sammlung in einen Iterator auf verschiedene Weise, indem sie verschiedene Ansichten auf die Daten innerhalb der Sammlung bieten.

- `iter` - Dies entleiht jedes Element der Sammlung bei jeder Iteration. Dadurch bleibt die Sammlung unberührt und kann nach der Schleife erneut verwendet werden.

```rust
fn main() {
    let names = vec!["Bob", "Frank", "Ferris"];

    for name in names.iter() {
        match name {
            &"Ferris" => println!("Es gibt einen Rustacean unter uns!"),
            // TODO ^ Versuchen Sie, das & zu löschen und nur "Ferris" zu matchen
            _ => println!("Hallo {}", name),
        }
    }

    println!("names: {:?}", names);
}
```

- `into_iter` - Dies konsumiert die Sammlung, sodass bei jeder Iteration die genauen Daten bereitgestellt werden. Nachdem die Sammlung konsumiert wurde, ist sie nicht mehr für die Wiederverwendung verfügbar, da sie innerhalb der Schleife "verschoben" wurde.

```rust
fn main() {
    let names = vec!["Bob", "Frank", "Ferris"];

    for name in names.into_iter() {
        match name {
            "Ferris" => println!("Es gibt einen Rustacean unter uns!"),
            _ => println!("Hallo {}", name),
        }
    }

    println!("names: {:?}", names);
    // FIXME ^ Kommentieren Sie diese Zeile aus
}
```

- `iter_mut` - Dies mutierbar entleiht jedes Element der Sammlung, was es ermöglicht, die Sammlung in-place zu modifizieren.

```rust
fn main() {
    let mut names = vec!["Bob", "Frank", "Ferris"];

    for name in names.iter_mut() {
        *name = match name {
            &mut "Ferris" => "Es gibt einen Rustacean unter uns!",
            _ => "Hallo",
        }
    }

    println!("names: {:?}", names);
}
```

In den obigen Codeausschnitten beachten Sie den Typ der `match`-Verzweigung, das ist der entscheidende Unterschied in den Typen der Iteration. Der Unterschied im Typ impliziert natürlich auch unterschiedliche Aktionen, die ausgeführt werden können.
