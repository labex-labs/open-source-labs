# Funktionen

Funktionen sind in Rust-Code weit verbreitet. Du hast bereits eine der wichtigsten Funktionen in der Sprache gesehen: die `main`-Funktion, die der Einstiegspunkt vieler Programme ist. Du hast auch das `fn`-Schlüsselwort gesehen, das dir erlaubt, neue Funktionen zu deklarieren.

Erstelle ein neues Projekt namens `functions`:

```bash
cargo new functions
cd functions
```

Rust-Code verwendet _snake case_ als die übliche Schreibweise für Funktions- und Variablennamen, bei der alle Buchstaben klein geschrieben sind und Unterstriche Wörter trennen. Hier ist ein Programm, das eine Beispiel-Funktionsdefinition enthält:

Dateiname: `src/main.rs`

```rust
fn main() {
    println!("Hello, world!");

    another_function();
}

fn another_function() {
    println!("Another function.");
}
```

Wir definieren eine Funktion in Rust, indem wir `fn` eingeben, gefolgt vom Funktionsnamen und einer Klammerung. Die geschweiften Klammern sagen dem Compiler, wo der Funktionskörper beginnt und endet.

Wir können jede Funktion, die wir definiert haben, aufrufen, indem wir ihren Namen gefolgt von einer Klammerung eingeben. Da `another_function` im Programm definiert ist, kann sie aus der `main`-Funktion heraus aufgerufen werden. Beachte, dass wir `another_function` _nach_ der `main`-Funktion im Quellcode definiert haben; wir hätten es auch vorher definieren können. Rust kümmert sich nicht darum, wo du deine Funktionen definierst, nur darum, dass sie irgendwo in einem Gültigkeitsbereich definiert sind, den der Aufrufer sehen kann.

Lass uns ein neues binäres Projekt namens _functions_ starten, um Funktionen weiter zu erkunden. Plaziere das `another_function`-Beispiel in `src/main.rs` und führe es aus. Du solltest die folgende Ausgabe sehen:

```bash
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
    Finished dev [unoptimized + debuginfo] target(s) in 0.28s
     Running `target/debug/functions`
Hello, world!
Another function.
```

Die Zeilen werden in der Reihenfolge ausgeführt, in der sie in der `main`-Funktion erscheinen. Zuerst wird die "Hello, world!"-Nachricht ausgegeben, und dann wird `another_function` aufgerufen und ihre Nachricht ausgegeben.
