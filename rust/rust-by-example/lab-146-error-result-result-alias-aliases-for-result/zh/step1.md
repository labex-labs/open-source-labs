# `Result` 的别名

当我们想要多次复用特定的 `Result` 类型时该怎么办呢？回想一下，Rust 允许我们创建别名。很方便的是，我们可以为所讨论的特定 `Result` 定义一个别名。

在模块级别，创建别名可能会特别有帮助。在特定模块中发现的错误通常具有相同的 `Err` 类型，因此单个别名可以简洁地定义所有相关的 `Result`。这非常有用，以至于 `std` 库甚至提供了一个：`io::Result`！

下面是一个快速示例来展示语法：

```rust
use std::num::ParseIntError;

// 为错误类型为 `ParseIntError` 的 `Result` 定义一个通用别名。
type AliasedResult<T> = Result<T, ParseIntError>;

// 使用上述别名来引用我们特定的 `Result` 类型。
fn multiply(first_number_str: &str, second_number_str: &str) -> AliasedResult<i32> {
    first_number_str.parse::<i32>().and_then(|first_number| {
        second_number_str.parse::<i32>().map(|second_number| first_number * second_number)
    })
}

// 在这里，别名再次让我们节省了一些空间。
fn print(result: AliasedResult<i32>) {
    match result {
        Ok(n)  => println!("n 是 {}", n),
        Err(e) => println!("错误：{}", e),
    }
}

fn main() {
    print(multiply("10", "2"));
    print(multiply("t", "2"));
}
```
