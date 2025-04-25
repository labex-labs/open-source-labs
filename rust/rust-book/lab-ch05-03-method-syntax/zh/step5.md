# 多个 impl 块

每个结构体允许有多个 `impl` 块。例如，清单 5-15 等同于清单 5-16 中所示的代码，其中每个方法都在自己的 `impl` 块中。

```rust
impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }
}

impl Rectangle {
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}
```

清单 5-16：使用多个 `impl` 块重写清单 5-15

在这里没有理由将这些方法分成多个 `impl` 块，但这是有效的语法。在第 10 章讨论泛型类型和 trait 时，我们会看到一个多个 `impl` 块很有用的例子。
