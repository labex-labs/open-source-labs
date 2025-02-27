# ループを使って複数回の予想を可能にする

`loop`キーワードは無限ループを作成します。ユーザーに数を予想する機会をもう少し与えるためにループを追加しましょう。

ファイル名：`src/main.rs`

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

ご覧の通り、予想入力プロンプト以降のすべてのコードをループ内に移動しました。ループ内の行をそれぞれさらに4つのスペースでインデントし、再度プログラムを実行してください。すると、プログラムは永久に別の予想を求め続けます。これは実際には新しい問題を引き起こします。ユーザーがゲームを終了できないように見えます！

ユーザーは常にキーボードショートカットのctrl-Cを使ってプログラムを中断することができます。しかし、「予想値と秘密の数を比較する」の`parse`に関する議論で言及されているように、この貪欲なモンスターから抜け出す別の方法もあります。ユーザーが数字以外の答えを入力した場合、プログラムはクラッシュします。これを利用してユーザーがゲームを終了できるようにすることができます。以下のようになります。

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

`quit`と入力するとゲームが終了しますが、ご覧の通り、他の数字以外の入力を行っても同じようにゲームが終了します。少なくとも言えば、これは最適ではありません。正解の数字を予想したときにもゲームが停止するようにしたいです。
