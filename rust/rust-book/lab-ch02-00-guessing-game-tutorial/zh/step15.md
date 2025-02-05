# 使用循环允许多次猜测

`loop` 关键字会创建一个无限循环。我们将添加一个循环，给用户更多机会来猜测数字：

文件名：`src/main.rs`

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

如你所见，我们将从猜测输入提示开始的所有内容都移到了一个循环中。确保将循环内的行再各自缩进四个空格，然后再次运行程序。现在程序将永远要求输入另一个猜测，这实际上引入了一个新问题。看起来用户无法退出！

用户总是可以通过使用键盘快捷键 ctrl-C 来中断程序。但正如在“比较猜测值和秘密数字”中关于 `parse` 的讨论中提到的，还有另一种方法可以逃离这个贪得无厌的怪物：如果用户输入一个非数字答案，程序将会崩溃。我们可以利用这一点来允许用户退出，如下所示：

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
thread'main' panicked at 'Please type a number!: ParseIntError
{ kind: InvalidDigit }', src/main.rs:28:47
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
```

输入 `quit` 会退出游戏，但正如你会注意到的，输入任何其他非数字输入也会这样。至少可以说，这并不理想；我们希望游戏在猜出正确数字时也能停止。
