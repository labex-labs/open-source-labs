# 介绍 `?`

有时候，我们只想要 `unwrap` 的简便性，又不想有程序恐慌（panic）的可能性。到目前为止，当我们真正想要的是取出变量时，`unwrap` 却迫使我们进行越来越深的嵌套。这正是 `?` 的用途。

一旦发现 `Err`，有两种有效的操作：

1. `panic!`，我们已经决定尽可能避免这种情况
2. `return`，因为 `Err` 意味着无法处理

`?` 几乎\[\^†\]等同于一个 `unwrap`，它在遇到 `Err` 时返回而不是使程序恐慌（panic）。让我们看看如何简化之前使用组合器的示例：

```rust
use std::num::ParseIntError;

fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {
    let first_number = first_number_str.parse::<i32>()?;
    let second_number = second_number_str.parse::<i32>()?;

    Ok(first_number * second_number)
}

fn print(result: Result<i32, ParseIntError>) {
    match result {
        Ok(n)  => println!("n is {}", n),
        Err(e) => println!("Error: {}", e),
    }
}

fn main() {
    print(multiply("10", "2"));
    print(multiply("t", "2"));
}
```

## `try!` 宏

在有 `?` 之前，相同的功能是通过 `try!` 宏实现的。现在推荐使用 `?` 运算符，但在查看旧代码时你可能仍然会看到 `try!`。上一个示例中的相同 `multiply` 函数使用 `try!` 看起来会是这样：

```rust
// 要在使用 Cargo 时无错误地编译并运行此示例，请将 `Cargo.toml` 文件的 `[package]` 部分中的 `edition` 字段的值更改为 "2015"。

use std::num::ParseIntError;

fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {
    let first_number = try!(first_number_str.parse::<i32>());
    let second_number = try!(second_number_str.parse::<i32>());

    Ok(first_number * second_number)
}

fn print(result: Result<i32, ParseIntError>) {
    match result {
        Ok(n)  => println!("n is {}", n),
        Err(e) => println!("Error: {}", e),
    }
}

fn main() {
    print(multiply("10", "2"));
    print(multiply("t", "2"));
}
```
