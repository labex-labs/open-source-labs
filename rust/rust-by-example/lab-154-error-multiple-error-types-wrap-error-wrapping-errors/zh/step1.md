# 包装错误

与将错误装箱的另一种方法是将它们包装在你自己的错误类型中。

```rust
use std::error;
use std::error::Error;
use std::num::ParseIntError;
use std::fmt;

type Result<T> = std::result::Result<T, DoubleError>;

#[derive(Debug)]
enum DoubleError {
    EmptyVec,
    // 我们将把解析错误委托给其错误实现。
    // 提供额外信息需要向类型中添加更多数据。
    Parse(ParseIntError),
}

impl fmt::Display for DoubleError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match *self {
            DoubleError::EmptyVec =>
                write!(f, "请使用至少包含一个元素的向量"),
            // 包装的错误包含额外信息，可通过 source() 方法获取。
            DoubleError::Parse(..) =>
                write!(f, "提供的字符串无法解析为整数"),
        }
    }
}

impl error::Error for DoubleError {
    fn source(&self) -> Option<&(dyn error::Error + 'static)> {
        match *self {
            DoubleError::EmptyVec => None,
            // 原因是底层实现错误类型。它会隐式转换为 trait 对象 `&error::Error`。这之所以可行，是因为底层类型已经实现了`Error` trait。
            DoubleError::Parse(ref e) => Some(e),
        }
    }
}

// 实现从 `ParseIntError`到`DoubleError` 的转换。
// 如果需要将 `ParseIntError`转换为`DoubleError`，`?` 会自动调用此函数。
impl From<ParseIntError> for DoubleError {
    fn from(err: ParseIntError) -> DoubleError {
        DoubleError::Parse(err)
    }
}

fn double_first(vec: Vec<&str>) -> Result<i32> {
    let first = vec.first().ok_or(DoubleError::EmptyVec)?;
    // 这里我们隐式使用了 `From`的`ParseIntError` 实现（我们上面定义的）来创建一个`DoubleError`。
    let parsed = first.parse::<i32>()?;

    Ok(2 * parsed)
}

fn print(result: Result<i32>) {
    match result {
        Ok(n)  => println!("第一个数翻倍后是{}", n),
        Err(e) => {
            println!("错误：{}", e);
            if let Some(source) = e.source() {
                println!("  由以下原因导致：{}", source);
            }
        },
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

这会增加一些处理错误的样板代码，并且在所有应用中可能并非都需要。有一些库可以为你处理这些样板代码。
