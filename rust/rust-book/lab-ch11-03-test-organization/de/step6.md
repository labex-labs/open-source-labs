# Das tests-Verzeichnis

Wir erstellen ein Verzeichnis `tests` auf der obersten Ebene unseres Projektverzeichnisses, neben `src`. Cargo weiß, in diesem Verzeichnis nach Integrations-Testdateien zu suchen. Wir können dann so viele Testdateien wie wir möchten erstellen, und Cargo wird jede Datei als eigenständigen Kasten kompilieren.

Lassen Sie uns einen Integrations-Test erstellen. Mit dem Code in Listing 11-12 noch in der Datei `src/lib.rs`, erstellen Sie ein Verzeichnis `tests` und eine neue Datei namens `tests/integration_test.rs`. Ihre Verzeichnisstruktur sollte so aussehen:

    adder
    ├── Cargo.lock
    ├── Cargo.toml
    ├── src
    │   └── lib.rs
    └── tests
        └── integration_test.rs

Geben Sie den Code in Listing 11-13 in die Datei `tests/integration_test.rs` ein.

Dateiname: `tests/integration_test.rs`

```rust
use adder;

#[test]
fn it_adds_two() {
    assert_eq!(4, adder::add_two(2));
}
```

Listing 11-13: Ein Integrations-Test einer Funktion im `adder`-Kasten

Jede Datei im `tests`-Verzeichnis ist ein separater Kasten, daher müssen wir unsere Bibliothek in den Geltungsbereich jedes Testkastens bringen. Aus diesem Grund fügen wir `use adder;` am Anfang des Codes hinzu, was wir in den Einheitstests nicht benötigten.

Wir müssen keinen Code in `tests/integration_test.rs` mit `#[cfg(test)]` annotieren. Cargo behandelt das `tests`-Verzeichnis speziell und kompiliert Dateien in diesem Verzeichnis nur, wenn wir `cargo test` ausführen. Führen Sie jetzt `cargo test` aus:

```bash

```

Die drei Abschnitte der Ausgabe umfassen die Einheitstests, den Integrations-Test und die Dokutests. Beachten Sie, dass, wenn ein Test in einem Abschnitt fehlschlägt, die folgenden Abschnitte nicht ausgeführt werden. Beispielsweise wird, wenn ein Einheitstest fehlschlägt, keine Ausgabe für Integrations- und Dokutests erscheinen, da diese Tests nur ausgeführt werden, wenn alle Einheitstests bestanden werden.

Der erste Abschnitt für die Einheitstests \[1\] ist der gleiche wie bisher: Eine Zeile für jeden Einheitstest (einer benannt `internal`, den wir in Listing 11-12 hinzugefügt haben) und dann eine Zusammenfassungszeile für die Einheitstests.

Der Abschnitt mit den Integrations-Tests beginnt mit der Zeile `Running tests/integration_test.rs` \[2\]. Danach gibt es eine Zeile für jede Testfunktion in diesem Integrations-Test \[3\] und eine Zusammenfassungszeile für die Ergebnisse des Integrations-Tests \[4\] direkt vor dem Abschnitt `Doc-tests adder` beginnt.

Jede Integrations-Testdatei hat ihren eigenen Abschnitt, daher wird, wenn wir weitere Dateien im `tests`-Verzeichnis hinzufügen, es auch mehr Abschnitte mit Integrations-Tests geben.

Wir können immer noch einen bestimmten Integrations-Testfunktion ausführen, indem wir den Namen der Testfunktion als Argument für `cargo test` angeben. Um alle Tests in einer bestimmten Integrations-Testdatei auszuführen, verwenden Sie das `--test`-Argument von `cargo test` gefolgt vom Dateinamen:

```bash

```

Dieser Befehl führt nur die Tests in der Datei `tests/integration_test.rs` aus.
