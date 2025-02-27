# Suchen in jeder Zeile nach der Abfrage

Als nächstes überprüfen wir, ob die aktuelle Zeile unseren Suchstring enthält. Glücklicherweise hat die `String`-Klasse eine hilfreiche Methode namens `contains`, die genau das für uns erledigt! Fügen Sie einen Aufruf der `contains`-Methode in die `search`-Funktion hinzu, wie in Listing 12-18 gezeigt. Beachten Sie, dass dies immer noch nicht kompilieren wird.

Dateiname: `src/lib.rs`

```rust
pub fn search<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    for line in contents.lines() {
        if line.contains(query) {
            // do something with line
        }
    }
}
```

Listing 12-18: Hinzufügen der Funktionalität, um zu überprüfen, ob die Zeile den String in `query` enthält

Im Moment bauen wir die Funktionalität auf. Um den Code zu kompilieren, müssen wir einen Wert aus dem Funktionsrumpf zurückgeben, wie wir es in der Funktionssignatur angegeben haben.
