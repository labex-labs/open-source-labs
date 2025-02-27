# Модульное тестирование

Тесты — это функции Rust, которые проверяют, работает ли код, не являющийся тестом, в ожидаемом режиме. Тело тестовых функций обычно выполняет некоторые настройки, запускает код, который мы хотим протестировать, а затем утверждает, соответствуют ли результаты нашим ожиданиям.

Большинство модульных тестов помещаются в модуль `tests` с атрибутом `#[cfg(test)]`. Тестовые функции помечаются атрибутом `#[test]`.

Тесты завершаются с ошибкой, если в тестовой функции произойдёт паника. Есть некоторые вспомогательные макросы:

- `assert!(expression)` — вызывает панику, если выражение оценивается как `false`.
- `assert_eq!(left, right)` и `assert_ne!(left, right)` — проверяют равенство и неравенство соответственно между выражениями `left` и `right`.

```rust
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

// Это действительно плохая функция сложения, её цель — завершиться с ошибкой в этом
// примере.
#[allow(dead_code)]
fn bad_add(a: i32, b: i32) -> i32 {
    a - b
}

#[cfg(test)]
mod tests {
    // Обратите внимание на этот полезный идиом: импорт имен из внешней (для модульных тестов) области.
    use super::*;

    #[test]
    fn test_add() {
        assert_eq!(add(1, 2), 3);
    }

    #[test]
    fn test_bad_add() {
        // Эта проверка вызовет ошибку, и тест завершится с ошибкой.
        // Обратите внимание, что приватные функции также можно протестировать!
        assert_eq!(bad_add(1, 2), 3);
    }
}
```

Тесты можно запускать с помощью `cargo test`.

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

## Тесты и `?`

Ни один из предыдущих примеров модульных тестов не имел возвращаемого типа. Но в Rust 2018 модульные тесты могут возвращать `Result<()>`, что позволяет использовать оператор `?` в них! Это может сделать их гораздо компактнее.

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

Подробнее см. в "Руководстве по редакциям".

## Тестирование паник

Для проверки функций, которые должны завершаться с паникой при определённых обстоятельствах, используйте атрибут `#[should_panic]`. Этот атрибут принимает необязательный параметр `expected =` с текстом сообщения о панике. Если ваша функция может завершиться с паникой несколькими способами, это помогает убедиться, что ваш тест проверяет правильную панику.

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

Запуск этих тестов даёт следующие результаты:

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

## Запуск конкретных тестов

Для запуска конкретных тестов можно указать имя теста в команде `cargo test`.

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

Для запуска нескольких тестов можно указать часть имени теста, которая соответствует всем тестам, которые должны быть запущены.

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

## Игнорирование тестов

Тесты можно пометить атрибутом `#[ignore]`, чтобы исключить некоторые тесты. Или запустить их с помощью команды `cargo test -- --ignored`

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
