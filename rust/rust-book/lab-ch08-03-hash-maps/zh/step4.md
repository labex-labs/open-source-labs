# 哈希映射与所有权

对于实现了 `Copy` 特性的类型，比如 `i32`，值会被复制到哈希映射中。对于像 `String` 这样的拥有所有权的值，值会被移动，并且哈希映射将成为这些值的所有者，如清单 8-22 所示。

```rust
use std::collections::HashMap;

let field_name = String::from("Favorite color");
let field_value = String::from("Blue");

let mut map = HashMap::new();
map.insert(field_name, field_value);
// field_name 和 field_value 在此处无效，尝试
// 使用它们，看看会得到什么编译器错误！
```

清单 8-22：展示键和值在插入哈希映射后由其拥有

在通过调用 `insert` 将变量 `field_name` 和 `field_value` 移动到哈希映射中之后，我们就无法再使用它们了。

如果我们将值的引用插入到哈希映射中，值不会被移动到哈希映射中。引用所指向的值必须至少在哈希映射有效期间内保持有效。我们将在“使用生命周期验证引用”中更多地讨论这些问题。
