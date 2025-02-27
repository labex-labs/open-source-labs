# Shortcuts for Panic on Error: unwrap and expect

Использование `match` работает достаточно хорошо, но может быть немного избыточным и не всегда хорошо передавать намерение. Тип `Result<T, E>` имеет множество вспомогательных методов, определенных для него, чтобы выполнять различные более специфические задачи. Метод `unwrap` - это краткий метод, реализованный так же, как выражение `match`, которое мы написали в листинге 9-4. Если значение `Result` является вариантом `Ok`, `unwrap` вернет значение внутри `Ok`. Если `Result` является вариантом `Err`, `unwrap` вызовет для нас макрос `panic!`. Вот пример использования `unwrap`:

Filename: `src/main.rs`

```rust
use std::fs::File;

fn main() {
    let greeting_file = File::open("hello.txt").unwrap();
}
```

Если мы запустим этот код без файла _hello.txt_, мы увидим сообщение об ошибке от вызова `panic!`, который делает метод `unwrap`:

    thread 'main' panicked at 'called `Result::unwrap()` on an `Err` value: Os {
    code: 2, kind: NotFound, message: "No such file or directory" }',
    src/main.rs:4:49

Аналогично, метод `expect` позволяет нам также выбрать сообщение об ошибке `panic!`. Использование `expect` вместо `unwrap` и предоставление хороших сообщений об ошибках может передать ваше намерение и сделать поиск источника паники проще. Синтаксис `expect` выглядит так:

Filename: `src/main.rs`

```rust
use std::fs::File;

fn main() {
    let greeting_file = File::open("hello.txt")
     .expect("hello.txt should be included in this project");
}
```

Мы используем `expect` так же, как и `unwrap`: чтобы вернуть дескриптор файла или вызвать макрос `panic!`. Сообщение об ошибке, используемое `expect` при вызове `panic!`, будет параметром, который мы передаем в `expect`, а не стандартным сообщением `panic!`, которое использует `unwrap`. Вот, как это выглядит:

    thread 'main' panicked at 'hello.txt should be included in this project: Os {
    code: 2, kind: NotFound, message: "No such file or directory" }',
    src/main.rs:5:10

В коде промышленного качества большинство Rustaceans выбирают `expect` вместо `unwrap` и дают больше контекста о том, почему операция должна всегда успешно завершаться. Таким образом, если ваши предположения окажутся неверными, у вас будет больше информации для отладки.
