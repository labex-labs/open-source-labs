# 函数中的泛型生命周期

我们将编写一个函数，返回两个字符串切片中较长的那个。这个函数将接受两个字符串切片，并返回一个字符串切片。在实现了 `longest` 函数之后，清单 10-19 中的代码应该会打印出 `The longest string is abcd`。

文件名：`src/main.rs`

```rust
fn main() {
    let string1 = String::from("abcd");
    let string2 = "xyz";

    let result = longest(string1.as_str(), string2);
    println!("The longest string is {result}");
}
```

清单 10-19：一个 `main` 函数，调用 `longest` 函数来找出两个字符串切片中较长的那个

请注意，我们希望函数接受字符串切片（即引用），而不是字符串，因为我们不希望 `longest` 函数获取其参数的所有权。有关为什么我们在清单 10-19 中使用这些参数的更多讨论，请参考“作为参数的字符串切片”。

如果我们尝试按清单 10-20 所示实现 `longest` 函数，它将无法编译。

文件名：`src/main.rs`

```rust
fn longest(x: &str, y: &str) -> &str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
```

清单 10-20：`longest` 函数的实现，返回两个字符串切片中较长的那个，但尚未编译

相反，我们会得到以下关于生命周期的错误：

```bash
error[E0106]: missing lifetime specifier
 --> src/main.rs:9:33
  |
9 | fn longest(x: &str, y: &str) -> &str {
  |               ----     ----     ^ expected named lifetime parameter
  |
  = help: this function's return type contains a borrowed value,
but the signature does not say whether it is borrowed from `x` or `y`
help: consider introducing a named lifetime parameter
  |
9 | fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
  |           ++++     ++          ++          ++
```

帮助信息表明返回类型需要一个泛型生命周期参数，因为 Rust 无法判断返回的引用是指向 `x` 还是 `y`。实际上，我们也不知道，因为这个函数体中的 `if` 块返回对 `x` 的引用，而 `else` 块返回对 `y` 的引用！

当我们定义这个函数时，我们不知道将传递给这个函数的具体值，所以我们不知道 `if` 情况还是 `else` 情况会执行。我们也不知道将传入的引用的具体生命周期，所以我们不能像在清单 10-17 和 10-18 中那样查看作用域来确定我们返回的引用是否始终有效。借用检查器也无法确定这一点，因为它不知道 `x` 和 `y` 的生命周期与返回值的生命周期有何关系。为了解决这个错误，我们将添加泛型生命周期参数来定义引用之间的关系，以便借用检查器能够进行分析。
