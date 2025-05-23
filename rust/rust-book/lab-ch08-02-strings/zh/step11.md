# 遍历字符串的方法

处理字符串片段的最佳方法是明确你想要的是字符还是字节。对于单个 Unicode 标量值，使用 `chars` 方法。对“Зд”调用 `chars` 会将其分开并返回两个 `char` 类型的值，你可以遍历结果来访问每个元素：

    for c in "Зд".chars() {
        println!("{c}");
    }

这段代码将输出：

```rust
З
д
```

或者，`bytes` 方法返回每个原始字节，这可能适合你的应用场景：

    for b in "Зд".bytes() {
        println!("{b}");
    }

这段代码将输出组成这个字符串的四个字节：

    208
    151
    208
    180

但要记住，有效的 Unicode 标量值可能由多个字节组成。

从字符串中获取字形簇，比如对于天城体文字，是很复杂的，所以标准库没有提供此功能。如果你需要此功能，可以在 *https://crates.io* 上找到相关的 crate。
