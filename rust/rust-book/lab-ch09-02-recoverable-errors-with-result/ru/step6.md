# A Shortcut for Propagating Errors: The? Operator

Листинг 9-7 показывает реализацию `read_username_from_file`, которая имеет ту же функциональность, что и в листинге 9-6, но эта реализация использует оператор `?`.

Filename: `src/main.rs`

```rust
use std::fs::File;
use std::io::{self, Read};

fn read_username_from_file() -> Result<String, io::Error> {
    let mut username_file = File::open("hello.txt")?;
    let mut username = String::new();
    username_file.read_to_string(&mut username)?;
    Ok(username)
}
```

Листинг 9-7: Функция, которая возвращает ошибки вызывающему коду с использованием оператора `?`

Оператор `?`, поставленный после значения `Result`, определен для работы почти так же, как выражения `match`, которые мы определили для обработки значений `Result` в листинге 9-6. Если значение `Result` является `Ok`, значение внутри `Ok` будет возвращено из этого выражения, и программа продолжит работу. Если значение является `Err`, `Err` будет возвращено из всей функции, точно так же, как если бы мы использовали ключевое слово `return`, так что значение ошибки передается вызывающему коду.

Есть разница между тем, что делает выражение `match` из листинга 9-6, и то, что делает оператор `?`: значения ошибки, для которых вызывается оператор `?`, проходят через функцию `from`, определенную в трейте `From` в стандартной библиотеке, которая используется для преобразования значений из одного типа в другой. Когда оператор `?` вызывает функцию `from`, тип ошибки, полученный, преобразуется в тип ошибки, определенный в возвращаемом типе текущей функции. Это полезно, когда функция возвращает один тип ошибки, чтобы представить все способы, которыми функция может завершиться с ошибкой, даже если некоторые части могут завершиться с ошибкой по разным причинам.

Например, мы могли изменить функцию `read_username_from_file` в листинге 9-7, чтобы она возвращала пользовательский тип ошибки под названием `OurError`, который мы определяем. Если мы также определим `impl From<io::Error> for OurError` для создания экземпляра `OurError` из `io::Error`, то вызовы оператора `?` в теле `read_username_from_file` вызовут `from` и преобразуют типы ошибок, не требуя добавления дополнительного кода в функцию.

В контексте листинга 9-7, `?` в конце вызова `File::open` вернет значение внутри `Ok` в переменную `username_file`. Если возникает ошибка, оператор `?` выйдет из всей функции досрочно и передаст любое значение `Err` вызывающему коду. То же самое относится к `?` в конце вызова `read_to_string`.

Оператор `?` устраняет много шаблонного кода и делает реализацию этой функции проще. Мы даже могли бы сократить этот код еще больше, объединив вызовы методов сразу после `?`, как показано в листинге 9-8.

Filename: `src/main.rs`

```rust
use std::fs::File;
use std::io::{self, Read};

fn read_username_from_file() -> Result<String, io::Error> {
    let mut username = String::new();

    File::open("hello.txt")?.read_to_string(&mut username)?;

    Ok(username)
}
```

Листинг 9-8: Объединение вызовов методов после оператора `?`

Мы перенесли создание новой `String` в `username` в начало функции; эта часть не изменилась. Вместо создания переменной `username_file` мы объединили вызов `read_to_string` непосредственно с результатом `File::open("hello.txt")?`. У нас по-прежнему есть `?` в конце вызова `read_to_string`, и мы по-прежнему возвращаем значение `Ok`, содержащее `username`, когда и `File::open`, и `read_to_string` завершаются успешно, вместо возврата ошибок. Функциональность снова та же, что и в листингах 9-6 и 9-7; это просто другой, более удобный способ написания.

Листинг 9-9 показывает способ сделать это еще короче, используя `fs::read_to_string`.

Filename: `src/main.rs`

```rust
use std::fs;
use std::io;

fn read_username_from_file() -> Result<String, io::Error> {
    fs::read_to_string("hello.txt")
}
```

Листинг 9-9: Использование `fs::read_to_string` вместо открытия и чтения файла

Чтение файла в строку - это довольно распространенная операция, поэтому стандартная библиотека предоставляет удобную функцию `fs::read_to_string`, которая открывает файл, создает новую `String`, читает содержимое файла, помещает содержимое в эту `String` и возвращает ее. Конечно, использование `fs::read_to_string` не дает нам возможность объяснить все обработку ошибок, поэтому мы сначала сделали это длинным способом.
