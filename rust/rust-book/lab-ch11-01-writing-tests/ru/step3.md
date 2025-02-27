# Проверка результатов с помощью макроса `assert!`

Макрос `assert!`, предоставляемый стандартной библиотекой, полезен, когда вы хотите убедиться, что какое - то условие в тесте оценивается как `true`. Мы передаем макросу `assert!` аргумент, который оценивается в булево значение. Если значение равно `true`, ничего не происходит и тест проходит. Если значение равно `false`, макрос `assert!` вызывает `panic!`, чтобы привести к неудаче тест. Использование макроса `assert!` помогает нам проверить, работает ли наш код так, как мы предполагаем.

В Листинге 5-15 мы использовали структуру `Rectangle` и метод `can_hold`, которые повторяются здесь в Листинге 11-5. Давайте поместим этот код в файл `src/lib.rs`, а затем напишем для него несколько тестов с использованием макроса `assert!`.

Имя файла: `src/lib.rs`

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}
```

Листинг 11-5: Использование структуры `Rectangle` и ее метода `can_hold` из главы 5

Метод `can_hold` возвращает булево значение, что означает, что это идеальный случай для использования макроса `assert!`. В Листинге 11-6 мы пишем тест, который проверяет метод `can_hold`, создав экземпляр структуры `Rectangle` с шириной 8 и высотой 7 и проверив, может ли он вместить другой экземпляр структуры `Rectangle` с шириной 5 и высотой 1.

Имя файла: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
  1 use super::*;

    #[test]
  2 fn larger_can_hold_smaller() {
      3 let larger = Rectangle {
            width: 8,
            height: 7,
        };
        let smaller = Rectangle {
            width: 5,
            height: 1,
        };

      4 assert!(larger.can_hold(&smaller));
    }
}
```

Листинг 11-6: Тест для `can_hold`, который проверяет, может ли большая прямоугольная область вместить меньшую

Обратите внимание, что мы добавили новую строку внутри модуля `tests`: `use super::*;` \[1\]. Модуль `tests` — это обычный модуль, который подчиняется обычным правилам видимости, о которых мы говорили в разделе "Пути для обращения к элементу в дереве модулей". Поскольку модуль `tests` является внутренним модулем, нам нужно подключить код, подлежащий тестированию, из внешнего модуля в область видимости внутреннего модуля. Мы используем глобальную ссылку здесь, поэтому все, что мы определяем в внешнем модуле, доступно для этого модуля `tests`.

Мы назвали наш тест `larger_can_hold_smaller` \[2\], и создали два экземпляра структуры `Rectangle`, которые нам нужны \[3\]. Затем мы вызвали макрос `assert!` и передали ему результат вызова `larger.can_hold(&smaller)` \[4\]. Эта выражение должно возвращать `true`, поэтому наш тест должен пройти. Проверим!

    running 1 test
    test tests::larger_can_hold_smaller... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

Тест действительно проходит! Добавим еще один тест, на этот раз проверив, что меньшая прямоугольная область не может вместить большую:

Имя файла: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn larger_can_hold_smaller() {
        --snip--
    }

    #[test]
    fn smaller_cannot_hold_larger() {
        let larger = Rectangle {
            width: 8,
            height: 7,
        };
        let smaller = Rectangle {
            width: 5,
            height: 1,
        };

        assert!(!smaller.can_hold(&larger));
    }
}
```

Поскольку правильный результат работы функции `can_hold` в этом случае — `false`, мы должны отрицать этот результат, прежде чем передать его в макрос `assert!`. Таким образом, наш тест пройдет, если `can_hold` возвращает `false`:

    running 2 tests
    test tests::larger_can_hold_smaller... ok
    test tests::smaller_cannot_hold_larger... ok

    test result: ok. 2 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

Два теста, которые проходят! Теперь посмотрим, что произойдет с нашими результатами тестов, если мы внедрим ошибку в наш код. Мы изменим реализацию метода `can_hold`, заменив знак больше на знак меньше при сравнении ширины:

    --snip--

    impl Rectangle {
        fn can_hold(&self, other: &Rectangle) -> bool {
            self.width < other.width && self.height > other.height
        }
    }

Запуск тестов теперь дает следующий результат:

    running 2 tests
    test tests::smaller_cannot_hold_larger... ok
    test tests::larger_can_hold_smaller... FAILED

    failures:

    ---- tests::larger_can_hold_smaller stdout ----
    thread 'main' panicked at 'assertion failed:
    larger.can_hold(&smaller)', src/lib.rs:28:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace


    failures:
        tests::larger_can_hold_smaller

    test result: FAILED. 1 passed; 1 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

Наши тесты обнаружили ошибку! Поскольку `larger.width` равно 8, а `smaller.width` равно 5, сравнение ширины в методе `can_hold` теперь возвращает `false`: 8 не меньше 5.
