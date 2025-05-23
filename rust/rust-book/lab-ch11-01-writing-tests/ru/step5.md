# Добавление пользовательских сообщений об ошибке

Вы также можете добавить пользовательское сообщение, которое будет выводиться вместе с сообщением об ошибке, в качестве необязательных аргументов для макросов `assert!`, `assert_eq!` и `assert_ne!`. Любые аргументы, указанные после обязательных аргументов, передаются в макрос `format!` (обсуждается в разделе "Конкатенация с помощью оператора + или макроса format!"), поэтому вы можете передать строку форматирования, которая содержит плейсхолдеры `{}` и значения, которые будут подставляться в эти плейсхолдеры. Пользовательские сообщения полезны для документирования того, что означает утверждение; когда тест не проходит, вы будете лучше понимать, в чем проблема с кодом.

Например, предположим, у нас есть функция, которая приветствует людей по имени, и мы хотим проверить, что имя, которое мы передаем в функцию, появляется в выводе:

Имя файла: `src/lib.rs`

```rust
pub fn greeting(name: &str) -> String {
    format!("Hello {name}!")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn greeting_contains_name() {
        let result = greeting("Carol");
        assert!(result.contains("Carol"));
    }
}
```

Требования для этой программы еще не были согласованы, и мы довольно уверены, что текст `Hello` в начале приветствия изменится. Мы решили, что не хотим обновлять тест, когда требования меняются, поэтому вместо проверки точного равенства значению, возвращаемому функцией `greeting`, мы просто проверим, что вывод содержит текст входного параметра.

Теперь давайте внесем ошибку в этот код, изменив `greeting`, чтобы он не включал `name`, чтобы увидеть, как выглядит стандартное сообщение об ошибке при тестировании:

```rust
pub fn greeting(name: &str) -> String {
    String::from("Hello!")
}
```

Запуск этого теста дает следующий результат:

    running 1 test
    test tests::greeting_contains_name... FAILED

    failures:

    ---- tests::greeting_contains_name stdout ----
    thread 'main' panicked at 'assertion failed:
    result.contains(\"Carol\")', src/lib.rs:12:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace


    failures:
        tests::greeting_contains_name

Этот результат только показывает, что утверждение не прошло и на какой строке находится утверждение. Более полезное сообщение об ошибке выведет значение из функции `greeting`. Добавим пользовательское сообщение об ошибке, составленное из строки форматирования с заполненным плейсхолдером фактическим значением, которое мы получили из функции `greeting`:

    #[test]
    fn greeting_contains_name() {
        let result = greeting("Carol");
        assert!(
            result.contains("Carol"),
            "Greeting did not contain name, value was `{result}`"
        );
    }

Теперь, когда мы запускаем тест, мы получим более информативное сообщение об ошибке:

    ---- tests::greeting_contains_name stdout ----
    thread 'main' panicked at 'Greeting did not contain name, value
    was `Hello!`', src/lib.rs:12:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace

Мы можем увидеть значение, которое мы фактически получили в выводе теста, что поможет нам отладить, что произошло, вместо того, что мы ожидали.
