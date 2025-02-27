# Чтение файла

Теперь мы добавим функциональность для чтения файла, указанного в аргументе `file_path`. Во - первых, нам нужен пример файла для тестирования: мы будем использовать файл с небольшим количеством текста на нескольких строках с некоторыми повторяющимися словами. В Listing 12-3 представлен стихотворение Эмили Диккенсон, которое подойдет отлично! Создайте файл с именем _poem.txt_ в корневой директории вашего проекта и введите стихотворение "I'm Nobody! Who are you?".

Имя файла: poem.txt

    I'm nobody! Who are you?
    Are you nobody, too?
    Then there's a pair of us - don't tell!
    They'd banish us, you know.

    How dreary to be somebody!
    How public, like a frog
    To tell your name the livelong day
    To an admiring bog!

Listing 12-3: Стихотворение Эмили Диккенсон делает хороший тестовый случай.

После того, как текст就位, отредактируйте `src/main.rs` и добавьте код для чтения файла, как показано в Listing 12-4.

Имя файла: `src/main.rs`

```rust
use std::env;
1 use std::fs;

fn main() {
    --snip--
    println!("In file {}", file_path);

  2 let contents = fs::read_to_string(file_path)
       .expect("Should have been able to read the file");

  3 println!("With text:\n{contents}");
}
```

Listing 12-4: Чтение содержимого файла, указанного вторым аргументом

Во - первых, мы подключаем соответствующую часть стандартной библиотеки с помощью инструкции `use`: нам нужно `std::fs` для работы с файлами \[1\].

В `main`, новая инструкция `fs::read_to_string` принимает `file_path`, открывает этот файл и возвращает `std::io::Result<String>` содержимого файла \[2\].

После этого мы снова добавляем временную инструкцию `println!`, которая выводит значение `contents` после чтения файла, чтобы проверить, работает ли программа до сих пор \[3\].

Запустим этот код с любым строковым аргументом в качестве первого аргумента командной строки (потому что мы еще не реализовали часть поиска) и файлом _poem.txt_ в качестве второго аргумента:

```bash
$ cargo run -- the poem.txt
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep the poem.txt`
Searching for the
In file poem.txt
With text:
I'm nobody! Who are you?
Are you nobody, too?
Then there's a pair of us - don't tell!
They'd banish us, you know.

How dreary to be somebody!
How public, like a frog
To tell your name the livelong day
To an admiring bog!
```

Отлично! Код прочитал и вывел содержимое файла. Но код имеет несколько недостатков. В настоящее время функция `main` имеет несколько обязанностей: как правило, функции проще понять и легче поддерживать, если каждая функция отвечает только за одну идею. Другая проблема заключается в том, что мы не обрабатываем ошибки как следует. Программа еще небольшая, поэтому эти недостатки не представляют большой проблемы, но по мере роста программы будет труднее исправить их корректно. Хорошим практикой является раннее начало рефакторинга при разработке программы, потому что гораздо проще рефакторить меньшие объемы кода. Мы это сделаем далее.
