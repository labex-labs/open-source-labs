# 遮蔽

正如你在第2章的猜数字游戏教程中看到的，你可以声明一个与先前变量同名的新变量。Rust开发者说第一个变量被第二个变量**遮蔽**了，这意味着当你使用变量名时，编译器看到的是第二个变量。实际上，第二个变量遮蔽了第一个变量，将变量名的任何使用都归为自身，直到它自己被遮蔽或作用域结束。我们可以通过使用相同的变量名并重复使用 `let` 关键字来遮蔽一个变量，如下所示：

文件名：`src/main.rs`

```rust
fn main() {
    let x = 5;

    let x = x + 1;

    {
        let x = x * 2;
        println!("The value of x in the inner scope is: {x}");
    }

    println!("The value of x is: {x}");
}
```

这个程序首先将 `x` 绑定到值 `5`。然后它通过重复 `let x =` 创建一个新变量 `x`，取原始值并加 `1`，所以 `x` 的值变为 `6`。然后，在由花括号创建的内部作用域中，第三个 `let` 语句也遮蔽了 `x` 并创建一个新变量，将前一个值乘以 `2` 得到 `x` 的值为 `12`。当那个作用域结束时，内部遮蔽结束，`x` 又变回 `6`。当我们运行这个程序时，它将输出以下内容：

```bash
$ cargo run
   Compiling variables v0.1.0 (file:///projects/variables)
    Finished dev [unoptimized + debuginfo] target(s) in 0.31s
     Running `target/debug/variables`
The value of x in the inner scope is: 12
The value of x is: 6
```

遮蔽与将变量标记为 `mut` 不同，因为如果我们不小心尝试在不使用 `let` 关键字的情况下重新赋值给这个变量，我们会得到一个编译时错误。通过使用 `let`，我们可以对一个值进行一些转换，但在转换完成后变量仍然是不可变的。

`mut` 和遮蔽之间的另一个区别是，因为当我们再次使用 `let` 关键字时实际上是创建了一个新变量，所以我们可以改变值的类型但重用相同的名称。例如，假设我们的程序要求用户通过输入空格字符来显示他们想要在某些文本之间留多少个空格，然后我们想将该输入存储为一个数字：

```rust
let spaces = "   ";
let spaces = spaces.len();
```

第一个 `spaces` 变量是字符串类型，第二个 `spaces` 变量是数字类型。因此，遮蔽使我们不必想出不同的名称，比如 `spaces_str` 和 `spaces_num`；相反，我们可以重用更简单的 `spaces` 名称。然而，如果我们尝试像这样使用 `mut`，我们会得到一个编译时错误：

```rust
let mut spaces = "   ";
spaces = spaces.len();
```

错误信息表明我们不允许改变变量的类型：

```bash
$ cargo run
   Compiling variables v0.1.0 (file:///projects/variables)
error[E0308]: mismatched types
 --> src/main.rs:3:14
  |
2 |     let mut spaces = "   ";
  |                      ----- expected due to this value
3 |     spaces = spaces.len();
  |              ^^^^^^^^^^^^ expected `&str`, found `usize`
```

既然我们已经探讨了变量的工作原理，让我们来看看它们可以拥有的更多数据类型。
