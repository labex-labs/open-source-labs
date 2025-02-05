# `Result`

`Result` 是 `Option` 类型的更丰富版本，它描述的是可能的 _错误_ 而非可能的 _缺失_。

也就是说，`Result<T, E>` 可能有两种结果之一：

- `Ok(T)`：找到了元素 `T`
- `Err(E)`：找到了带有元素 `E` 的错误

按照惯例，预期的结果是 `Ok`，而意外的结果是 `Err`。

与 `Option` 一样，`Result` 也有许多与之相关的方法。例如，`unwrap()` 要么返回元素 `T`，要么导致程序 `panic`。对于情况处理，`Result` 和 `Option` 之间有许多重叠的组合器。

在使用 Rust 时，你可能会遇到返回 `Result` 类型的方法，比如 `parse()` 方法。将字符串解析为其他类型并不总是可行的，所以 `parse()` 返回一个 `Result` 来表示可能的失败。

让我们看看成功和不成功地 `parse()` 一个字符串时会发生什么：

```rust
fn multiply(first_number_str: &str, second_number_str: &str) -> i32 {
    // 我们试试用 `unwrap()` 取出数字。它会给我们带来麻烦吗？
    let first_number = first_number_str.parse::<i32>().unwrap();
    let second_number = second_number_str.parse::<i32>().unwrap();
    first_number * second_number
}

fn main() {
    let twenty = multiply("10", "2");
    println!("double is {}", twenty);

    let tt = multiply("t", "2");
    println!("double is {}", tt);
}
```

在不成功的情况下，`parse()` 会给 `unwrap()` 留下一个错误，从而导致程序 `panic`。此外，`panic` 会退出我们的程序并提供一个不太友好的错误消息。

为了提高我们错误消息的质量，我们应该更明确地指定返回类型，并考虑显式地处理错误。

## 在 `main` 函数中使用 `Result`

如果显式指定，`Result` 类型也可以是 `main` 函数的返回类型。通常 `main` 函数的形式如下：

```rust
fn main() {
    println!("Hello World!");
}
```

然而，`main` 函数也能够具有 `Result` 的返回类型。如果在 `main` 函数中发生错误，它将返回一个错误代码并打印错误的调试表示形式（使用 \[`Debug`\] 特性）。以下示例展示了这样一种情况，并涉及到 \[下一节\] 中涵盖的方面。

```rust
use std::num::ParseIntError;

fn main() -> Result<(), ParseIntError> {
    let number_str = "10";
    let number = match number_str.parse::<i32>() {
        Ok(number)  => number,
        Err(e) => return Err(e),
    };
    println!("{}", number);
    Ok(())
}
```
