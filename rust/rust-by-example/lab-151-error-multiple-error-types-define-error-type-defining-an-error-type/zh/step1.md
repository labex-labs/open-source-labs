# 定义错误类型

有时，用单一类型的错误来掩盖所有不同的错误会简化代码。我们将通过一个自定义错误来展示这一点。

Rust 允许我们定义自己的错误类型。一般来说，一个“好的”错误类型：

- 用同一类型表示不同错误
- 向用户呈现友好的错误消息
- 便于与其他类型进行比较
  - 好的：`Err(EmptyVec)`
  - 不好的：`Err("Please use a vector with at least one element".to_owned())`
- 能够保存有关错误的信息
  - 好的：`Err(BadChar(c, position))`
  - 不好的：`Err("+ cannot be used here".to_owned())`
- 能与其他错误很好地组合

```rust
use std::fmt;

type Result<T> = std::result::Result<T, DoubleError>;

// 定义我们的错误类型。这些可以根据我们的错误处理情况进行定制。
// 现在我们将能够编写自己的错误，委托给底层的错误实现，或者介于两者之间。
#[derive(Debug, Clone)]
struct DoubleError;

// 错误的生成与它的显示方式完全分开。
// 无需担心用显示样式来扰乱复杂的逻辑。
//
// 注意，我们没有存储任何关于错误的额外信息。这意味着在不修改我们的类型以携带该信息的情况下，我们无法说明哪个字符串解析失败。
impl fmt::Display for DoubleError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "invalid first item to double")
    }
}

fn double_first(vec: Vec<&str>) -> Result<i32> {
    vec.first()
        // 将错误更改为我们的新类型。
     .ok_or(DoubleError)
     .and_then(|s| {
            s.parse::<i32>()
                // 这里也更新为新的错误类型。
             .map_err(|_| DoubleError)
             .map(|i| 2 * i)
        })
}

fn print(result: Result<i32>) {
    match result {
        Ok(n) => println!("The first doubled is {}", n),
        Err(e) => println!("Error: {}", e),
    }
}

fn main() {
    let numbers = vec!["42", "93", "18"];
    let empty = vec![];
    let strings = vec!["tofu", "93", "18"];

    print(double_first(numbers));
    print(double_first(empty));
    print(double_first(strings));
}
```
