# 按名称运行部分测试

有时，运行完整的测试套件可能需要很长时间。如果你正在处理特定区域的代码，可能只想运行与该代码相关的测试。你可以通过将你想要运行的测试名称作为参数传递给 `cargo test` 来选择运行哪些测试。

为了演示如何运行部分测试，我们首先为 `add_two` 函数创建三个测试，如清单 11-11 所示，然后选择运行哪些测试。

文件名：`src/lib.rs`

```rust
pub fn add_two(a: i32) -> i32 {
    a + 2
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn add_two_and_two() {
        assert_eq!(4, add_two(2));
    }

    #[test]
    fn add_three_and_two() {
        assert_eq!(5, add_two(3));
    }

    #[test]
    fn one_hundred() {
        assert_eq!(102, add_two(100));
    }
}
```

清单 11-11：三个具有不同名称的测试

正如我们之前看到的，如果不传递任何参数运行测试，所有测试将并行运行：

    running 3 tests
    test tests::add_three_and_two... ok
    test tests::add_two_and_two... ok
    test tests::one_hundred... ok

    test result: ok. 3 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s
