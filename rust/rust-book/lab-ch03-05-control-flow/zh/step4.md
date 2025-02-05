# 在 `let` 语句中使用 `if`

因为 `if` 是一个表达式，所以我们可以在 `let` 语句的右侧使用它，将结果赋给一个变量，如清单 3-2 所示。

文件名：`src/main.rs`

```rust
fn main() {
    let condition = true;
    let number = if condition { 5 } else { 6 };

    println!("number 的值是: {number}");
}
```

清单 3-2：将 `if` 表达式的结果赋给一个变量

`number` 变量将根据 `if` 表达式的结果绑定到一个值。运行这段代码，看看会发生什么：

```bash
$ cargo run
   正在编译 branches v0.1.0 (file:///projects/branches)
    已完成开发 [未优化 + 调试信息] 目标，耗时 0.30 秒
     正在运行 `target/debug/branches`
number 的值是: 5
```

记住，代码块计算结果为其中的最后一个表达式，数字本身也是表达式。在这种情况下，整个 `if` 表达式的值取决于执行哪个代码块。这意味着 `if` 每个分支可能产生的结果值必须是相同的类型；在清单 3-2 中，`if` 分支和 `else` 分支的结果都是 `i32` 整数。如果类型不匹配，如下例所示，我们将会得到一个错误：

文件名：`src/main.rs`

```rust
fn main() {
    let condition = true;

    let number = if condition { 5 } else { "six" };

    println!("number 的值是: {number}");
}
```

当我们尝试编译这段代码时，将会得到一个错误。`if` 和 `else` 分支的值类型不兼容，Rust 会准确指出程序中的问题所在：

```bash
$ cargo run
   正在编译 branches v0.1.0 (file:///projects/branches)
错误[E0308]：`if` 和 `else` 具有不兼容的类型
 --> src/main.rs:4:44
  |
4 |     let number = if condition { 5 } else { "six" };
  |                                 -          ^^^^^ 期望整数，找到
`&str`
  |                                 |
  |                                 因为这个原因期望
```

`if` 块中的表达式计算结果为一个整数，而 `else` 块中的表达式计算结果为一个字符串。这行不通，因为变量必须具有单一类型，并且 Rust 需要在编译时确切知道 `number` 变量是什么类型。知道 `number` 的类型可以让编译器在我们使用 `number` 的任何地方验证类型是否有效。如果 `number` 的类型仅在运行时确定，Rust 将无法做到这一点；如果编译器必须为任何变量跟踪多个假设类型，那么编译器将会更复杂，并且对代码的保证也会更少。
