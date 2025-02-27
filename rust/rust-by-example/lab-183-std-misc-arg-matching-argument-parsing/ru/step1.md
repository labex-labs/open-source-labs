# Разбор аргументов

Сопоставление можно использовать для разбора простых аргументов:

```rust
use std::env;

fn increase(number: i32) {
    println!("{}", number + 1);
}

fn decrease(number: i32) {
    println!("{}", number - 1);
}

fn help() {
    println!("usage:
match_args <string>
    Проверить, является ли заданная строка ответом.
match_args {{increase|decrease}} <integer>
    Увеличить или уменьшить заданное целое число на единицу.");
}

fn main() {
    let args: Vec<String> = env::args().collect();

    match args.len() {
        // аргументы не переданы
        1 => {
            println!("Меня зовут'match_args'. Попробуйте передать некоторые аргументы!");
        },
        // передан один аргумент
        2 => {
            match args[1].parse() {
                Ok(42) => println!("This is the answer!"),
                _ => println!("This is not the answer."),
            }
        },
        // передана одна команда и один аргумент
        3 => {
            let cmd = &args[1];
            let num = &args[2];
            // преобразовать число
            let number: i32 = match num.parse() {
                Ok(n) => {
                    n
                },
                Err(_) => {
                    eprintln!("error: second argument not an integer");
                    help();
                    return;
                },
            };
            // преобразовать команду
            match &cmd[..] {
                "increase" => increase(number),
                "decrease" => decrease(number),
                _ => {
                    eprintln!("error: invalid command");
                    help();
                },
            }
        },
        // все остальные случаи
        _ => {
            // показать сообщение помощи
            help();
        }
    }
}
```

```shell
$./match_args Rust
This is not the answer.
$./match_args 42
This is the answer!
$./match_args do something
error: second argument not an integer
usage:
match_args <string>
    Проверить, является ли заданная строка ответом.
match_args {increase|decrease} <integer>
    Увеличить или уменьшить заданное целое число на единицу.
$./match_args do 42
error: invalid command
usage:
match_args <string>
    Проверить, является ли заданная строка ответом.
match_args {increase|decrease} <integer>
    Увеличить или уменьшить заданное целое число на единицу.
$./match_args increase 42
43
```
