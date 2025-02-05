# 参数

我们可以定义带有**参数**的函数，参数是函数签名的一部分的特殊变量。当一个函数有参数时，你可以为这些参数提供具体的值。从技术上讲，具体的值被称为**实参**，但在日常交流中，人们倾向于互换使用“参数”和“实参”这两个词，来指代函数定义中的变量或调用函数时传入的具体值。

在 `another_function` 的这个版本中，我们添加了一个参数：

文件名：`src/main.rs`

```rust
fn main() {
    another_function(5);
}

fn another_function(x: i32) {
    println!("The value of x is: {x}");
}
```

尝试运行这个程序；你应该会得到以下输出：

```bash
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
    Finished dev [unoptimized + debuginfo] target(s) in 1.21s
     Running `target/debug/functions`
The value of x is: 5
```

`another_function` 的声明有一个名为 `x` 的参数。`x` 的类型被指定为 `i32`。当我们将 `5` 传递给 `another_function` 时，`println!` 宏会将 `5` 放在格式字符串中包含 `x` 的那对花括号的位置。

在函数签名中，你**必须**声明每个参数的类型。这是 Rust 设计中的一个有意为之的决定：在函数定义中要求类型注释意味着编译器几乎从不需要你在代码的其他地方使用它们来弄清楚你指的是什么类型。如果编译器知道函数期望的是什么类型，它也能够给出更有用的错误信息。

当定义多个参数时，用逗号分隔参数声明，如下所示：

文件名：`src/main.rs`

```rust
fn main() {
    print_labeled_measurement(5, 'h');
}

fn print_labeled_measurement(value: i32, unit_label: char) {
    println!("The measurement is: {value}{unit_label}");
}
```

这个例子创建了一个名为 `print_labeled_measurement` 的函数，它有两个参数。第一个参数名为 `value`，是 `i32` 类型。第二个参数名为 `unit_label`，是 `char` 类型。然后该函数会打印包含 `value` 和 `unit_label` 的文本。

让我们尝试运行这段代码。用前面的例子替换你 _functions_ 项目的 `src/main.rs` 文件中当前的程序，然后使用 `cargo run` 运行它：

```bash
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
    Finished dev [unoptimized + debuginfo] target(s) in 0.31s
     Running `target/debug/functions`
The measurement is: 5h
```

因为我们调用函数时将 `5` 作为 `value` 的值，将 `'h'` 作为 `unit_label` 的值，所以程序输出包含了这些值。
