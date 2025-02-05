# `?` 的其他用法

注意在上一个示例中，我们对调用 `parse` 的直接反应是将库错误映射为装箱错误：

```rust
.and_then(|s| s.parse::<i32>())
 .map_err(|e| e.into())
```

由于这是一个简单且常见的操作，如果可以省略它会很方便。可惜，因为 `and_then` 不够灵活，所以无法做到。不过，我们可以改用 `?`。

之前解释过 `?` 要么是 `unwrap`，要么是 `return Err(err)`。这只是大致正确。实际上它的意思是 `unwrap` 或者 `return Err(From::from(err))`。由于 `From::from` 是不同类型之间的转换工具，这意味着如果你在错误可转换为返回类型的地方使用 `?`，它会自动进行转换。

在这里，我们使用 `?` 重写前面的示例。结果是，当为我们的错误类型实现了 `From::from` 时，`map_err` 就会消失：

```rust
use std::error;
use std::fmt;

// 将别名更改为 `Box<dyn error::Error>`。
type Result<T> = std::result::Result<T, Box<dyn error::Error>>;

#[derive(Debug)]
struct EmptyVec;

impl fmt::Display for EmptyVec {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "invalid first item to double")
    }
}

impl error::Error for EmptyVec {}

// 与之前的结构相同，但不是将所有 `Result` 和 `Option` 链式连接起来，
// 而是使用 `?` 立即获取内部值。
fn double_first(vec: Vec<&str>) -> Result<i32> {
    let first = vec.first().ok_or(EmptyVec)?;
    let parsed = first.parse::<i32>()?;
    Ok(2 * parsed)
}

fn print(result: Result<i32>) {
    match result {
        Ok(n)  => println!("The first doubled is {}", n),
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

现在这实际上相当简洁。与原始的 `panic` 相比，它与用 `?` 替换 `unwrap` 调用非常相似，只是返回类型是 `Result`。因此，必须在顶级解构它们。
