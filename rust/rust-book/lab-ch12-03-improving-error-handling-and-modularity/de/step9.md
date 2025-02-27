# Calling Config::build and Handling Errors

Um den Fehlerfall zu behandeln und eine benutzerfreundliche Nachricht auszugeben, müssen wir `main` aktualisieren, um das `Result`, das von `Config::build` zurückgegeben wird, zu verarbeiten, wie in Listing 12-10 gezeigt. Wir übernehmen auch die Verantwortung, das Befehlszeilentool mit einem nichtnullen Fehlercode zu beenden, weg von `panic!` und implementieren es stattdessen von Hand. Ein nichtnuller Exit-Status ist eine Konvention, um dem aufrufenden Prozess mitzuteilen, dass das Programm mit einem Fehlerzustand beendet wurde.

Dateiname: `src/main.rs`

```rust
1 use std::process;

fn main() {
    let args: Vec<String> = env::args().collect();

  2 let config = Config::build(&args).3 unwrap_or_else(|4 err| {
      5 println!("Problem parsing arguments: {err}");
      6 process::exit(1);
    });

    --snip--
```

Listing 12-10: Exiting with an error code if building a `Config` fails

In dieser Liste haben wir eine Methode verwendet, die wir noch nicht im Detail behandelt haben: `unwrap_or_else`, die von der Standardbibliothek auf `Result<T, E>` definiert ist \[2\]. Mit `unwrap_or_else` können wir eine benutzerdefinierte, nicht-`panic!`-Fehlerbehandlung definieren. Wenn das `Result` ein `Ok`-Wert ist, verhält sich diese Methode ähnlich wie `unwrap`: Sie gibt den inneren Wert zurück, den `Ok` umschließt. Wenn der Wert jedoch ein `Err`-Wert ist, ruft diese Methode den Code in der _Closure_ auf, die eine anonyme Funktion ist, die wir definieren und als Argument an `unwrap_or_else` übergeben \[3\]. Wir werden Closures im nächsten Kapitel 13 im Detail behandeln. Für jetzt müssen Sie nur wissen, dass `unwrap_or_else` den inneren Wert von `Err`, der in diesem Fall der statische String `"not enough arguments"` ist, den wir in Listing 12-9 hinzugefügt haben, an unsere Closure im Argument `err` übergeben wird, das zwischen den vertikalen Schläuchen erscheint \[4\]. Der Code in der Closure kann dann den `err`-Wert verwenden, wenn er ausgeführt wird.

Wir haben eine neue `use`-Zeile hinzugefügt, um `process` aus der Standardbibliothek in den Gültigkeitsbereich zu bringen \[1\]. Der Code in der Closure, der im Fehlerfall ausgeführt wird, umfasst nur zwei Zeilen: wir drucken den `err`-Wert \[5\] und rufen dann `process::exit` auf \[6\]. Die `process::exit`-Funktion stoppt das Programm sofort und gibt die Zahl zurück, die als Exit-Statuscode übergeben wurde. Dies ähnelt der `panic!`-basierten Behandlung, die wir in Listing 12-8 verwendet haben, aber wir erhalten keine zusätzlichen Ausgaben mehr. Probieren wir es aus:

```bash
$ cargo run
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.48s
     Running `target/debug/minigrep`
Problem parsing arguments: not enough arguments
```

Super! Diese Ausgabe ist für unsere Benutzer viel freundlicher.
