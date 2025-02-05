# 覆盖值

如果我们向哈希映射中插入一个键值对，然后再用不同的值插入同一个键，那么与该键关联的值将会被替换。尽管清单 8-23 中的代码调用了两次 `insert`，但哈希映射只会包含一个键值对，因为我们两次插入的都是蓝色队伍键的值。

```rust
use std::collections::HashMap;

let mut scores = HashMap::new();

scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Blue"), 25);

println!("{:?}", scores);
```

清单 8-23：替换特定键存储的值

这段代码将打印 `{"Blue": 25}`。原来的值 `10` 已被覆盖。
