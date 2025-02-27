# Codeverständlichkeit durch Iteratoradapter

Wir können auch Iteratoren im `search`-Funktion unseres I/O-Projekts nutzen, die hier in Listing 13-21 wiedergegeben ist, wie sie in Listing 12-19 war.

Dateiname: `src/lib.rs`

```rust
pub fn search<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    let mut results = Vec::new();

    for line in contents.lines() {
        if line.contains(query) {
            results.push(line);
        }
    }

    results
}
```

Listing 13-21: Die Implementierung der `search`-Funktion aus Listing 12-19

Wir können diesen Code auf eine kürzere Weise mit Iteratoradaptermethoden schreiben. Dadurch vermeiden wir auch, einen mutablen Zwischenvektor `results` zu haben. Der funktionale Programmierungstil bevorzugt es, den Umfang des mutablen Zustands zu minimieren, um den Code klarer zu machen. Das Entfernen des mutablen Zustands könnte eine zukünftige Verbesserung ermöglichen, um die Suche parallel durchzuführen, da wir nicht mehr die konkurrierende Zugriffe auf den `results`-Vektor verwalten müssten. Listing 13-22 zeigt diese Änderung.

Dateiname: `src/lib.rs`

```rust
pub fn search<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    contents
     .lines()
     .filter(|line| line.contains(query))
     .collect()
}
```

Listing 13-22: Verwendung von Iteratoradaptermethoden in der Implementierung der `search`-Funktion

Denken Sie daran, dass der Zweck der `search`-Funktion darin besteht, alle Zeilen in `contents` zurückzugeben, die den `query` enthalten. Ähnlich wie das `filter`-Beispiel in Listing 13-16 verwendet dieser Code den `filter`-Adapter, um nur die Zeilen zu behalten, für die `line.contains(query)` `true` zurückgibt. Wir sammeln dann die übereinstimmenden Zeilen in einem anderen Vektor mit `collect`. Viel einfacher! Fühlen Sie sich frei, die gleiche Änderung auch in der `search_case_insensitive`-Funktion zu machen, um Iteratormethoden zu verwenden.
