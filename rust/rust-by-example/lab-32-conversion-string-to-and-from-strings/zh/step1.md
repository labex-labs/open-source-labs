# 与字符串的转换

## 转换为字符串

将任何类型转换为 `String` 很简单，只需为该类型实现 `ToString` 特性。不过，你不应直接这样做，而应实现 `fmt::Display` 特性，它会自动提供 `ToString`，并且还允许像在 `print!` 部分讨论的那样打印该类型。

```rust
use std::fmt;

struct Circle {
    radius: i32
}

impl fmt::Display for Circle {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "Circle of radius {}", self.radius)
    }
}

fn main() {
    let circle = Circle { radius: 6 };
    println!("{}", circle.to_string());
}
```

## 解析字符串

将字符串转换为数字是比较常见的类型转换之一。惯用的方法是使用 `parse` 函数，并安排类型推断或使用 “turbofish” 语法指定要解析的类型。以下示例展示了这两种方法。

只要为该类型实现了 `FromStr` 特性，这将把字符串转换为指定的类型。标准库中的许多类型都实现了该特性。要在用户定义的类型上获得此功能，只需为该类型实现 `FromStr` 特性。

```rust
fn main() {
    let parsed: i32 = "5".parse().unwrap();
    let turbo_parsed = "10".parse::<i32>().unwrap();

    let sum = parsed + turbo_parsed;
    println!("Sum: {:?}", sum);
}
```
