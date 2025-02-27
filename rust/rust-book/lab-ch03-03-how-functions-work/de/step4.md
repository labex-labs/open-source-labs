# Funktionen mit Rückgabewerten

Funktionen können Werte an den Code zurückgeben, der sie aufruft. Wir benennen die Rückgabewerte nicht, aber wir müssen ihren Typ nach einem Pfeil (`->`) deklarieren. In Rust ist der Rückgabewert einer Funktion synonym mit dem Wert des letzten Ausdrucks im Block des Funktionskörpers. Du kannst frühzeitig aus einer Funktion zurückkehren, indem du das `return`-Schlüsselwort verwendest und einen Wert angibst, aber die meisten Funktionen geben den letzten Ausdruck implizit zurück. Hier ist ein Beispiel einer Funktion, die einen Wert zurückgibt:

Dateiname: `src/main.rs`

```rust
fn five() -> i32 {
    5
}

fn main() {
    let x = five();

    println!("The value of x is: {x}");
}
```

In der `five`-Funktion gibt es keine Funktionsaufrufe, Makros oder sogar `let`-Anweisungen - nur die Zahl `5` selbst. Das ist in Rust eine vollkommen gültige Funktion. Beachte, dass der Rückgabetyp der Funktion ebenfalls angegeben wird, als `-> i32`. Versuche, diesen Code auszuführen; die Ausgabe sollte so aussehen:

```bash
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
    Finished dev [unoptimized + debuginfo] target(s) in 0.30s
     Running `target/debug/functions`
The value of x is: 5
```

Die `5` in `five` ist der Rückgabewert der Funktion, weshalb der Rückgabetyp `i32` ist. Betrachten wir dies im Detail. Es gibt zwei wichtige Punkte: Erstens zeigt die Zeile `let x = five();`, dass wir den Rückgabewert einer Funktion verwenden, um eine Variable zu initialisieren. Da die Funktion `five` einen `5` zurückgibt, ist diese Zeile gleich der folgenden:

```rust
let x = 5;
```

Zweitens hat die `five`-Funktion keine Parameter und definiert den Typ des Rückgabewerts, aber der Funktionskörper ist eine einsame `5` ohne Semikolon, weil es ein Ausdruck ist, dessen Wert wir zurückgeben möchten.

Schauen wir uns ein weiteres Beispiel an:

Dateiname: `src/main.rs`

```rust
fn main() {
    let x = plus_one(5);

    println!("The value of x is: {x}");
}

fn plus_one(x: i32) -> i32 {
    x + 1
}
```

Wenn du diesen Code ausführst, wird `The value of x is: 6` gedruckt. Aber wenn wir ein Semikolon am Ende der Zeile, die `x + 1` enthält, platzieren und sie dadurch von einem Ausdruck zu einer Anweisung umwandeln, erhalten wir einen Fehler:

Dateiname: `src/main.rs`

```rust
fn main() {
    let x = plus_one(5);

    println!("The value of x is: {x}");
}

fn plus_one(x: i32) -> i32 {
    x + 1;
}
```

Das Kompilieren dieses Codes führt zu einem Fehler, wie folgt:

```bash
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
error[E0308]: mismatched types
 --> src/main.rs:7:24
  |
7 | fn plus_one(x: i32) -> i32 {
  |    --------            ^^^ expected `i32`, found `()`
  |    |
  |    implicitly returns `()` as its body has no tail or `return` expression
8 |     x + 1;
  |          - help: remove this semicolon
```

Die Hauptfehlermeldung, `mismatched types` (ungleiche Typen), offenbart das Kernproblem dieses Codes. Die Definition der Funktion `plus_one` sagt, dass sie einen `i32` zurückgeben wird, aber Anweisungen evaluieren nicht zu einem Wert, was durch `()` (die Einheitstyp) ausgedrückt wird. Daher wird nichts zurückgegeben, was der Funktionsdefinition widerspricht und zu einem Fehler führt. In dieser Ausgabe gibt Rust eine Nachricht, die möglicherweise helfen soll, dieses Problem zu beheben: Es schlägt vor, das Semikolon zu entfernen, was den Fehler beheben würde.
