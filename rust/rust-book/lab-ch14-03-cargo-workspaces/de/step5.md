# Ein Test in einen Arbeitsbereich hinzufügen

Als weitere Verbesserung fügen wir einen Test der `add_one::add_one`-Funktion innerhalb des `add_one`-Kratens hinzu:

Dateiname: `add_one/src/lib.rs`

```rust
pub fn add_one(x: i32) -> i32 {
    x + 1
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        assert_eq!(3, add_one(2));
    }
}
```

Führen Sie jetzt `cargo test` im obersten Ebene `add`-Verzeichnis aus. Wenn Sie `cargo test` in einem Arbeitsbereich wie diesem ausführen, werden die Tests für alle Kraten im Arbeitsbereich ausgeführt:

```bash
[object Object]
```

Der erste Abschnitt der Ausgabe zeigt, dass der `it_works`-Test im `add_one`-Kraten bestanden hat. Der nächste Abschnitt zeigt, dass in dem `adder`-Kraten keine Tests gefunden wurden, und der letzte Abschnitt zeigt, dass in dem `add_one`-Kraten keine Dokumentationstests gefunden wurden.

Wir können auch die Tests für einen bestimmten Kraten in einem Arbeitsbereich aus dem obersten Ebene Verzeichnis ausführen, indem wir das `-p`-Flag verwenden und den Namen des Kratens angeben, für den wir die Tests ausführen möchten:

```bash
[object Object]
```

Diese Ausgabe zeigt, dass `cargo test` nur die Tests für den `add_one`-Kraten ausgeführt hat und die `adder`-Kraten-Tests nicht ausgeführt hat.

Wenn Sie die Kraten im Arbeitsbereich auf *https://crates.io* veröffentlichen, müssen Sie jedes Kraten im Arbeitsbereich separat veröffentlichen. Wie `cargo test` können wir ein bestimmtes Kraten in unserem Arbeitsbereich veröffentlichen, indem wir das `-p`-Flag verwenden und den Namen des Kratens angeben, das wir veröffentlichen möchten.

Für zusätzliche Übung fügen Sie einen `add_two`-Kraten zu diesem Arbeitsbereich auf eine ähnliche Weise wie den `add_one`-Kraten hinzu!

Wenn sich Ihr Projekt erweitert, sollten Sie einen Arbeitsbereich in Betracht ziehen: Er bietet einfachere zu verstehende, kleinere, individuelle Komponenten als ein großer Codeblock. Darüber hinaus kann das Zusammenhalten der Kraten in einem Arbeitsbereich die Koordination zwischen den Kraten erleichtern, wenn sie oft gleichzeitig geändert werden.
