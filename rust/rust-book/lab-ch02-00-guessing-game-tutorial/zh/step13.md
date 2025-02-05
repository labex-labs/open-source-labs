# 生成随机数

让我们开始使用 `rand` 来生成一个要猜测的数字。下一步是更新 `src/main.rs`，如清单 2-3 所示。

文件名：`src/main.rs`

```rust
use std::io;
1 use rand::Rng;

fn main() {
    println!("Guess the number!");

  2 let secret_number = rand::thread_rng().gen_range(1..=100);

  3 println!("The secret number is: {secret_number}");

    println!("Please input your guess.");

    let mut guess = String::new();

    io::stdin()
     .read_line(&mut guess)
     .expect("Failed to read line");

    println!("You guessed: {guess}");
}
```

清单 2-3：添加生成随机数的代码

首先，我们添加了 `use rand::Rng;` 这一行 \[1\]。`Rng` 特性定义了随机数生成器实现的方法，并且为了使用这些方法，这个特性必须在作用域内。第 10 章将详细介绍特性。

接下来，我们在中间添加了两行。在第一行 \[2\] 中，我们调用 `rand::thread_rng` 函数，它为我们提供要使用的特定随机数生成器：一个是当前执行线程本地的并且由操作系统播种的生成器。然后我们在随机数生成器上调用 `gen_range` 方法。这个方法是由我们通过 `use rand::Rng;` 语句引入作用域的 `Rng` 特性定义的。`gen_range` 方法接受一个范围表达式作为参数，并在该范围内生成一个随机数。我们这里使用的范围表达式形式为 `start..=end`，并且包含下限和上限，所以我们需要指定 `1..=100` 来请求一个 1 到 100 之间的数字。

> 注意：你不会仅仅知道要使用哪些特性以及从一个包中调用哪些方法和函数，所以每个包都有使用说明的文档。Cargo 的另一个很棒的特性是运行 `cargo doc --open` 命令将在本地构建你所有依赖项提供的文档并在你的浏览器中打开它。例如，如果你对 `rand` 包中的其他功能感兴趣，运行 `cargo doc --open` 并在左边的侧边栏中点击 `rand`。

第二行新代码 \[3\] 打印秘密数字。在我们开发程序以便能够测试它的时候这很有用，但我们会在最终版本中删除它。如果程序一启动就打印出答案，那就没什么游戏可言了！

试着运行几次这个程序：

```bash
$ cargo run
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 2.53s
     Running `target/debug/guessing_game`
Guess the number!
The secret number is: 7
Please input your guess.
4
You guessed: 4

$ cargo run
    Finished dev [unoptimized + debuginfo] target(s) in 0.02s
     Running `target/debug/guessing_game`
Guess the number!
The secret number is: 83
Please input your guess.
5
You guessed: 5
```

你应该会得到不同的随机数，并且它们都应该是 1 到 100 之间的数字。干得好！
