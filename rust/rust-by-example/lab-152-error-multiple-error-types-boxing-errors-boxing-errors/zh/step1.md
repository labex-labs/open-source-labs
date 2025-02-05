# 用 `Box` 包装错误

一种在保留原始错误的同时编写简单代码的方法是使用 `Box` 对它们进行包装。缺点是底层错误类型仅在运行时可知，而不是在编译时静态确定。

标准库通过让 `Box` 实现从任何实现 `Error` 特性的类型到特性对象 `Box<Error>` 的转换（通过 `From`），来帮助我们对错误进行装箱。

```rust
use std::error;
use std::fmt;

// 将别名更改为 `Box<error::Error>`。
type Result<T> = std::result::Result<T, Box<dyn error::Error>>;

#[derive(Debug, Clone)]
struct EmptyVec;

impl fmt::Display for EmptyVec {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "invalid first item to double")
    }
}

impl error::Error for EmptyVec {}

fn double_first(vec: Vec<&str>) -> Result<i32> {
    vec.first()
     .ok_or_else(|| EmptyVec.into()) // 转换为 Box
     .and_then(|s| {
            s.parse::<i32>()
             .map_err(|e| e.into()) // 转换为 Box
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
