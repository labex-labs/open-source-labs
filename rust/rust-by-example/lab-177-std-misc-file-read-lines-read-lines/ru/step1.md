# `read_lines`

## Наивный подход

Это может быть разумная первая попытка для начинающего программиста при первом реализации чтения строк из файла.

```rust
use std::fs::read_to_string;

fn read_lines(filename: &str) -> Vec<String> {
    let mut result = Vec::new();

    for line in read_to_string(filename).unwrap().lines() {
        result.push(line.to_string())
    }

    result
}
```

Поскольку метод `lines()` возвращает итератор по строкам в файле, мы также можем выполнить `map` inline и собрать результаты, получая более краткое и выразительное выражение.

```rust
use std::fs::read_to_string;

fn read_lines(filename: &str) -> Vec<String> {
    read_to_string(filename)
     .unwrap()  // panic при возможных ошибках чтения файла
     .lines()  // разделить строку на итератор строковых срезов
     .map(String::from)  // превратить каждый срез в строку
     .collect()  // собрать их в вектор
}
```

Обратите внимание, что в обоих примерах выше мы должны преобразовать `&str` ссылку, возвращаемую из `lines()`, в собственный тип `String`, используя `.to_string()` и `String::from` соответственно.

## Более эффективный подход

Здесь мы передаем владение открытым `File` в структуру `BufReader`. `BufReader` использует внутренний буфер для уменьшения промежуточных выделений памяти.

Мы также обновляем `read_lines` для возврата итератора вместо выделения новых объектов `String` в памяти для каждой строки.

```rust
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    // Файл hosts.txt должен существовать в текущем каталоге
    if let Ok(lines) = read_lines("./hosts.txt") {
        // Консумирует итератор, возвращает (Optional) String
        for line in lines {
            if let Ok(ip) = line {
                println!("{}", ip);
            }
        }
    }
}

// Результат обернут в Result для обработки ошибок
// Возвращает итератор для Reader строк файла.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
```

Запуск этой программы просто выводит строки по отдельности.

```shell
$ echo -e "127.0.0.1\n192.168.0.1\n" > hosts.txt
$ rustc read_lines.rs && ./read_lines
127.0.0.1
192.168.0.1
```

(Обратите внимание, что поскольку `File::open` ожидает обобщенный `AsRef<Path>` в качестве аргумента, мы определяем наш обобщенный метод `read_lines()` с тем же обобщенным ограничением, используя ключевое слово `where`.)

Этот процесс более эффективен, чем создание `String` в памяти с содержимым всего файла. Это особенно может вызывать проблемы с производительностью при работе с большими файлами.
