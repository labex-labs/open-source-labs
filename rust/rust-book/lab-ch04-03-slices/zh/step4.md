# 作为参数的字符串切片

知道了你可以获取字面量和 `String` 值的切片后，我们可以对 `first_word` 进行进一步改进，那就是它的签名：

```rust
fn first_word(s: &String) -> &str {
```

更有经验的 Rust 开发者会写成清单 4-9 所示的签名，因为这样我们就可以在 `&String` 值和 `&str` 值上使用同一个函数。

```rust
fn first_word(s: &str) -> &str {
```

清单 4-9：通过将 `s` 参数的类型改为字符串切片来改进 `first_word` 函数

如果我们有一个字符串切片，就可以直接传递它。如果我们有一个 `String`，我们可以传递 `String` 的切片或者对 `String` 的引用。这种灵活性利用了**解引用强制转换**，这是一个我们将在“函数和方法的隐式解引用强制转换”中介绍的特性。

定义一个函数来接受字符串切片而不是对 `String` 的引用，会使我们的 API 更通用、更有用，同时不会损失任何功能：

文件名：`src/main.rs`

```rust
fn main() {
    let my_string = String::from("hello world");

    // `first_word` 适用于 `String` 的切片，无论是部分切片还是整个切片
    let word = first_word(&my_string[0..6]);
    let word = first_word(&my_string[..]);
    // `first_word` 也适用于对 `String` 的引用，这等同于 `String` 的整个切片
    let word = first_word(&my_string);

    let my_string_literal = "hello world";

    // `first_word` 适用于字符串字面量的切片，无论是部分切片还是整个切片
    let word = first_word(&my_string_literal[0..6]);
    let word = first_word(&my_string_literal[..]);

    // 因为字符串字面量本身就是字符串切片，所以这样也可以，无需切片语法！
    let word = first_word(my_string_literal);
}
```
