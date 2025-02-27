# Untermodule in Integrations-Tests

Wenn Sie mehr Integrations-Tests hinzufügen, möchten Sie möglicherweise mehr Dateien im `tests`-Verzeichnis erstellen, um sie zu organisieren; beispielsweise können Sie die Testfunktionen nach der Funktionalität gruppieren, die sie testen. Wie bereits erwähnt, wird jede Datei im `tests`-Verzeichnis als eigener separater Kasten kompiliert, was hilfreich ist, um separate Geltungsbereiche zu erstellen, um die Art und Weise zu näher imitieren, wie Endbenutzer Ihre Bibliothek verwenden werden. Dies bedeutet jedoch, dass Dateien im `tests`-Verzeichnis nicht das gleiche Verhalten wie Dateien in `src` haben, wie Sie im Kapitel 7 gelernt haben, wie man Code in Module und Dateien aufteilt.

Das unterschiedliche Verhalten von Dateien im `tests`-Verzeichnis ist am auffälligsten, wenn Sie eine Reihe von Hilfsfunktionen haben, die in mehreren Integrations-Testdateien verwendet werden sollen, und Sie versuchen, die Schritte in "Trennen von Modulen in verschiedene Dateien" zu folgen, um sie in ein gemeinsames Modul zu extrahieren. Beispielsweise, wenn wir `tests/common.rs` erstellen und eine Funktion namens `setup` darin platzieren, können wir einigen Code in `setup` hinzufügen, den wir von mehreren Testfunktionen in mehreren Testdateien aufrufen möchten:

Dateiname: `tests/common.rs`

```rust
pub fn setup() {
    // setup code specific to your library's tests would go here
}
```

Wenn wir die Tests erneut ausführen, sehen wir einen neuen Abschnitt in der Testausgabe für die Datei `common.rs`, obwohl diese Datei keine Testfunktionen enthält und wir die `setup`-Funktion auch von keinem anderen Ort aus aufgerufen haben:

    running 1 test
    test tests::internal... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

         Running tests/common.rs (target/debug/deps/common-
    92948b65e88960b4)

    running 0 tests

    test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

         Running tests/integration_test.rs
    (target/debug/deps/integration_test-92948b65e88960b4)

    running 1 test
    test it_adds_two... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

       Doc-tests adder

    running 0 tests

    test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

Dass `common` in den Testresultaten erscheint, mit `running 0 tests` für es angezeigt, ist nicht das, was wir wollten. Wir wollten nur etwas Code mit den anderen Integrations-Testdateien teilen. Um zu vermeiden, dass `common` in der Testausgabe erscheint, erstellen wir statt `tests/common.rs` `tests/common/mod.rs` anstelle. Das Projektverzeichnis sieht jetzt so aus:

    ├── Cargo.lock
    ├── Cargo.toml
    ├── src
    │   └── lib.rs
    └── tests
        ├── common
        │   └── mod.rs
        └── integration_test.rs

Dies ist die ältere Namenskonvention, die Rust ebenfalls versteht, die wir in "Alternative Dateipfade" erwähnt haben. Wenn wir die Datei so benennen, sagt Rust, die `common`-Modul nicht als Integrations-Testdatei zu behandeln. Wenn wir den Code der `setup`-Funktion in `tests/common/mod.rs` verschieben und die Datei `tests/common.rs` löschen, wird der Abschnitt in der Testausgabe nicht mehr erscheinen. Dateien in Unterverzeichnissen des `tests`-Verzeichnisses werden nicht als separate Kisten kompiliert oder haben Abschnitte in der Testausgabe.

Nachdem wir `tests/common/mod.rs` erstellt haben, können wir es von jeder der Integrations-Testdateien als Modul verwenden. Hier ist ein Beispiel, wie die `setup`-Funktion aus dem Test `it_adds_two` in `tests/integration_test.rs` aufgerufen wird:

Dateiname: `tests/integration_test.rs`

```rust
use adder;

mod common;

#[test]
fn it_adds_two() {
    common::setup();
    assert_eq!(4, adder::add_two(2));
}
```

Beachte, dass die Deklaration `mod common;` die gleiche wie die Moduldeklaration ist, die wir in Listing 7-21 demonstriert haben. Dann können wir in der Testfunktion die Funktion `common::setup()` aufrufen.
