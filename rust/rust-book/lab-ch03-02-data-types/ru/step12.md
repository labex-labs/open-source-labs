# Недопустимый доступ к элементу массива

Посмотрим, что произойдет, если вы попытаетесь получить доступ к элементу массива, который находится за его пределами. Предположим, что вы запускаете этот код, похожий на игру угадывания из главы 2, чтобы получить индекс массива от пользователя:

Имя файла: `src/main.rs`

```rust
use std::io;

fn main() {
    let a = [1, 2, 3, 4, 5];

    println!("Please enter an array index.");

    let mut index = String::new();

    io::stdin()
     .read_line(&mut index)
     .expect("Failed to read line");

    let index: usize = index
     .trim()
     .parse()
     .expect("Index entered was not a number");

    let element = a[index];

    println!(
        "The value of the element at index {index} is: {element}"
    );
}
```

Этот код успешно компилируется. Если вы запустите этот код с помощью `cargo run` и введете `0`, `1`, `2`, `3` или `4`, программа выведет соответствующее значение по этому индексу в массиве. Если вы вместо этого введете число, превышающее размер массива, например `10`, вы увидите такой вывод:

    thread'main' panicked at 'index out of bounds: the len is 5 but the index is
    10', src/main.rs:19:19
    note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

Программа завершилась с ошибкой в момент использования недопустимого значения в операции индексирования. Программа завершилась с сообщением об ошибке и не выполнила последнюю инструкцию `println!`. Когда вы пытаетесь получить доступ к элементу с использованием индексирования, Rust проверит, что индекс, который вы указали, меньше длины массива. Если индекс больше или равен длине, Rust сгенерирует панику. Эта проверка должна происходить во время выполнения, особенно в этом случае, потому что компилятор не может знать, какое значение введет пользователь, когда он запустит код позже.

Это пример практики принципов безопасности памяти Rust. Во многих низкоуровневых языках такая проверка не выполняется, и когда вы предоставляете неправильный индекс, можно получить доступ к недействительной памяти. Rust защищает вас от таких ошибок, немедленно завершая программу вместо того, чтобы позволить доступ к памяти и продолжить выполнение. Глава 9 рассматривает более подробно обработку ошибок в Rust и то, как вы можете писать читаемый, безопасный код, который не вызывает паники и не позволяет доступа к недействительной памяти.
