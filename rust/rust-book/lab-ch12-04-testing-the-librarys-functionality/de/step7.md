# Verwenden der search-Funktion in der run-Funktion

Jetzt, da die `search`-Funktion funktioniert und getestet ist, müssen wir `search` aus unserer `run`-Funktion aufrufen. Wir müssen den Wert `config.query` und den `contents`, den `run` aus der Datei liest, an die `search`-Funktion übergeben. Dann wird `run` jede Zeile aus `search` ausgeben:

Dateiname: `src/lib.rs`

```rust
pub fn run(config: Config) -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string(config.file_path)?;

    for line in search(&config.query, &contents) {
        println!("{line}");
    }

    Ok(())
}
```

Wir verwenden immer noch eine `for`-Schleife, um jede Zeile aus `search` zurückzugeben und auszugeben.

Jetzt sollte das gesamte Programm funktionieren! Probieren wir es aus, zunächst mit einem Wort, das genau eine Zeile aus dem Gedicht von Emily Dickinson zurückgeben sollte: _frosch_.

```bash
$ cargo run -- frosch gedicht.txt
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.38s
     Running `target/debug/minigrep frosch gedicht.txt`
Wie öffentlich, wie ein Frosch
```

Cool! Jetzt probieren wir ein Wort, das mehrere Zeilen übereinstimmen wird, wie _Körper_:

```bash
$ cargo run -- Körper gedicht.txt
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep Körper gedicht.txt`
Ich bin Niemand! Wer bist du?
Bist du auch Niemand?
Wie langweilig, jemand zu sein!
```

Und schließlich stellen wir sicher, dass wir keine Zeilen erhalten, wenn wir nach einem Wort suchen, das nicht irgendwo im Gedicht vorkommt, wie _Monomorphisierung_:

```bash
$ cargo run -- Monomorphisierung gedicht.txt
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep Monomorphisierung gedicht.txt`
```

Toller! Wir haben eine eigene Mini-Version eines klassischen Tools gebaut und viel über die Struktur von Anwendungen gelernt. Wir haben auch ein bisschen über Dateieingabe und -ausgabe, Lebenszeiten, Testen und Kommandozeilenanalyse gelernt.

Um dieses Projekt abzurunden, werden wir kurz demonstrieren, wie man mit Umgebungsvariablen umgeht und wie man auf die Standardfehlerausgabe schreibt, was beide nützlich sind, wenn man Kommandozeilenprogramme schreibt.
