# Позволение множества попыток угадывания с использованием цикла

Ключевое слово `loop` создает бесконечный цикл. Мы добавим цикл, чтобы дать пользователям больше шансов угадать число:

Имя файла: `src/main.rs`

```rust
use std::io;
use rand::Rng;
use std::cmp::Ordering;

fn main() {
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1..=100);

    println!("The secret number is: {secret_number}");

    loop {
        println!("Please input your guess.");
        let mut guess = String::new();

        io::stdin()
         .read_line(&mut guess)
         .expect("Failed to read line");

        let guess: u32 = guess
         .trim()
         .parse()
         .expect("Please type a number!");

        println!("You guessed: {guess}");

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => println!("You win!"),
        }
    }
}
```

Как вы можете видеть, мы переместили все, начиная от приглашения ввода попытки, в цикл. Убедитесь, что отступить строки внутри цикла на еще четыре пробела каждая и запустить программу снова. Теперь программа будет постоянно запрашивать новую попытку, что на самом деле представляет новую проблему. Казалось бы, пользователь не может выйти!

Пользователь всегда может прервать программу, используя сочетание клавиш ctrl-C. Но есть еще один способ избавиться от этой неутомимой монстры, как упоминалось в обсуждении `parse` в разделе "Сравнение попытки угадать с секретным числом": если пользователь вводит нечисловой ответ, программа упадет. Мы можем использовать это, чтобы позволить пользователю выйти, как показано здесь:

```bash
$ cargo run
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 1.50s
     Running `target/debug/guessing_game`
Guess the number!
The secret number is: 59
Please input your guess.
45
You guessed: 45
Too small!
Please input your guess.
60
You guessed: 60
Too big!
Please input your guess.
59
You guessed: 59
You win!
Please input your guess.
quit
thread 'main' panicked at 'Please type a number!: ParseIntError
{ kind: InvalidDigit }', src/main.rs:28:47
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
```

Ввод `quit` вызовет выход из игры, но, как вы заметите, так же будет выходить при вводе любого другого нечислового ввода. Это, по крайней мере, неоптимально; мы хотим, чтобы игра также останавливалась, когда угадано правильное число.
