# Anzeige der Funktionsausgabe

Standardmäßig fängt die Testbibliothek von Rust alles auf der Standardausgabe ausgegebene an, wenn ein Test erfolgreich ist. Beispielsweise, wenn wir `println!` in einem Test aufrufen und der Test erfolgreich ist, werden wir die `println!`-Ausgabe nicht im Terminal sehen; wir sehen nur die Zeile, die angibt, dass der Test bestanden hat. Wenn ein Test fehlschlägt, werden wir alles sehen, was auf die Standardausgabe ausgegeben wurde, zusammen mit der restlichen Fehlermeldung.

Als Beispiel hat Listing 11-10 eine alberne Funktion, die den Wert ihres Parameters ausgibt und 10 zurückgibt, sowie einen Test, der bestanden und einen Test, der fehlschlägt.

Dateiname: `src/lib.rs`

```rust
fn prints_and_returns_10(a: i32) -> i32 {
    println!("I got the value {a}");
    10
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn this_test_will_pass() {
        let value = prints_and_returns_10(4);
        assert_eq!(10, value);
    }

    #[test]
    fn this_test_will_fail() {
        let value = prints_and_returns_10(8);
        assert_eq!(5, value);
    }
}
```

Listing 11-10: Tests für eine Funktion, die `println!` aufruft

Wenn wir diese Tests mit `cargo test` ausführen, sehen wir die folgende Ausgabe:

    running 2 tests
    test tests::this_test_will_pass... ok
    test tests::this_test_will_fail... FAILED

    failures:

    ---- tests::this_test_will_fail stdout ----
    1 I got the value 8
    thread 'main' panicked at 'assertion failed: `(left == right)`
      left: `5`,
     right: `10`', src/lib.rs:19:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace

    failures:
        tests::this_test_will_fail

    test result: FAILED. 1 passed; 1 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

Beachten Sie, dass wir nirgends in dieser Ausgabe `I got the value 4` sehen, das ausgegeben wird, wenn der erfolgreich verlaufende Test ausgeführt wird. Diese Ausgabe wurde erfasst. Die Ausgabe des fehlgeschlagenen Tests, `I got the value 8` \[1\], erscheint im Abschnitt der Testzusammenfassungsausgabe, die auch die Ursache des Testfehlschlags zeigt.

Wenn wir auch die ausgegebenen Werte für erfolgreich verlaufende Tests sehen möchten, können wir Rust sagen, die Ausgabe erfolgreicher Tests ebenfalls anzuzeigen, mit `--show-output`:

```bash
cargo test -- --show-output
```

Wenn wir die Tests in Listing 11-10 erneut mit dem `--show-output`-Flag ausführen, sehen wir die folgende Ausgabe:

    running 2 tests
    test tests::this_test_will_pass... ok
    test tests::this_test_will_fail... FAILED

    successes:

    ---- tests::this_test_will_pass stdout ----
    I got the value 4


    successes:
        tests::this_test_will_pass

    failures:

    ---- tests::this_test_will_fail stdout ----
    I got the value 8
    thread 'main' panicked at 'assertion failed: `(left == right)`
      left: `5`,
     right: `10`', src/lib.rs:19:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace

    failures:
        tests::this_test_will_fail

    test result: FAILED. 1 passed; 1 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s
