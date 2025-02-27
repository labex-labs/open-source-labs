# Extracting the Argument Parser

Wir extrahieren die Funktionalität zum Analysieren von Argumenten in eine Funktion, die `main` aufrufen wird, um die Vorbereitung für das Verschieben der Befehlszeilenanalyse-Logik in `src/lib.rs*` zu erleichtern. Listing 12-5 zeigt den neuen Anfang von `main`, der eine neue Funktion `parse_config` aufruft, die wir momentan in `src/main.rs*` definieren werden.

Dateiname: `src/main.rs`

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

    let (query, file_path) = parse_config(&args);

    --snip--
}

fn parse_config(args: &[String]) -> (&str, &str) {
    let query = &args[1];
    let file_path = &args[2];

    (query, file_path)
}
```

Listing 12-5: Extracting a `parse_config` function from `main`

Wir sammeln immer noch die Befehlszeilenargumente in einem Vektor, aber anstatt die Argumentwerte an Index 1 der Variable `query` und die Argumentwerte an Index 2 der Variable `file_path` innerhalb der `main`-Funktion zuzuweisen, übergeben wir den gesamten Vektor an die `parse_config`-Funktion. Die `parse_config`-Funktion enthält dann die Logik, die bestimmt, welches Argument in welche Variable gehört, und gibt die Werte zurück an `main`. Wir erstellen die `query`- und `file_path`-Variablen immer noch in `main`, aber `main` hat keine Verantwortung mehr für die Bestimmung, wie die Befehlszeilenargumente und die Variablen korrespondieren.

Dieser Umbau mag für unser kleines Programm übertrieben erscheinen, aber wir refaktorisieren in kleinen, sukzessiven Schritten. Nachdem Sie diese Änderung vorgenommen haben, führen Sie das Programm erneut aus, um zu überprüfen, ob die Argumentanalyse weiterhin funktioniert. Es ist gut, Ihre Fortschritte häufig zu überprüfen, um die Ursache von Problemen zu identifizieren, wenn sie auftreten.
