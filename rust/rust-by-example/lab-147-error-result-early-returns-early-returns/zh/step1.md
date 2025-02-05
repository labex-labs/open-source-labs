# 提前返回

在上一个示例中，我们使用组合器显式地处理了错误。处理这种情况分析的另一种方法是结合使用 `match` 语句和**提前返回**。

也就是说，如果发生错误，我们可以简单地停止执行函数并返回错误。对于某些人来说，这种形式的代码可能更易于读写。考虑使用提前返回重写的上一个示例的这个版本：

```rust
use std::num::ParseIntError;

fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {
    let first_number = match first_number_str.parse::<i32>() {
        Ok(first_number)  => first_number,
        Err(e) => return Err(e),
    };

    let second_number = match second_number_str.parse::<i32>() {
        Ok(second_number)  => second_number,
        Err(e) => return Err(e),
    };

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

至此，我们已经学会了使用组合器和提前返回显式地处理错误。虽然我们通常希望避免恐慌，但显式地处理所有错误很麻烦。

在下一节中，我们将介绍 `?` 运算符，用于在我们只需要 `unwrap` 而又不会引发 `panic` 的情况下。
