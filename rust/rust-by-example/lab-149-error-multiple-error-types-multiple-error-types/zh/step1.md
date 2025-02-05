# 多种错误类型

之前的示例总是非常方便；`Result` 与其他 `Result` 交互，`Option` 与其他 `Option` 交互。

有时，一个 `Option` 需要与一个 `Result` 交互，或者一个 `Result<T, Error1>` 需要与一个 `Result<T, Error2>` 交互。在这些情况下，我们希望以一种使不同错误类型可组合且易于交互的方式来管理它们。

在以下代码中，`unwrap` 的两个实例会生成不同的错误类型。`Vec::first` 返回一个 `Option`，而 `parse::<i32>` 返回一个 `Result<i32, ParseIntError>`：

```rust
fn double_first(vec: Vec<&str>) -> i32 {
    let first = vec.first().unwrap(); // 生成错误1
    2 * first.parse::<i32>().unwrap() // 生成错误2
}

fn main() {
    let numbers = vec!["42", "93", "18"];
    let empty = vec![];
    let strings = vec!["tofu", "93", "18"];

    println!("The first doubled is {}", double_first(numbers));

    println!("The first doubled is {}", double_first(empty));
    // 错误1：输入向量为空

    println!("The first doubled is {}", double_first(strings));
    // 错误2：元素无法解析为数字
}
```

在接下来的部分中，我们将看到几种处理这类问题的策略。
