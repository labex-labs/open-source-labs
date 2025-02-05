# `Result` 的 `map` 方法

在前一个示例的 `multiply` 函数中使用 `unwrap` 会导致程序恐慌，这可不是健壮的代码。通常，我们希望将错误返回给调用者，以便调用者决定处理错误的正确方式。

我们首先需要知道正在处理的是哪种错误类型。要确定 `Err` 类型，我们查看 `parse()` 函数，它是为 `i32` 类型实现的 `FromStr` 特征。因此，`Err` 类型被指定为 `ParseIntError`。

在下面的示例中，直接使用 `match` 语句会使代码整体变得更加繁琐。

```rust
use std::num::ParseIntError;

// 重写返回类型后，我们使用模式匹配而不使用 `unwrap()`。
fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {
    match first_number_str.parse::<i32>() {
        Ok(first_number)  => {
            match second_number_str.parse::<i32>() {
                Ok(second_number)  => {
                    Ok(first_number * second_number)
                },
                Err(e) => Err(e),
            }
        },
        Err(e) => Err(e),
    }
}

fn print(result: Result<i32, ParseIntError>) {
    match result {
        Ok(n)  => println!("n is {}", n),
        Err(e) => println!("Error: {}", e),
    }
}

fn main() {
    // 这仍然会给出合理的答案。
    let twenty = multiply("10", "2");
    print(twenty);

    // 下面这个会给出更有用的错误信息。
    let tt = multiply("t", "2");
    print(tt);
}
```

幸运的是，`Option` 类型的 `map`、`and_then` 以及许多其他组合器也为 `Result` 类型实现了。`Result` 类型有完整的列表。

```rust
use std::num::ParseIntError;

// 与 `Option` 类型一样，我们可以使用 `map()` 等组合器。
// 这个函数与上面的函数功能相同，其含义是：
// 如果两个值都能从字符串解析成功，则相乘，否则传递错误。
fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {
    first_number_str.parse::<i32>().and_then(|first_number| {
        second_number_str.parse::<i32>().map(|second_number| first_number * second_number)
    })
}

fn print(result: Result<i32, ParseIntError>) {
    match result {
        Ok(n)  => println!("n is {}", n),
        Err(e) => println!("Error: {}", e),
    }
}

fn main() {
    // 这仍然会给出合理的答案。
    let twenty = multiply("10", "2");
    print(twenty);

    // 下面这个会给出更有用的错误信息。
    let tt = multiply("t", "2");
    print(tt);
}
```
