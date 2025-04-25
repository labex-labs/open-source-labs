# 使用 `let`-`else`

借助 `let`-`else`，可反驳模式能够像普通的 `let` 一样匹配并绑定周围作用域中的变量，若模式不匹配，则会发散（例如 `break`、`return`、`panic!`）。

```rust
use std::str::FromStr;

fn get_count_item(s: &str) -> (u64, &str) {
    let mut it = s.split(' ');
    let (Some(count_str), Some(item)) = (it.next(), it.next()) else {
        panic!("无法分割计数 - 物品对：'{s}'");
    };
    let Ok(count) = u64::from_str(count_str) else {
        panic!("无法解析整数：'{count_str}'");
    };
    (count, item)
}

fn main() {
    assert_eq!(get_count_item("3 chairs"), (3, "chairs"));
}
```

名称绑定的作用域是它与 `match` 或 `if let`-`else` 表达式的主要区别所在。以前，你可能需要通过一些不太优雅的重复代码和外部 `let` 来近似实现这些模式：

```rust
use std::str::FromStr;

fn get_count_item(s: &str) -> (u64, &str) {
    let mut it = s.split(' ');
    let (count_str, item) = match (it.next(), it.next()) {
        (Some(count_str), Some(item)) => (count_str, item),
        _ => panic!("无法分割计数 - 物品对：'{s}'"),
    };
    let count = if let Ok(count) = u64::from_str(count_str) {
        count
    } else {
        panic!("无法解析整数：'{count_str}'");
    };
        (count, item)
    }

    assert_eq!(get_count_item("3 chairs"), (3, "chairs"));
```
