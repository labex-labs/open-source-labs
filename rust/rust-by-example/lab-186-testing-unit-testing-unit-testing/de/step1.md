# Unit-Tests

Tests sind Rust-Funktionen, die überprüfen, ob der nicht-testende Code wie erwartet funktioniert. Die Körper von Testfunktionen führen normalerweise einige Einstellungen durch, führen den Code aus, den wir testen möchten, und stellen dann sicher, dass die Ergebnisse den Erwartungen entsprechen.

Die meisten Unit-Tests befinden sich in einem `tests`-Modul mit dem Attribut `#[cfg(test)]`. Testfunktionen werden mit dem Attribut `#[test]` markiert.

Tests scheitern, wenn etwas in der Testfunktion einen Panik-Auslöser auslöst. Es gibt einige Hilfsmakros:

- `assert!(expression)` - löst eine Panik aus, wenn der Ausdruck `false` auswertet.
- `assert_eq!(left, right)` und `assert_ne!(left, right)` - testen die linke und rechte Ausdrücke auf Gleichheit und Ungleichheit respective.

```rust
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

// Dies ist eine wirklich schlechte Additionsfunktion, deren Zweck es ist, in diesem
// Beispiel fehlzuschlagen.
#[allow(dead_code)]
fn bad_add(a: i32, b: i32) -> i32 {
    a - b
}

#[cfg(test)]
mod tests {
    // Beachten Sie diese nützliche Idiomatik: Importieren von Namen aus dem äußeren (für Mod-Tests) Bereich.
    use super::*;

    #[test]
    fn test_add() {
        assert_eq!(add(1, 2), 3);
    }

    #[test]
    fn test_bad_add() {
        // Dieser Assert würde auslösen und der Test würde fehlschlagen.
        // Beachten Sie, dass private Funktionen ebenfalls getestet werden können!
        assert_eq!(bad_add(1, 2), 3);
    }
}
```

Tests können mit `cargo test` ausgeführt werden.

```shell
$ cargo test

running 2 tests
test tests::test_bad_add... FAILED
test tests::test_add... ok

failures:

---- tests::test_bad_add stdout ----
thread 'tests::test_bad_add' panicked at 'assertion failed: `(left == right)`
  left: `-1`,
 right: `3`', src/lib.rs:21:8
note: Run with $(RUST_BACKTRACE=1) for a backtrace.

failures:
tests::test_bad_add

test result: FAILED. 1 passed
1 failed
0 ignored
0 measured
0 filtered out
```

## Tests und `?`

Keines der vorherigen Unit-Testbeispiele hatte einen Rückgabetyp. Aber in Rust 2018 können Ihre Unit-Tests `Result<()>` zurückgeben, was es Ihnen ermöglicht, `?` darin zu verwenden! Dies kann sie viel präziser gestalten.

```rust
fn sqrt(number: f64) -> Result<f64, String> {
    if number >= 0.0 {
        Ok(number.powf(0.5))
    } else {
        Err("negative floats don't have square roots".to_owned())
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_sqrt() -> Result<(), String> {
        let x = 4.0;
        assert_eq!(sqrt(x)?.powf(2.0), x);
        Ok(())
    }
}
```

Weitere Details finden Sie in der "Edition Guide".

## Testen von Paniken

Um Funktionen zu überprüfen, die unter bestimmten Umständen einen Panik-Auslöser auslösen sollten, verwenden Sie das Attribut `#[should_panic]`. Dieses Attribut akzeptiert einen optionalen Parameter `expected =` mit dem Text der Panik-Nachricht. Wenn Ihre Funktion auf verschiedene Weise einen Panik-Auslöser auslösen kann, hilft dies sicherzustellen, dass Ihr Test den richtigen Panik-Auslöser testet.

```rust
pub fn divide_non_zero_result(a: u32, b: u32) -> u32 {
    if b == 0 {
        panic!("Divide-by-zero error");
    } else if a < b {
        panic!("Divide result is zero");
    }
    a / b
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_divide() {
        assert_eq!(divide_non_zero_result(10, 2), 5);
    }

    #[test]
    #[should_panic]
    fn test_any_panic() {
        divide_non_zero_result(1, 0);
    }

    #[test]
    #[should_panic(expected = "Divide result is zero")]
    fn test_specific_panic() {
        divide_non_zero_result(1, 10);
    }
}
```

Das Ausführen dieser Tests liefert uns Folgendes:

```shell
$ cargo test

running 3 tests
test tests::test_any_panic... ok
test tests::test_divide... ok
test tests::test_specific_panic... ok

test result: ok. 3 passed
0 failed
0 ignored
0 measured
0 filtered out

Doc-tests tmp-test-should-panic

running 0 tests

test result: ok. 0 passed
0 failed
0 ignored
0 measured
0 filtered out
```

## Ausführen von spezifischen Tests

Um spezifische Tests auszuführen, kann man den Testnamen an den `cargo test`-Befehl angeben.

```shell
$ cargo test test_any_panic
running 1 test
test tests::test_any_panic... ok

test result: ok. 1 passed
0 failed
0 ignored
0 measured
2 filtered out

Doc-tests tmp-test-should-panic

running 0 tests

test result: ok. 0 passed
0 failed
0 ignored
0 measured
0 filtered out
```

Um mehrere Tests auszuführen, kann man einen Teil des Testnamens angeben, der mit allen Tests übereinstimmt, die ausgeführt werden sollen.

```shell
$ cargo test panic
running 2 tests
test tests::test_any_panic... ok
test tests::test_specific_panic... ok

test result: ok. 2 passed
0 failed
0 ignored
0 measured
1 filtered out

Doc-tests tmp-test-should-panic

running 0 tests

test result: ok. 0 passed
0 failed
0 ignored
0 measured
0 filtered out
```

## Tests ignorieren

Tests können mit dem Attribut `#[ignore]` markiert werden, um einige Tests auszuschließen. Oder um sie mit dem Befehl `cargo test -- --ignored` auszuführen

```rust
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_add() {
        assert_eq!(add(2, 2), 4);
    }

    #[test]
    fn test_add_hundred() {
        assert_eq!(add(100, 2), 102);
        assert_eq!(add(2, 100), 102);
    }

    #[test]
    #[ignore]
    fn ignored_test() {
        assert_eq!(add(0, 0), 0);
    }
}
```

```shell
$ cargo test
running 3 tests
test tests::ignored_test... ignored
test tests::test_add... ok
test tests::test_add_hundred... ok

test result: ok. 2 passed
0 failed
1 ignored
0 measured
0 filtered out

Doc-tests tmp-ignore

running 0 tests

test result: ok. 0 passed
0 failed
0 ignored
0 measured
0 filtered out

$ cargo test -- --ignored
running 1 test
test tests::ignored_test... ok

test result: ok. 1 passed
0 failed
0 ignored
0 measured
0 filtered out

Doc-tests tmp-ignore

running 0 tests

test result: ok. 0 passed
0 failed
0 ignored
0 measured
0 filtered out
```
