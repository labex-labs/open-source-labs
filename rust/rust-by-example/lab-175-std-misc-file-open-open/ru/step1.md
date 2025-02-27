# `open`

Функция `open` может быть использована для открытия файла в режиме только для чтения.

Объект `File` владеет ресурсом, дескриптором файла, и заботится о закрытии файла, когда он выходит из области видимости (`drop`).

```rust
use std::fs::File;
use std::io::prelude::*;
use std::path::Path;

fn main() {
    // Создаём путь к нужному файлу
    let path = Path::new("hello.txt");
    let display = path.display();

    // Открываем путь в режиме только для чтения, возвращает `io::Result<File>`
    let mut file = match File::open(&path) {
        Err(why) => panic!("не удалось открыть {}: {}", display, why),
        Ok(file) => file,
    };

    // Считываем содержимое файла в строку, возвращает `io::Result<usize>`
    let mut s = String::new();
    match file.read_to_string(&mut s) {
        Err(why) => panic!("не удалось прочитать {}: {}", display, why),
        Ok(_) => print!("{} содержит:\n{}", display, s),
    }

    // Объект `file` выходит из области видимости, и файл "hello.txt" закрывается
}
```

Вот ожидаемый успешный вывод:

```shell
$ echo "Hello World!" > hello.txt
$ rustc open.rs && ./open
hello.txt содержит:
Hello World!
```

(Рекомендуется протестировать предыдущий пример при различных условиях ошибок: файл `hello.txt` не существует, или файл `hello.txt` не доступен для чтения и т.д.)
