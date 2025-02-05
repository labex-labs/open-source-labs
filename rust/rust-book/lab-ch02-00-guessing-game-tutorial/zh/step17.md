# 处理无效输入

为了进一步优化游戏的行为，当用户输入非数字时，我们不要让程序崩溃，而是让游戏忽略这个非数字输入，这样用户就可以继续猜测。我们可以通过修改将 `guess` 从 `String` 转换为 `u32` 的那一行代码来实现，如清单 2-5 所示。

文件名：`src/main.rs`

```rust
--snip--

io::stdin()
 .read_line(&mut guess)
 .expect("Failed to read line");

let guess: u32 = match guess.trim().parse() {
    Ok(num) => num,
    Err(_) => continue,
};

println!("You guessed: {guess}");

--snip--
```

清单 2-5：忽略非数字猜测并要求再次猜测，而不是让程序崩溃

我们从使用 `expect` 调用改为使用 `match` 表达式，以便从在错误时崩溃转变为处理错误。记住，`parse` 返回一个 `Result` 类型，而 `Result` 是一个枚举，它有 `Ok` 和 `Err` 这两个变体。我们在这里使用了一个 `match` 表达式，就像我们对 `cmp` 方法的 `Ordering` 结果所做的那样。

如果 `parse` 能够成功地将字符串转换为数字，它将返回一个包含结果数字的 `Ok` 值。这个 `Ok` 值将匹配第一个分支的模式，并且 `match` 表达式将只返回 `parse` 生成并放在 `Ok` 值中的 `num` 值。这个数字最终会在我们创建的新 `guess` 变量中处于我们想要的位置。

如果 `parse` 不能将字符串转换为数字，它将返回一个包含有关错误的更多信息的 `Err` 值。`Err` 值与第一个 `match` 分支中的 `Ok(num)` 模式不匹配，但它与第二个分支中的 `Err(_)` 模式匹配。下划线 `_` 是一个通配符值；在这个例子中，我们说我们想要匹配所有的 `Err` 值，无论它们内部包含什么信息。所以程序将执行第二个分支的代码 `continue`，这会告诉程序进入 `loop` 的下一次迭代并要求再次猜测。所以，实际上，程序忽略了 `parse` 可能遇到的所有错误！

现在程序中的所有内容都应该按预期工作了。让我们试试看：

```bash
$ cargo run
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 4.45s
     Running `target/debug/guessing_game`
Guess the number!
The secret number is: 61
Please input your guess.
10
You guessed: 10
Too small!
Please input your guess.
99
You guessed: 99
Too big!
Please input your guess.
foo
Please input your guess.
61
You guessed: 61
You win!
```

太棒了！再做一个小的最终调整，我们就将完成猜数字游戏。回想一下，程序仍然在打印秘密数字。这在测试时很有用，但它破坏了游戏体验。让我们删除输出秘密数字的 `println!`。清单 2-6 展示了最终代码。

文件名：`src/main.rs`

```rust
use rand::Rng;
use std::cmp::Ordering;
use std::io;

fn main() {
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1..=100);

    loop {
        println!("Please input your guess.");

        let mut guess = String::new();

        io::stdin()
         .read_line(&mut guess)
         .expect("Failed to read line");

        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        println!("You guessed: {guess}");

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => {
                println!("You win!");
                break;
            }
        }
    }
}
```

清单 2-6：完整的猜数字游戏代码

至此，你已经成功构建了猜数字游戏。恭喜！
