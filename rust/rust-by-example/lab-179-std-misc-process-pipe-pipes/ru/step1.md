# Трубы

Структура `std::Child` представляет запущенный дочерний процесс и предоставляет дескрипторы `stdin`, `stdout` и `stderr` для взаимодействия с основным процессом через трубы.

```rust
use std::io::prelude::*;
use std::process::{Command, Stdio};

static PANGRAM: &'static str =
"the quick brown fox jumped over the lazy dog\n";

fn main() {
    // Запускаем команду `wc`
    let process = match Command::new("wc")
                              .stdin(Stdio::piped())
                              .stdout(Stdio::piped())
                              .spawn() {
        Err(why) => panic!("couldn't spawn wc: {}", why),
        Ok(process) => process,
    };

    // Записываем строку в `stdin` команды `wc`.
    //
    // `stdin` имеет тип `Option<ChildStdin>`, но поскольку мы знаем, что этот экземпляр
    // обязательно должен иметь его, мы можем напрямую использовать `unwrap`.
    match process.stdin.unwrap().write_all(PANGRAM.as_bytes()) {
        Err(why) => panic!("couldn't write to wc stdin: {}", why),
        Ok(_) => println!("sent pangram to wc"),
    }

    // Поскольку `stdin` не существует после вышеуказанных вызовов, он уничтожается (`drop`),
    // и труба закрывается.
    //
    // Это очень важно, иначе `wc` не начнет обрабатывать ввод, который мы только что отправили.

    // Поле `stdout` также имеет тип `Option<ChildStdout>`, поэтому его также нужно развернуть (`unwrap`).
    let mut s = String::new();
    match process.stdout.unwrap().read_to_string(&mut s) {
        Err(why) => panic!("couldn't read wc stdout: {}", why),
        Ok(_) => print!("wc responded with:\n{}", s),
    }
}
```
