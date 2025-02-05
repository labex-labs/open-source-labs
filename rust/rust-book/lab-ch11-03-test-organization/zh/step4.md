# 测试私有函数

在测试社区中，对于是否应该直接测试私有函数存在争议，并且其他语言使得测试私有函数变得困难或不可能。无论你坚持哪种测试理念，Rust 的隐私规则确实允许你测试私有函数。考虑清单 11-12 中的代码，其中有一个私有函数 `internal_adder`。

文件名：`src/lib.rs`

```rust
pub fn add_two(a: i32) -> i32 {
    internal_adder(a, 2)
}

fn internal_adder(a: i32, b: i32) -> i32 {
    a + b
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn internal() {
        assert_eq!(4, internal_adder(2, 2));
    }
}
```

清单 11-12：测试一个私有函数

请注意，`internal_adder` 函数没有被标记为 `pub`。测试只是 Rust 代码，而 `tests` 模块只是另一个模块。正如我们在“模块树中引用项的路径”中所讨论的，子模块中的项可以使用其祖先模块中的项。在这个测试中，我们使用 `use super::*` 将 `test` 模块的父模块的所有项引入作用域，然后测试就可以调用 `internal_adder`。如果你认为不应该测试私有函数，Rust 中没有什么会强迫你这样做。
