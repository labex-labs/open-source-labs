# Ausgeben von Fehlern an die Standardfehlerausgabe

Wir werden den Code in Listing 12-24 verwenden, um zu ändern, wie Fehlermeldungen ausgegeben werden. Aufgrund der Umstrukturierung, die wir zu Beginn dieses Kapitels durchgeführt haben, befindet sich all der Code, der Fehlermeldungen ausgibt, in einer Funktion, `main`. Die Standardbibliothek bietet das `eprintln!`-Makro an, das an den Standardfehlerstream ausgibt. Lassen Sie uns daher die beiden Stellen, an denen wir `println!` aufgerufen haben, um Fehler auszugeben, ändern, um `eprintln!` zu verwenden.

Dateiname: `src/main.rs`

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

    let config = Config::build(&args).unwrap_or_else(|err| {
        eprintln!("Problem parsing arguments: {err}");
        process::exit(1);
    });

    if let Err(e) = minigrep::run(config) {
        eprintln!("Application error: {e}");
        process::exit(1);
    }
}
```

Listing 12-24: Schreiben von Fehlermeldungen an die Standardfehlerausgabe statt an die Standardausgabe mit `eprintln!`

Lassen Sie uns nun das Programm erneut auf die gleiche Weise ausführen, ohne jegliche Argumente und mit der Umleitung der Standardausgabe mit `>`:

```bash
$ cargo run > output.txt
Problem parsing arguments: not enough arguments
```

Jetzt sehen wir den Fehler auf dem Bildschirm, und _output.txt_ enthält nichts, was das Verhalten ist, das wir von Befehlszeilenprogrammen erwarten.

Lassen Sie uns das Programm erneut mit Argumenten ausführen, die keinen Fehler verursachen, aber immer noch die Standardausgabe in eine Datei umleiten, wie folgt:

```bash
cargo run -- to poem.txt > output.txt
```

Wir werden keine Ausgabe auf dem Terminal sehen, und _output.txt_ wird unsere Ergebnisse enthalten:

Dateiname: output.txt

```rust
Are you nobody, too?
How dreary to be somebody!
```

Dies demonstriert, dass wir jetzt die Standardausgabe für erfolgreiche Ausgabe und die Standardfehlerausgabe für Fehlermeldungen entsprechend verwenden.
