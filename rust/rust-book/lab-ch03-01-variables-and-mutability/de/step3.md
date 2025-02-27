# Shadowing

Wie Sie im Tippspiel-Tutorial im zweiten Kapitel gesehen haben, können Sie eine neue Variable mit dem gleichen Namen wie eine vorherige Variable deklarieren. Rust-Entwickler sagen, dass die erste Variable von der zweiten _verdeckt_ wird, was bedeutet, dass die zweite Variable das ist, was der Compiler sieht, wenn Sie den Variablennamen verwenden. In der Tat überdeckt die zweite Variable die erste, indem sie alle Verwendung des Variablennamens auf sich zieht, bis entweder sie selbst verdeckt wird oder der Gültigkeitsbereich endet. Wir können eine Variable verbergen, indem wir denselben Variablennamen verwenden und die Verwendung des `let`-Schlüsselworts wiederholen, wie folgt:

Dateiname: `src/main.rs`

```rust
fn main() {
    let x = 5;

    let x = x + 1;

    {
        let x = x * 2;
        println!("The value of x in the inner scope is: {x}");
    }

    println!("The value of x is: {x}");
}
```

Dieses Programm bindet zunächst `x` an einen Wert von `5`. Anschließend erstellt es eine neue Variable `x`, indem es `let x =` wiederholt, nimmt den ursprünglichen Wert und addiert `1`, sodass der Wert von `x` dann `6` ist. Anschließend, innerhalb eines inneren Gültigkeitsbereichs, der mit geschweiften Klammern erstellt wird, deklariert der dritte `let`-Befehl ebenfalls `x` und erstellt eine neue Variable, indem er den vorherigen Wert mit `2` multipliziert, um `x` einen Wert von `12` zu geben. Wenn dieser Gültigkeitsbereich vorbei ist, endet das innere Verbergen und `x` kehrt wieder auf `6` zurück. Wenn wir dieses Programm ausführen, wird es folgendes ausgeben:

```bash
$ cargo run
   Compiling variables v0.1.0 (file:///projects/variables)
    Finished dev [unoptimized + debuginfo] target(s) in 0.31s
     Running `target/debug/variables`
The value of x in the inner scope is: 12
The value of x is: 6
```

Das Verbergen unterscheidet sich von der Markierung einer Variable als `mut`, weil wir einen Compile-Zeitfehler erhalten, wenn wir versehentlich versuchen, dieser Variable erneut zuzuweisen, ohne das `let`-Schlüsselwort zu verwenden. Indem wir `let` verwenden, können wir einige Transformationen an einem Wert vornehmen, aber die Variable bleibt unveränderlich, nachdem diese Transformationen abgeschlossen sind.

Der andere Unterschied zwischen `mut` und Verbergen besteht darin, dass wir effektiv eine neue Variable erstellen, wenn wir das `let`-Schlüsselwort erneut verwenden, sodass wir den Typ des Werts ändern können, aber den gleichen Namen wiederverwenden können. Beispielsweise sagen wir, dass unser Programm einen Benutzer auffordert, anzugeben, wie viele Leerzeichen sie zwischen einigen Texten möchten, indem sie Leerzeichen eingeben, und wir möchten diese Eingabe als Zahl speichern:

```rust
let spaces = "   ";
let spaces = spaces.len();
```

Die erste `spaces`-Variable ist vom String-Typ und die zweite `spaces`-Variable ist vom Zahlentyp. Das Verbergen erspart uns daher die Notwendigkeit, verschiedene Namen wie `spaces_str` und `spaces_num` zu erfinden; anstatt dessen können wir den einfachereren Namen `spaces` wiederverwenden. Wenn wir jedoch versuchen, `mut` für dies zu verwenden, wie hier gezeigt, erhalten wir einen Compile-Zeitfehler:

```rust
let mut spaces = "   ";
spaces = spaces.len();
```

Der Fehler besagt, dass wir nicht zulassen, den Typ einer Variable zu mutieren:

```bash
$ cargo run
   Compiling variables v0.1.0 (file:///projects/variables)
error[E0308]: mismatched types
 --> src/main.rs:3:14
  |
2 |     let mut spaces = "   ";
  |                      ----- expected due to this value
3 |     spaces = spaces.len();
  |              ^^^^^^^^^^^^ expected `&str`, found `usize`
```

Jetzt, nachdem wir untersucht haben, wie Variablen funktionieren, schauen wir uns an, welche weiteren Datentypen sie haben können.
