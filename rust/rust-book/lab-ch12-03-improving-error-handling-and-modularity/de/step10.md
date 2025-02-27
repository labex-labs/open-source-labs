# Extracting Logic from main

Jetzt, nachdem wir die Umgestaltung der Konfigurationsanalyse abgeschlossen haben, kehren wir zur Logik des Programms zurück. Wie wir in "Separation of Concerns for Binary Projects" erwähnt haben, extrahieren wir eine Funktion namens `run`, die alle Logik enthalten wird, die derzeit in der `main`-Funktion ist und die nicht mit der Einrichtung der Konfiguration oder der Fehlerbehandlung zusammenhängt. Wenn wir fertig sind, wird `main` prägnant und leicht durch Überprüfung zu verifizieren, und wir können Tests für alle anderen Logiken schreiben.

Listing 12-11 zeigt die extrahierte `run`-Funktion. Momentan machen wir nur die kleine, sukzessive Verbesserung, die Funktion zu extrahieren. Wir definieren die Funktion immer noch in `src/main.rs`.

Dateiname: `src/main.rs`

```rust
fn main() {
    --snip--

    println!("Searching for {}", config.query);
    println!("In file {}", config.file_path);

    run(config);
}

fn run(config: Config) {
    let contents = fs::read_to_string(config.file_path)
     .expect("Should have been able to read the file");

    println!("With text:\n{contents}");
}

--snip--
```

Listing 12-11: Extracting a `run` function containing the rest of the program logic

Die `run`-Funktion enthält jetzt alle verbleibende Logik aus `main`, beginnend mit dem Lesen der Datei. Die `run`-Funktion nimmt die `Config`-Instanz als Argument entgegen.
