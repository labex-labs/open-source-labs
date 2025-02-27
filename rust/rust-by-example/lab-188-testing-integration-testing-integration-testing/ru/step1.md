# Интеграционное тестирование

Модульные тесты проверяют один модуль по отдельности: они небольшие и могут тестировать приватный код. Интеграционные тесты находятся вне вашей коробки и используют только ее публичный интерфейс так же, как и любой другой код. Их цель - проверить, правильно ли работают вместе многие части вашей библиотеки.

Cargo ищет интеграционные тесты в каталоге `tests`, расположенном рядом с `src`.

Файл `src/lib.rs`:

```rust
// Определите это в коробке под названием `adder`.
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}
```

Файл с тестом: `tests/integration_test.rs`:

```rust
#[test]
fn test_add() {
    assert_eq!(adder::add(3, 2), 5);
}
```

Запуск тестов с помощью команды `cargo test`:

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

Каждый файл исходного кода Rust в каталоге `tests` компилируется как отдельная коробка. Чтобы поделиться некоторым кодом между интеграционными тестами, мы можем создать модуль с публичными функциями, импортировать и использовать его в тестах.

Файл `tests/common/mod.rs`:

```rust
pub fn setup() {
    // Некоторый код настройки, например, создание необходимых файлов/каталогов, запуск
    // серверов и т.д.
}
```

Файл с тестом: `tests/integration_test.rs`

```rust
// Импортируем общий модуль.
mod common;

#[test]
fn test_add() {
    // Используем общий код.
    common::setup();
    assert_eq!(adder::add(3, 2), 5);
}
```

Создание модуля в виде `tests/common.rs` также работает, но не рекомендуется, потому что тестовый runner будет воспринимать файл как тестовую коробку и пытаться запустить тесты внутри него.
