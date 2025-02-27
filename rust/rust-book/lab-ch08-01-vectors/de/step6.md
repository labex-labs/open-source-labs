# Verwenden eines Enums, um mehrere Typen zu speichern

Vektoren können nur Werte vom gleichen Typ speichern. Dies kann unbequem sein; es gibt definitiv Anwendungsfälle, in denen man eine Liste von Elementen unterschiedlicher Typen speichern muss. Glücklicherweise werden die Varianten eines Enums unter dem gleichen Enum-Typ definiert, sodass wir, wenn wir einen Typ benötigen, um Elemente unterschiedlicher Typen zu repräsentieren, ein Enum definieren und verwenden können!

Nehmen wir beispielsweise an, dass wir Werte aus einer Zeile in einer Tabellenkalkulation abrufen möchten, in der einige Spalten der Zeile ganze Zahlen, einige Gleitkommazahlen und einige Zeichenketten enthalten. Wir können ein Enum definieren, dessen Varianten die verschiedenen Werttypen aufnehmen werden, und alle Enum-Varianten werden als derselbe Typ betrachtet: der des Enums. Dann können wir einen Vektor erstellen, um dieses Enum zu speichern und somit letztendlich verschiedene Typen zu speichern. Wir haben dies in Listing 8-9 demonstriert.

```rust
enum SpreadsheetCell {
    Int(i32),
    Float(f64),
    Text(String),
}

let row = vec![
    SpreadsheetCell::Int(3),
    SpreadsheetCell::Text(String::from("blue")),
    SpreadsheetCell::Float(10.12),
];
```

Listing 8-9: Definieren eines `Enum`s, um Werte unterschiedlicher Typen in einem Vektor zu speichern

Rust muss zur Compile-Zeit wissen, welche Typen im Vektor sein werden, damit es genau weiß, wie viel Speicher auf dem Heap für jedes Element benötigt wird. Wir müssen auch explizit darüber informieren, welche Typen in diesem Vektor erlaubt sind. Wenn Rust einem Vektor erlaubte, beliebige Typen zu speichern, gäbe es die Möglichkeit, dass ein oder mehrere Typen Fehler bei den auf die Elemente des Vektors ausgeführten Operationen verursachen würden. Das Verwenden eines Enums plus eines `match`-Ausdrucks bedeutet, dass Rust zur Compile-Zeit gewährleistet, dass jeder mögliche Fall behandelt wird, wie im Kapitel 6 besprochen.

Wenn Sie die erschöpfende Menge an Typen nicht kennen, die ein Programm zur Laufzeit erhalten wird, um sie in einem Vektor zu speichern, wird die Enum-Technik nicht funktionieren. Stattdessen können Sie ein Trait-Objekt verwenden, das wir im Kapitel 17 behandeln werden.

Jetzt, nachdem wir einige der häufigsten Möglichkeiten, Vektoren zu verwenden, diskutiert haben, sollten Sie sich die API-Dokumentation für alle der vielen nützlichen Methoden ansehen, die auf `Vec<T>` von der Standardbibliothek definiert sind. Beispielsweise entfernt die `pop`-Methode neben `push` das letzte Element und gibt es zurück.
