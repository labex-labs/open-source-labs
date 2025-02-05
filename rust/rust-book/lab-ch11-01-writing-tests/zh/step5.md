# 添加自定义失败消息

你还可以添加一条自定义消息，与失败消息一起打印，作为 `assert!`、`assert_eq!` 和 `assert_ne!` 宏的可选参数。在必选参数之后指定的任何参数都会被传递给 `format!` 宏（在“使用 + 运算符或 format! 宏进行拼接”中讨论），所以你可以传递一个包含 `{}` 占位符以及要放入这些占位符的值的格式字符串。自定义消息对于记录断言的含义很有用；当测试失败时，你将能更好地了解代码出了什么问题。

例如，假设我们有一个按名字向人们打招呼的函数，并且我们想要测试我们传递给该函数的名字是否出现在输出中：

文件名：`src/lib.rs`

```rust
pub fn greeting(name: &str) -> String {
    format!("Hello {name}!")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn greeting_contains_name() {
        let result = greeting("Carol");
        assert!(result.contains("Carol"));
    }
}
```

这个程序的要求尚未确定，并且我们很确定问候语开头的 `Hello` 文本将会改变。我们决定在需求改变时不必更新测试，所以我们不检查与 `greeting` 函数返回值的精确相等性，而是只断言输出包含输入参数的文本。

现在让我们通过将 `greeting` 改为不包含 `name` 来在这段代码中引入一个错误，看看默认的测试失败是什么样的：

```rust
pub fn greeting(name: &str) -> String {
    String::from("Hello!")
}
```

运行这个测试会产生以下结果：

    running 1 test
    test tests::greeting_contains_name... FAILED

    failures:

    ---- tests::greeting_contains_name stdout ----
    thread'main' panicked at 'assertion failed:
    result.contains(\"Carol\")', src/lib.rs:12:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace


    failures:
        tests::greeting_contains_name

这个结果只是表明断言失败了以及断言在第几行。一个更有用的失败消息会打印 `greeting` 函数返回的值。让我们添加一条自定义失败消息，它由一个格式字符串组成，其中的占位符用我们从 `greeting` 函数实际得到的值填充：

    #[test]
    fn greeting_contains_name() {
        let result = greeting("Carol");
        assert!(
            result.contains("Carol"),
            "Greeting did not contain name, value was `{result}`"
        );
    }

现在当我们运行测试时，我们将得到一个更有信息量的错误消息：

    ---- tests::greeting_contains_name stdout ----
    thread'main' panicked at 'Greeting did not contain name, value
    was `Hello!`', src/lib.rs:12:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace

我们可以在测试输出中看到我们实际得到的值，这将帮助我们调试实际发生了什么，而不是我们期望发生什么。
