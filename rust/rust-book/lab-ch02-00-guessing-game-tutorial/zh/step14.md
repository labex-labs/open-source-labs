# 比较猜测值和秘密数字

既然我们已经有了用户输入和一个随机数，就可以对它们进行比较了。这一步如清单 2-4 所示。请注意，这段代码目前还无法编译，稍后我们会解释原因。

文件名：`src/main.rs`

```rust
use rand::Rng;
1 use std::cmp::Ordering;
use std::io;

fn main() {
    --snip--

    println!("You guessed: {guess}");

  2 match guess.3 cmp(&secret_number) {
        Ordering::Less => println!("Too small!"),
        Ordering::Greater => println!("Too big!"),
        Ordering::Equal => println!("You win!"),
    }
}
```

清单 2-4：处理比较两个数字时可能的返回值

首先，我们添加了另一个 `use` 语句 \[1\]，从标准库中引入一个名为 `std::cmp::Ordering` 的类型。`Ordering` 类型是另一个枚举，它有 `Less`、`Greater` 和 `Equal` 这几个变体。这些是比较两个值时可能出现的三种结果。

然后，我们在底部添加了五行使用 `Ordering` 类型的代码。`cmp` 方法 \[3\] 用于比较两个值，并且可以在任何可比较的类型上调用。它接受一个你想要与之比较的引用：这里是将 `guess` 与 `secret_number` 进行比较。然后它返回我们通过 `use` 语句引入作用域的 `Ordering` 枚举的一个变体。我们使用一个 `match` 表达式 \[2\] 根据调用 `cmp` 时使用 `guess` 和 `secret_number` 中的值返回的 `Ordering` 变体来决定接下来要做什么。

一个 `match` 表达式由 _分支_ 组成。一个分支由一个用于匹配的 _模式_ 以及如果传递给 `match` 的值符合该分支的模式时应该运行的代码组成。Rust 会获取传递给 `match` 的值，并依次查看每个分支的模式。模式和 `match` 结构是 Rust 的强大特性：它们让你能够表达代码可能遇到的各种情况，并确保你处理所有这些情况。这些特性将分别在第 6 章和第 18 章中详细介绍。

让我们通过这里使用的 `match` 表达式来走一个示例。假设用户猜了 50，而这次随机生成的秘密数字是 38。

当代码将 50 与 38 进行比较时，`cmp` 方法将返回 `Ordering::Greater`，因为 50 大于 38。`match` 表达式获取 `Ordering::Greater` 值并开始检查每个分支的模式。它查看第一个分支的模式 `Ordering::Less`，发现值 `Ordering::Greater` 与 `Ordering::Less` 不匹配，所以它忽略该分支中的代码并移动到下一个分支。下一个分支的模式是 `Ordering::Greater`，它 _确实_ 与 `Ordering::Greater` 匹配！该分支中的相关代码将执行并在屏幕上打印 `Too big!`。`match` 表达式在第一次成功匹配后结束，所以在这种情况下它不会查看最后一个分支。

然而，清单 2-4 中的代码目前还无法编译。让我们试试看：

```bash
$ cargo build
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
error[E0308]: mismatched types
  --> src/main.rs:22:21
   |
22 |     match guess.cmp(&secret_number) {
   |                     ^^^^^^^^^^^^^^ expected struct `String`, found integer
   |
   = note: expected reference `&String`
              found reference `&{integer}`
```

错误的核心表明存在 _类型不匹配_。Rust 有一个强大的静态类型系统。不过，它也有类型推断。当我们编写 `let mut guess = String::new()` 时，Rust 能够推断出 `guess` 应该是一个 `String` 类型，而不需要我们显式写出类型。另一方面，`secret_number` 是一个数字类型。Rust 有几种数字类型的值可以在 1 到 100 之间：`i32`，一个 32 位的数字；`u32`，一个无符号 32 位的数字；`i64`，一个 64 位的数字；以及其他类型。除非另有指定，Rust 默认使用 `i32`，除非你在其他地方添加了类型信息导致 Rust 推断出不同的数值类型，否则 `secret_number` 的类型就是 `i32`。错误的原因是 Rust 无法比较字符串和数字类型。

