# 泛型类型参数、trait 约束和生命周期一起使用

让我们简要看看在一个函数中同时指定泛型类型参数、trait 约束和生命周期的语法！

```rust
use std::fmt::Display;

fn longest_with_an_announcement<'a, T>(
    x: &'a str,
    y: &'a str,
    ann: T,
) -> &'a str
where
    T: Display,
{
    println!("Announcement! {ann}");
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
```

这是清单 10-21 中的 `longest` 函数，它返回两个字符串切片中较长的那个。但现在它有一个额外的名为 `ann` 的泛型类型 `T` 的参数，它可以由 `where` 子句指定的任何实现了 `Display` trait 的类型填充。这个额外的参数将使用 `{}` 打印，这就是为什么需要 `Display` trait 约束。因为生命周期是一种泛型，所以生命周期参数 `'a` 和泛型类型参数 `T` 的声明在函数名后的尖括号内的同一列表中。
