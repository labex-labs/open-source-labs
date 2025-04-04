# 重复

宏可以在参数列表中使用 `+` 来表示一个参数可以至少重复一次，或者使用 `*` 来表示该参数可以重复零次或更多次。

在以下示例中，用 `$(...),+` 包围匹配器将匹配一个或多个由逗号分隔的表达式。另请注意，在最后一种情况中，分号是可选的。

```rust
// `find_min!` 将计算任意数量参数中的最小值。
macro_rules! find_min {
    // 基本情况：
    ($x:expr) => ($x);
    // `$x` 后面跟着至少一个 `$y,`
    ($x:expr, $($y:expr),+) => (
        // 对尾部的 `$y` 调用 `find_min!`
        std::cmp::min($x, find_min!($($y),+))
    )
}

fn main() {
    println!("{}", find_min!(1));
    println!("{}", find_min!(1 + 2, 2));
    println!("{}", find_min!(5, 2 * 3, 4));
}
```