最终，我们希望将程序读取为输入的 `String` 转换为实际的数字类型，以便能够将其与秘密数字进行数值比较。我们通过在 `main` 函数体中添加这一行来实现：

文件名：`src/main.rs`

```rust
use std::io;
use rand::Rng;
use std::cmp::Ordering;

fn main() {
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1..=100);

    println!("The secret number is: {secret_number}");

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
```

我们创建了一个名为 `guess` 的变量。但是等等，程序不是已经有一个名为 `guess` 的变量了吗？没错，不过幸运的是 Rust 允许我们用一个新值 _遮蔽_ 之前的 `guess` 值。_遮蔽_ 让我们可以重用 `guess` 变量名，而不必强迫我们创建两个不同的变量，比如 `guess_str` 和 `guess`。我们将在第 3 章更详细地介绍这一点，但现在要知道，当你想将一个值从一种类型转换为另一种类型时，这个特性经常会被用到。

我们将这个新变量绑定到表达式 `guess.trim().parse()`。表达式中的 `guess` 指的是最初包含输入字符串的 `guess` 变量。`String` 实例上的 `trim` 方法会去除字符串开头和结尾的任何空白字符，为了能够将字符串与只能包含数值数据的 `u32` 进行比较，我们必须这样做。用户必须按下回车键以满足 `read_line` 并输入他们的猜测，这会在字符串中添加一个换行符。例如，如果用户输入 `5` 并按下回车键，`guess` 看起来像这样：`5\n`。`\n` 表示“换行”。（在 Windows 上，按下回车键会产生一个回车符和一个换行符，即 `\r\n`。）`trim` 方法会去除 `\n` 或 `\r\n`，结果只剩下 `5`。

字符串上的 `parse` 方法用于将字符串转换为另一种类型。在这里，我们用它将字符串转换为数字。我们需要通过使用 `let guess: u32` 告诉 Rust 我们想要的确切数字类型。`guess` 后面的冒号（`:`）告诉 Rust 我们将注释变量的类型。Rust 有几种内置的数字类型；这里看到的 `u32` 是一个无符号的 32 位整数。对于一个小的正数来说，它是一个不错的默认选择。你将在第 3 章了解其他数字类型。

此外，这个示例程序中的 `u32` 注释以及与 `secret_number` 的比较意味着 Rust 也会推断出 `secret_number` 应该也是一个 `u32`。所以现在比较将在两个相同类型的值之间进行！

`parse` 方法只对可以逻辑上转换为数字的字符有效，因此很容易出错。例如，如果字符串包含 `A`👍`%`，就没有办法将其转换为数字。因为它可能会失败，所以 `parse` 方法返回一个 `Result` 类型，就像 `read_line` 方法一样（在前面的“使用 Result 处理潜在失败”中讨论过）。我们将再次使用 `expect` 方法以相同的方式处理这个 `Result`。如果 `parse` 因为无法从字符串创建数字而返回 `Err` `Result` 变体，`expect` 调用将使游戏崩溃并打印我们给它的消息。如果 `parse` 能够成功地将字符串转换为数字，它将返回 `Result` 的 `Ok` 变体，并且 `expect` 将从 `Ok` 值中返回我们想要的数字。

现在让我们运行程序：

```bash
$ cargo run
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 0.43s
     Running `target/debug/guessing_game`
Guess the number!
The secret number is: 58
Please input your guess.
  76
You guessed: 76
Too big!
```

很好！即使在猜测之前添加了空格，程序仍然能够识别出用户猜的是 76。多次运行程序，以验证不同类型输入的不同行为：正确猜出数字、猜一个过高的数字以及猜一个过低的数字。

我们现在已经让游戏的大部分功能正常工作了，但是用户只能猜一次。让我们通过添加一个循环来改变这一点！
