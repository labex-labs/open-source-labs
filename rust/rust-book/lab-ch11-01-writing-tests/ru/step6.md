# Проверка на панику с помощью should_panic

Кроме проверки возвращаемых значений, важно проверить, обрабатывает ли наш код ошибочные ситуации, как мы ожидаем. Например, рассмотрим тип `Guess`, который мы создали в Листинге 9-13. Другие части кода, которые используют `Guess`, зависят от гарантии, что экземпляры `Guess` будут содержать только значения от 1 до 100. Мы можем написать тест, который гарантирует, что попытка создать экземпляр `Guess` с значением за пределами этого диапазона вызовет панику.

Мы это делаем, добавив атрибут `should_panic` к нашей тестовой функции. Тест пройдет, если код внутри функции вызывает панику; тест не пройдет, если код внутри функции не вызывает панику.

Листинг 11-8 показывает тест, который проверяет, что ошибочные ситуации `Guess::new` возникают, когда мы ожидаем их.

    // src/lib.rs
    pub struct Guess {
        value: i32,
    }

    impl Guess {
        pub fn new(value: i32) -> Guess {
            if value < 1 || value > 100 {
                panic!(
                    "Guess value must be between 1 and 100, got {}.",
                    value
                );
            }

            Guess { value }
        }
    }

    #[cfg(test)]
    mod tests {
        use super::*;

        #[test]
        #[should_panic]
        fn greater_than_100() {
            Guess::new(200);
        }
    }

Листинг 11-8: Тестирование того, что условие вызовет панику!

Мы помещаем атрибут `#[should_panic]` после атрибута `#[test]` и перед тестовой функцией, к которой он относится. Посмотрим на результат, когда этот тест пройдет:

    running 1 test
    test tests::greater_than_100 - should panic... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

Все хорошо! Теперь давайте внесем ошибку в наш код, удалив условие, при котором функция `new` будет вызывать панику, если значение больше 100:

    // src/lib.rs
    --snip--

    impl Guess {
        pub fn new(value: i32) -> Guess {
            if value < 1 {
                panic!(
                    "Guess value must be between 1 and 100, got {}.",
                    value
                );
            }

            Guess { value }
        }
    }

Когда мы запустим тест из Листинга 11-8, он не пройдет:

    running 1 test
    test tests::greater_than_100 - should panic... FAILED

    failures:

    ---- tests::greater_than_100 stdout ----
    note: test did not panic as expected

    failures:
        tests::greater_than_100

    test result: FAILED. 0 passed; 1 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

В этом случае мы не получаем очень полезного сообщения, но когда мы смотрим на тестовую функцию, мы видим, что она помечена атрибутом `#[should_panic]`. Неудача, которую мы получили, означает, что код в тестовой функции не вызвал панику.

Тесты, которые используют `should_panic`, могут быть неточными. Тест с `should_panic` пройдет даже если тест вызывает панику по другой причине, чем мы ожидали. Чтобы сделать тесты с `should_panic` более точными, мы можем добавить необязательный параметр `expected` к атрибуту `should_panic`. Тестовый механизм убедится, что сообщение об ошибке содержит указанный текст. Например, рассмотрим модифицированный код для `Guess` в Листинге 11-9, где функция `new` вызывает панику с разными сообщениями, в зависимости от того, является ли значение слишком малым или слишком большим.

    // src/lib.rs
    --snip--

    impl Guess {
        pub fn new(value: i32) -> Guess {
            if value < 1 {
                panic!(
                    "Guess value must be greater than or equal to 1, got {}.",
                    value
                );
            } else if value > 100 {
                panic!(
                    "Guess value must be less than or equal to 100, got {}.",
                    value
                );
            }

            Guess { value }
        }
    }

    #[cfg(test)]
    mod tests {
        use super::*;

        #[test]
        #[should_panic(expected = "less than or equal to 100")]
        fn greater_than_100() {
            Guess::new(200);
        }
    }

Листинг 11-9: Тестирование на панику с сообщением о панике, содержащим указанную подстроку

Этот тест пройдет, потому что значение, которое мы указали в параметре `expected` атрибута `should_panic`, является подстрокой сообщения, с которым функция `Guess::new` вызывает панику. Мы могли бы указать целое сообщение о панике, которое мы ожидаем, в этом случае оно было бы `Guess value must be less than or equal to 100, got 200`. То, что вы выбираете указывать, зависит от того, насколько уникально или динамично сообщение о панике и насколько точно вы хотите, чтобы был ваш тест. В этом случае подстрока сообщения о панике достаточно, чтобы убедиться, что код в тестовой функции выполняет блок `else if value > 100`.

Посмотрим, что произойдет, когда тест с `should_panic` и ожидаемым сообщением не пройдет. Давайте снова внесем ошибку в наш код, поменяв тела блоков `if value < 1` и `else if value > 100`:

    // src/lib.rs
    --snip--
    if value < 1 {
        panic!(
            "Guess value must be less than or equal to 100, got {}.",
            value
        );
    } else if value > 100 {
        panic!(
            "Guess value must be greater than or equal to 1, got {}.",
            value
        );
    }
    --snip--

На этот раз, когда мы запустим тест с `should_panic`, он не пройдет:

    running 1 test
    test tests::greater_than_100 - should panic... FAILED

    failures:

    ---- tests::greater_than_100 stdout ----
    thread 'main' panicked at 'Guess value must be greater than or equal to 1, got
    200.', src/lib.rs:13:13
    note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
    note: panic did not contain expected string
          panic message: `"Guess value must be greater than or equal to 1, got
    200."`,
     expected substring: `"less than or equal to 100"`

    failures:
        tests::greater_than_100

    test result: FAILED. 0 passed; 1 failed; 0 ignored; 0 measured; 0 filtered out;
    finished in 0.00s

Сообщение об ошибке показывает, что этот тест действительно вызвал панику, как мы ожидали, но сообщение о панике не содержало ожидаемой строки `'Guess value must be less than or equal to 100'`. Сообщение о панике, которое мы получили в этом случае, было `Guess value must be greater than or equal to 1, got 200`. Теперь мы можем начать определять, где находится наша ошибка!
