# 开发依赖项

有时仅需要为测试（或示例、基准测试）添加依赖项。此类依赖项添加到 `Cargo.toml` 的 `[dev-dependencies]` 部分中。这些依赖项不会传播到依赖此包的其他包。

一个这样的示例是[`pretty_assertions`](https://docs.rs/pretty_assertions/1.0.0/pretty_assertions/index.html)，它扩展了标准的 `assert_eq!` 和 `assert_ne!` 宏，以提供彩色差异。
文件 `Cargo.toml`：

```toml
# 省略了标准的包数据
[dev-dependencies]
pretty_assertions = "1"
```

文件 `src/lib.rs`：

```rust
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

#[cfg(test)]
mod tests {
    use super::*;
    use pretty_assertions::assert_eq; // 仅用于测试的包。不能在非测试代码中使用。

    #[test]
    fn test_add() {
        assert_eq!(add(2, 3), 5);
    }
}
```
