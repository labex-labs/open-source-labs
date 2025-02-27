# Показ вывода функции

По умолчанию, если тест проходит, тестовая библиотека Rust захватывает все, что выводится в стандартный вывод. Например, если мы вызываем `println!` в тесте и тест проходит, мы не увидим вывод `println!` в терминале; мы увидим только строку, которая показывает, что тест прошел. Если тест завершается с ошибкой, мы увидим все, что было выведено в стандартный вывод, вместе с остальной информацией об ошибке.

В качестве примера, в Листинге 11-10 есть простая функция, которая выводит значение своего параметра и возвращает 10, а также тест, который проходит, и тест, который завершается с ошибкой.

Имя файла: `src/lib.rs`

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

Листинг 11-10: Тесты для функции, которая вызывает `println!`

Когда мы запускаем эти тесты с помощью `cargo test`, мы увидим следующий вывод:

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

Заметим, что нигде в этом выводе мы не видим `I got the value 4`, которое выводится, когда проходит тест. Этот вывод был захвачен. Вывод из теста, который завершается с ошибкой, `I got the value 8` \[1\], появляется в разделе вывода сводки по тестам, который также показывает причину неудачи теста.

Если мы хотим также увидеть выведенные значения для проходящих тестов, мы можем попросить Rust также показать вывод успешных тестов с помощью флага `--show-output`:

```bash
cargo test -- --show-output
```

Когда мы снова запускаем тесты из Листинга 11-10 с флагом `--show-output`, мы видим следующий вывод:

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
