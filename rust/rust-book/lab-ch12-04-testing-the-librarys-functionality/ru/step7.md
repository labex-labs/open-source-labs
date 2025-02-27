# Использование функции search в функции run

Теперь, когда функция `search` работает и протестирована, нам нужно вызвать `search` из нашей функции `run`. Мы должны передать значение `config.query` и `contents`, которое `run` читает из файла, функции `search`. Затем `run` выведет каждую строку, возвращаемую функцией `search`:

Имя файла: `src/lib.rs`

```rust
pub fn run(config: Config) -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string(config.file_path)?;

    for line in search(&config.query, &contents) {
        println!("{line}");
    }

    Ok(())
}
```

Мы по-прежнему используем цикл `for`, чтобы вернуть каждую строку из `search` и вывести ее.

Теперь вся программа должна работать! Попробуем ее, сначала с словом, которое должно вернуть ровно одну строку из стихотворения Эмили Диккенсон: _frog_.

```bash
$ cargo run -- frog poem.txt
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.38s
     Running `target/debug/minigrep frog poem.txt`
How public, like a frog
```

Отлично! Теперь попробуем слово, которое совпадет с несколькими строками, например, _body_:

```bash
$ cargo run -- body poem.txt
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep body poem.txt`
I'm nobody! Who are you?
Are you nobody, too?
How dreary to be somebody!
```

И наконец, давайте убедимся, что мы не получаем никаких строк, когда ищем слово, которое не встречается нигде в стихотворении, например, _monomorphization_:

```bash
$ cargo run -- monomorphization poem.txt
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep monomorphization poem.txt`
```

Отлично! Мы создали свою мини-версию классического инструмента и узнали много о том, как структурировать приложения. Мы также узнали немного о вводе-выводе файлов, жизненных периодах, тестировании и разборе командной строки.

Чтобы завершить этот проект, мы кратко покажем, как работать с переменными окружения и как выводить сообщения в стандартный вывод ошибок, что полезно при написании командных строковых программ.
