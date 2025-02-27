# Integrationstestung

Unit-Tests testen jeweils ein Modul isoliert: Sie sind klein und können private Code testen. Integrationstests befinden sich außerhalb Ihres Crates und verwenden nur dessen öffentliche Schnittstelle, genauso wie jede andere Codebase. Ihr Zweck besteht darin, zu überprüfen, ob viele Teile Ihrer Bibliothek zusammen korrekt funktionieren.

Cargo sucht nach Integrationstests im Verzeichnis `tests` neben `src`.

Datei `src/lib.rs`:

```rust
// Definiere dies in einem Crate namens `adder`.
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}
```

Datei mit Test: `tests/integration_test.rs`:

```rust
#[test]
fn test_add() {
    assert_eq!(adder::add(3, 2), 5);
}
```

Ausführen von Tests mit dem Befehl `cargo test`:

```shell
$ cargo test
running 0 tests

test result: ok. 0 passed
0 failed
0 ignored
0 measured
0 filtered out

Running target/debug/deps/integration_test-bcd60824f5fbfe19

running 1 test
test test_add... ok

test result: ok. 1 passed
0 failed
0 ignored
0 measured
0 filtered out

Doc-tests adder

running 0 tests

test result: ok. 0 passed
0 failed
0 ignored
0 measured
0 filtered out
```

Jede Rust-Quelldatei im Verzeichnis `tests` wird als separates Crate kompiliert. Um Code zwischen Integrationstests zu teilen, können wir ein Modul mit öffentlichen Funktionen erstellen, es importieren und innerhalb der Tests verwenden.

Datei `tests/common/mod.rs`:

```rust
pub fn setup() {
    // Einige Setup-Code, wie das Erstellen von erforderlichen Dateien/Verzeichnissen, Starten
    // von Servern usw.
}
```

Datei mit Test: `tests/integration_test.rs`

```rust
// Importieren des gemeinsamen Moduls.
mod common;

#[test]
fn test_add() {
    // Verwenden des gemeinsamen Codes.
    common::setup();
    assert_eq!(adder::add(3, 2), 5);
}
```

Das Erstellen des Moduls als `tests/common.rs` funktioniert ebenfalls, wird jedoch nicht empfohlen, da der Testrunner die Datei als Test-Crate behandeln und versuchen wird, die darin enthaltenen Tests auszuführen.
