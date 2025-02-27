# Funktionsparameter

Funktionsparameter können ebenfalls Muster sein. Der Code in Listing 18-6, der eine Funktion namens `foo` deklariert, die einen Parameter namens `x` vom Typ `i32` annimmt, sollte Ihnen jetzt vertraut vorkommen.

```rust
fn foo(x: i32) {
    // code goes here
}
```

Listing 18-6: Eine Funktionssignatur, die Muster in den Parametern verwendet

Der Teil `x` ist ein Muster! Wie bei `let` konnten wir ein Tupel in den Argumenten einer Funktion mit dem Muster abgleichen. Listing 18-7 teilt die Werte in einem Tupel auf, wenn wir es an eine Funktion übergeben.

Dateiname: `src/main.rs`

```rust
fn print_coordinates(&(x, y): &(i32, i32)) {
    println!("Current location: ({x}, {y})");
}

fn main() {
    let point = (3, 5);
    print_coordinates(&point);
}
```

Listing 18-7: Eine Funktion mit Parametern, die ein Tupel aufspalten

Dieser Code gibt `Current location: (3, 5)` aus. Die Werte `&(3, 5)` entsprechen dem Muster `&(x, y)`, sodass `x` der Wert `3` und `y` der Wert `5` ist.

Wir können auch Muster in Closure-Parameterlisten auf die gleiche Weise wie in Funktionsparameterlisten verwenden, da Closures ähnlich wie Funktionen sind, wie im Kapitel 13 diskutiert.

An diesem Punkt haben Sie verschiedene Möglichkeiten gesehen, Muster zu verwenden, aber Muster funktionieren nicht auf die gleiche Weise überall, wo wir sie verwenden können. An einigen Stellen müssen die Muster unwiderlegbar sein; in anderen Umständen können sie widerlegbar sein. Wir werden diese beiden Konzepte im nächsten Abschnitt diskutieren.
