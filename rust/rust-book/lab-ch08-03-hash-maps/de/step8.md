# Aktualisieren eines Werts basierend auf dem alten Wert

Ein weiterer häufiger Anwendungsfall für Hash-Tabellen (Hash Maps) besteht darin, den Wert eines Schlüssels zu suchen und ihn dann basierend auf dem alten Wert zu aktualisieren. Beispielsweise zeigt Listing 8-25 Code, der zählt, wie oft jedes Wort in einem Text vorkommt. Wir verwenden eine Hash-Tabelle mit den Wörtern als Schlüsseln und erhöhen den Wert, um zu verfolgen, wie oft wir ein Wort gesehen haben. Wenn es das erste Mal ist, dass wir ein Wort sehen, fügen wir zunächst den Wert `0` ein.

```rust
use std::collections::HashMap;

let text = "hello world wonderful world";

let mut map = HashMap::new();

for word in text.split_whitespace() {
    let count = map.entry(word).or_insert(0);
    *count += 1;
}

println!("{:?}", map);
```

Listing 8-25: Zählen der Vorkommen von Wörtern mit einer Hash-Tabelle, die Wörter und Zählungen speichert

Dieser Code wird `{"world": 2, "hello": 1, "wonderful": 1}` ausgeben. Möglicherweise werden die gleichen Schlüssel-Wert-Paare in einer anderen Reihenfolge ausgegeben: Denken Sie an "Accessing Values in a Hash Map" (Zugreifen auf Werte in einer Hash-Tabelle), dass das Iterieren über eine Hash-Tabelle in beliebiger Reihenfolge erfolgt.

Die `split_whitespace`-Methode gibt einen Iterator über Teilschnitte zurück, die durch Leerzeichen getrennt sind, des Werts in `text`. Die `or_insert`-Methode gibt eine veränderliche Referenz (`&mut V`) auf den Wert für den angegebenen Schlüssel zurück. Hier speichern wir diese veränderliche Referenz in der Variablen `count`, daher müssen wir, um diesem Wert zuzuweisen, zunächst `count` mit dem Sternchen (`*`) dereferenzieren. Die veränderliche Referenz verlässt den Gültigkeitsbereich am Ende der `for`-Schleife, sodass alle diese Änderungen sicher sind und von den Borrowing-Regeln erlaubt werden.
