# 获取哈希映射中的值

我们可以通过向 `get` 方法提供键来从哈希映射中获取值，如清单 8-21 所示。

```rust
use std::collections::HashMap;

let mut scores = HashMap::new();

scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Yellow"), 50);

let team_name = String::from("Blue");
let score = scores.get(&team_name).copied().unwrap_or(0);
```

清单 8-21：获取存储在哈希映射中的蓝色队伍的分数

在这里，`score` 将具有与蓝色队伍相关联的值，结果将是 `10`。`get` 方法返回一个 `Option<&V>`；如果哈希映射中没有该键的值，`get` 将返回 `None`。此程序通过调用 `copied` 来处理 `Option`，以获取一个 `Option<i32>` 而不是 `Option<&i32>`，然后调用 `unwrap_or` 在 `scores` 中没有该键的条目时将 `score` 设置为零。

我们可以使用 `for` 循环，以与处理向量类似的方式遍历哈希映射中的每个键值对：

```rust
use std::collections::HashMap;

let mut scores = HashMap::new();

scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Yellow"), 50);

for (key, value) in &scores {
    println!("{key}: {value}");
}
```

这段代码将以任意顺序打印每一对：

```rust
Yellow: 50
Blue: 10
```
