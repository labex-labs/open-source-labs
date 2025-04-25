# 有返回值的函数

函数可以向调用它们的代码返回值。我们不给返回值命名，但必须在箭头（`->`）之后声明它们的类型。在 Rust 中，函数的返回值与函数体代码块中最后一个表达式的值同义。你可以使用 `return` 关键字并指定一个值提前从函数返回，但大多数函数会隐式返回最后一个表达式。下面是一个返回值的函数示例：

文件名：`src/main.rs`

```rust
fn five() -> i32 {
    5
}

fn main() {
    let x = five();

    println!("The value of x is: {x}");
}
```

`five` 函数中没有函数调用、宏，甚至没有 `let` 语句 —— 只有数字 `5` 本身。在 Rust 中，这是一个完全有效的函数。请注意，函数的返回类型也被指定为 `-> i32`。尝试运行这段代码；输出应该如下所示：

```bash
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
    Finished dev [unoptimized + debuginfo] target(s) in 0.30s
     Running `target/debug/functions`
The value of x is: 5
```

`five` 中的 `5` 是函数的返回值，这就是返回类型为 `i32` 的原因。让我们更详细地研究一下。有两个重要的点：首先，`let x = five();` 这一行表明我们正在使用函数的返回值来初始化一个变量。因为函数 `five` 返回一个 `5`，所以这一行与以下内容相同：

```rust
let x = 5;
```

其次，`five` 函数没有参数并定义了返回值的类型，但函数体是一个孤零零的 `5`，没有分号，因为它是一个我们想要返回其值的表达式。

让我们看另一个例子：

文件名：`src/main.rs`

```rust
fn main() {
    let x = plus_one(5);

    println!("The value of x is: {x}");
}

fn plus_one(x: i32) -> i32 {
    x + 1
}
```

运行这段代码将打印“The value of x is: 6”。但是如果我们在包含 `x + 1` 的行末尾加上分号，将其从一个表达式变为一个语句，我们就会得到一个错误：

文件名：`src/main.rs`

```rust
fn main() {
    let x = plus_one(5);

    println!("The value of x is: {x}");
}

fn plus_one(x: i32) -> i32 {
    x + 1;
}
```

编译这段代码会产生一个错误，如下所示：

```bash
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
error[E0308]: mismatched types
 --> src/main.rs:7:24
  |
7 | fn plus_one(x: i32) -> i32 {
  |    --------            ^^^ expected `i32`, found `()`
  |    |
  |    implicitly returns `()` as its body has no tail or `return` expression
8 |     x + 1;
  |          - help: remove this semicolon
```

主要的错误信息“mismatched types”揭示了这段代码的核心问题。函数 `plus_one` 的定义表明它将返回一个 `i32`，但语句不会计算出一个值，这由单元类型 `()` 表示。因此，没有返回任何值，这与函数定义相矛盾并导致错误。在这个输出中，Rust 提供了一条可能有助于纠正此问题的消息：它建议删除分号，这将修复错误。
