# Verbleibende Teile eines Werts mit `..`

Bei Werten, die viele Teile haben, können wir die Syntax `..` verwenden, um bestimmte Teile zu nutzen und den Rest zu ignorieren, wodurch es nicht mehr erforderlich ist, für jeden ignorierten Wert ein Unterstrich anzugeben. Das `..`-Muster ignoriert alle Teile eines Werts, die wir in anderen Teilen des Musters nicht explizit abgleichen. In Listing 18-23 haben wir eine `Point`-Struktur, die eine Koordinate im dreidimensionalen Raum speichert. Im `match`-Ausdruck möchten wir nur auf die `x`-Koordinate operieren und die Werte in den `y`- und `z`-Feldern ignorieren.

Dateiname: `src/main.rs`

```rust
struct Point {
    x: i32,
    y: i32,
    z: i32,
}

let origin = Point { x: 0, y: 0, z: 0 };

match origin {
    Point { x,.. } => println!("x ist {x}"),
}
```

Listing 18-23: Ignorieren aller Felder einer `Point` außer `x` durch Verwendung von `..`

Wir listieren den `x`-Wert und verwenden dann einfach das `..`-Muster. Dies ist schneller als es wäre, `y: _` und `z: _` aufzuschreiben, insbesondere wenn wir mit Strukturen arbeiten, die viele Felder haben und nur ein oder zwei Felder relevant sind.

Die Syntax `..` wird so weit erweitert, wie es erforderlich ist. Listing 18-24 zeigt, wie man `..` mit einem Tupel verwendet.

Dateiname: `src/main.rs`

```rust
fn main() {
    let numbers = (2, 4, 8, 16, 32);

    match numbers {
        (first,.., last) => {
            println!("Einige Zahlen: {first}, {last}");
        }
    }
}
```

Listing 18-24: Nur die ersten und letzten Werte in einem Tupel abgleichen und alle anderen Werte ignorieren

In diesem Code werden die ersten und letzten Werte mit `first` und `last` abgleicht. Das `..` wird alle Werte dazwischen abgleichen und ignorieren.

Wir müssen jedoch beachten, dass die Verwendung von `..` eindeutig sein muss. Wenn unklar ist, welche Werte für die Zuordnung bestimmt sind und welche ignoriert werden sollen, wird Rust uns einen Fehler geben. Listing 18-25 zeigt ein Beispiel für eine zweideutige Verwendung von `..`, sodass der Code nicht kompilieren wird.

Dateiname: `src/main.rs`

```rust
fn main() {
    let numbers = (2, 4, 8, 16, 32);

    match numbers {
        (.., second,..) => {
            println!("Einige Zahlen: {second}");
        },
    }
}
```

Listing 18-25: Ein Versuch, `..` auf eine zweideutige Weise zu verwenden

Wenn wir diesen Code kompilieren, erhalten wir diesen Fehler:

```bash
error: `..` kann nur einmal pro Tupel-Muster verwendet werden
 --> src/main.rs:5:22
  |
5 |         (.., second,..) => {
  |          --          ^^ kann nur einmal pro Tupel-Muster verwendet werden
  |          |
  |          zuvor hier verwendet
```

Es ist für Rust nicht möglich, zu bestimmen, wie viele Werte im Tupel ignoriert werden sollen, bevor ein Wert mit `second` abgeglichen wird, und dann wie viele weitere Werte danach ignoriert werden sollen. Dieser Code könnte bedeuten, dass wir `2` ignorieren möchten, `second` an `4` binden und dann `8`, `16` und `32` ignorieren; oder dass wir `2` und `4` ignorieren möchten, `second` an `8` binden und dann `16` und `32` ignorieren; und so weiter. Der Variablennamen `second` hat für Rust keine besondere Bedeutung, daher erhalten wir einen Compilerfehler, da das Verwenden von `..` an zwei Stellen so zweideutig ist.
