# 语句和表达式

函数体由一系列语句组成，这些语句可以选择以一个表达式结尾。到目前为止，我们所涉及的函数都没有以表达式结尾，但你已经见过表达式作为语句的一部分。因为 Rust 是一种基于表达式的语言，所以理解这一重要区别很有必要。其他语言没有同样的区别，所以让我们来看看什么是语句和表达式，以及它们的区别如何影响函数体。

- **语句**：是执行某些操作且不返回值的指令。
- **表达式**：计算出一个结果值。让我们来看一些例子。

实际上，我们已经使用过语句和表达式了。使用 `let` 关键字创建一个变量并为其赋值就是一个语句。在清单 3-1 中，`let y = 6;` 就是一个语句。

文件名：`src/main.rs`

```rust
fn main() {
    let y = 6;
}
```

清单 3-1：一个包含一条语句的 `main` 函数声明

函数定义也是语句；整个前面的例子本身就是一个语句。

语句不返回值。因此，你不能像下面的代码那样将一个 `let` 语句赋给另一个变量；你会得到一个错误：

文件名：`src/main.rs`

```rust
fn main() {
    let x = (let y = 6);
}
```

当你运行这个程序时，你得到的错误如下：

```bash
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
error: expected expression, found statement (`let`)
 --> src/main.rs:2:14
  |
2 |     let x = (let y = 6);
  |              ^^^^^^^^^
  |
  = note: variable declaration using `let` is a statement

error[E0658]: `let` expressions in this position are unstable
 --> src/main.rs:2:14
  |
2 |     let x = (let y = 6);
  |              ^^^^^^^^^
  |
  = note: see issue #53667 <https://github.com/rust-lang/rust/issues/53667> for
more information
```

`let y = 6` 语句不返回值，所以没有任何值可供 `x` 绑定。这与其他语言（如 C 和 Ruby）不同，在那些语言中，赋值会返回赋值的值。在那些语言中，你可以写 `x = y = 6`，这样 `x` 和 `y` 都会有值 `6`；但在 Rust 中并非如此。

表达式计算出一个值，并且构成了你在 Rust 中编写的大部分其他代码。考虑一个数学运算，比如 `5 + 6`，这是一个计算结果为值 `11` 的表达式。表达式可以是语句的一部分：在清单 3-1 中，语句 `let y = 6;` 中的 `6` 就是一个计算结果为值 `6` 的表达式。调用一个函数是一个表达式。调用一个宏是一个表达式。用花括号创建的一个新的作用域块是一个表达式，例如：

文件名：`src/main.rs`

```rust
fn main() {
  1 let y = {2
        let x = 3;
      3 x + 1
    };

    println!("The value of y is: {y}");
}
```

表达式 \[2\] 是一个块，在这种情况下，它计算结果为 `4`。作为 `let` 语句 \[1\] 的一部分，那个值被绑定到 `y` 上。注意最后一行没有分号 \[3\]，这与你目前看到的大多数行不同。表达式不包括结尾的分号。如果你在一个表达式的末尾添加一个分号，你就把它变成了一个语句，然后它将不会返回值。在你接下来探索函数返回值和表达式时，请记住这一点。
