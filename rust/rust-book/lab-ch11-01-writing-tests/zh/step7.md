# 在测试中使用 `Result<T, E>`

到目前为止，我们的测试在失败时都会导致程序恐慌。我们也可以编写使用 `Result<T, E>` 的测试！这是清单 11 - 1 中的测试，重写后使用 `Result<T, E>` 并返回一个 `Err` 而不是导致程序恐慌：

文件名：`src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    #[test]
    fn it_works() -> Result<(), String> {
        if 2 + 2 == 4 {
            Ok(())
        } else {
            Err(String::from("two plus two does not equal four"))
        }
    }
}
```

`it_works` 函数现在具有 `Result<(), String>` 返回类型。在函数体中，我们不是调用 `assert_eq!` 宏，而是在测试通过时返回 `Ok(())`，在测试失败时返回一个包含 `String` 的 `Err`。

编写返回 `Result<T, E>` 的测试使你能够在测试体中使用问号运算符，这是一种编写测试的便捷方式，如果测试中的任何操作返回 `Err` 变体，测试就应该失败。

你不能在使用 `Result<T, E>` 的测试上使用 `#[should_panic]` 注解。要断言一个操作返回 `Err` 变体，_不要_ 在 `Result<T, E>` 值上使用问号运算符。相反，使用 `assert!(value.is_err())`。

既然你已经知道了几种编写测试的方法，让我们看看当我们运行测试时会发生什么，并探索我们可以与 `cargo test` 一起使用的不同选项。
