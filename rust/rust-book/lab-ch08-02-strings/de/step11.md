# Methoden zum Iterieren über Strings

Der beste Weg, um mit Teilen von Strings zu arbeiten, ist es, klar zu machen, ob Sie Zeichen oder Bytes möchten. Für einzelne Unicode-Skalarwerte verwenden Sie die `chars`-Methode. Wenn Sie `chars` auf "Зд" aufrufen, werden die beiden Werte vom Typ `char` getrennt und zurückgegeben, und Sie können über das Ergebnis iterieren, um jedes Element zuzugreifen:

    for c in "Зд".chars() {
        println!("{c}");
    }

Dieser Code wird Folgendes ausgeben:

```rust
З
д
```

Alternativ gibt die `bytes`-Methode jedes ursprüngliche Byte zurück, was für Ihren Anwendungsbereich geeignet sein könnte:

    for b in "Зд".bytes() {
        println!("{b}");
    }

Dieser Code wird die vier Bytes ausgeben, die diesen String bilden:

    208
    151
    208
    180

Denken Sie jedoch daran, dass gültige Unicode-Skalarwerte aus mehr als einem Byte bestehen können.

Das Extrahieren von Grapheme-Clustern aus Strings, wie bei der Devanagari-Schrift, ist komplex, daher wird diese Funktionalität von der Standardbibliothek nicht bereitgestellt. Wenn Sie diese Funktionalität benötigen, finden Sie Crates unter *https://crates.io*.
