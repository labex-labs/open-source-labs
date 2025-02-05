# 迭代 `Result`

`Iter::map` 操作可能会失败，例如：

```rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
    let numbers: Vec<_> = strings
     .into_iter()
     .map(|s| s.parse::<i32>())
     .collect();
    println!("Results: {:?}", numbers);
}
```

让我们逐步探讨处理此问题的策略。

## 使用 `filter_map()` 忽略失败的项

`filter_map` 调用一个函数，并过滤掉 `None` 的结果。

```rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
    let numbers: Vec<_> = strings
     .into_iter()
     .filter_map(|s| s.parse::<i32>().ok())
     .collect();
    println!("Results: {:?}", numbers);
}
```

## 使用 `map_err()` 和 `filter_map()` 收集失败的项

`map_err` 用错误调用一个函数，因此通过将其添加到前面的 `filter_map` 解决方案中，我们可以在迭代时将错误保存到一边。

```rust
fn main() {
    let strings = vec!["42", "tofu", "93", "999", "18"];
    let mut errors = vec![];
    let numbers: Vec<_> = strings
     .into_iter()
     .map(|s| s.parse::<u8>())
     .filter_map(|r| r.map_err(|e| errors.push(e)).ok())
     .collect();
    println!("Numbers: {:?}", numbers);
    println!("Errors: {:?}", errors);
}
```

## 使用 `collect()` 使整个操作失败

`Result` 实现了 `FromIterator`，因此结果向量 (`Vec<Result<T, E>>`) 可以转换为包含向量的结果 (`Result<Vec<T>, E>`)。一旦找到 `Result::Err`，迭代将终止。

```rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
    let numbers: Result<Vec<_>, _> = strings
     .into_iter()
     .map(|s| s.parse::<i32>())
     .collect();
    println!("Results: {:?}", numbers);
}
```

同样的技术也可用于 `Option`。

## 使用 `partition()` 收集所有有效值和失败情况

```rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
    let (numbers, errors): (Vec<_>, Vec<_>) = strings
     .into_iter()
     .map(|s| s.parse::<i32>())
     .partition(Result::is_ok);
    println!("Numbers: {:?}", numbers);
    println!("Errors: {:?}", errors);
}
```

当你查看结果时，会注意到所有内容仍然包裹在 `Result` 中。为此需要更多一点样板代码。

```rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
    let (numbers, errors): (Vec<_>, Vec<_>) = strings
     .into_iter()
     .map(|s| s.parse::<i32>())
     .partition(Result::is_ok);
    let numbers: Vec<_> = numbers.into_iter().map(Result::unwrap).collect();
    let errors: Vec<_> = errors.into_iter().map(Result::unwrap_err).collect();
    println!("Numbers: {:?}", numbers);
    println!("Errors: {:?}", errors);
}
```
