# while let

与 `if let` 类似，`while let` 可以让那些笨拙的 `match` 序列更易于接受。考虑以下递增 `i` 的序列：

```rust
// 创建一个类型为 `Option<i32>` 的 `optional`
let mut optional = Some(0);

// 重复进行此测试。
loop {
    match optional {
        // 如果 `optional` 解构成功，执行块中的代码。
        Some(i) => {
            if i > 9 {
                println!("大于 9，退出！");
                optional = None;
            } else {
                println!("`i` 的值是 `{:?}`。再试一次。", i);
                optional = Some(i + 1);
            }
            // ^ 需要 3 个缩进！
        },
        // 当解构失败时退出循环：
        _ => { break; }
        // ^ 为什么需要这样？肯定有更好的方法！
    }
}
```

使用 `while let` 会使这个序列好得多：

```rust
fn main() {
    // 创建一个类型为 `Option<i32>` 的 `optional`
    let mut optional = Some(0);

    // 这可以理解为：“当 `let` 将 `optional` 解构为
    // `Some(i)` 时，执行块 (`{}`)。否则 `break`。
    while let Some(i) = optional {
        if i > 9 {
            println!("大于 9，退出！");
            optional = None;
        } else {
            println!("`i` 的值是 `{:?}`。再试一次。", i);
            optional = Some(i + 1);
        }
        // ^ 向右的缩进更少，并且不需要
        // 显式处理失败的情况。
    }
    // ^ `if let` 有额外的可选 `else`/`else if`
    // 子句。`while let` 没有这些。
}
```
