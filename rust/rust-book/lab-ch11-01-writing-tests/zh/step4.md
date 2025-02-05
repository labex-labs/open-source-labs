# 使用 `assert_eq!` 和 `assert_ne!` 宏测试相等性

验证功能的一种常见方法是测试被测代码的结果与你期望代码返回的值之间是否相等。你可以通过使用 `assert!` 宏并向其传递一个使用 `==` 运算符的表达式来做到这一点。然而，这是一个非常常见的测试，以至于标准库提供了一对宏——`assert_eq!` 和 `assert_ne!`——来更方便地执行此测试。这些宏分别比较两个参数是否相等或不相等。如果断言失败，它们还会打印这两个值，这使得更容易看出测试失败的 _原因_；相反，`assert!` 宏仅表明它对于 `==` 表达式得到了一个 `false` 值，而不会打印导致该 `false` 值的那些值。

在清单 11 - 7 中，我们编写了一个名为 `add_two` 的函数，它将其参数加 `2`，然后我们使用 `assert_eq!` 宏来测试这个函数。

文件名：`src/lib.rs`

```rust
pub fn add_two(a: i32) -> i32 {
    a + 2
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_adds_two() {
        assert_eq!(4, add_two(2));
    }
}
```

清单 11 - 7：使用 `assert_eq!` 宏测试 `add_two` 函数

让我们检查一下它是否通过！

    running 1 test
    test tests::it_adds_two... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

我们将 `4` 作为参数传递给 `assert_eq!`，它等于调用 `add_two(2)` 的结果。这个测试的那一行是 `test tests::it_adds_two... ok`，`ok` 文本表明我们的测试通过了！

让我们在代码中引入一个错误，看看 `assert_eq!` 失败时是什么样子。将 `add_two` 函数的实现改为加 `3`：

```rust
pub fn add_two(a: i32) -> i32 {
    a + 3
}
```

再次运行测试：

    running 1 test
    test tests::it_adds_two... FAILED

    failures:

    ---- tests::it_adds_two stdout ----
    1 thread'main' panicked at 'assertion failed: `(left == right)`
    2   left: `4`,
    3  right: `5`', src/lib.rs:11:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace

    failures:
        tests::it_adds_two

    test result: FAILED. 0 passed; 1 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

我们的测试发现了这个错误！`it_adds_two` 测试失败了，并且消息告诉我们失败的断言是 `assertion failed: `(left == right)\``\[1\] 以及`left`\[2\] 和`right` \[3\] 的值是什么。这个消息有助于我们开始调试：`left`参数是`4`，但 `right`参数，也就是我们调用`add_two(2)`得到的值，是`5`。你可以想象当我们有很多测试在进行时，这会特别有帮助。

请注意，在一些语言和测试框架中，相等性断言函数的参数被称为 `expected` 和 `actual`，并且我们指定参数的顺序很重要。然而，在 Rust 中，它们被称为 `left` 和 `right`，并且我们指定预期值和代码产生的值的顺序并不重要。我们可以将这个测试中的断言写成 `assert_eq!(add_two(2), 4)`，这将导致显示相同失败消息 `assertion failed: `(left == right)\`` 的结果。

`assert_ne!` 宏在我们给它的两个值不相等时会通过，而在它们相等时会失败。这个宏在我们不确定一个值 _会_ 是什么，但我们知道这个值肯定 _不应该_ 是什么的情况下最有用。例如，如果我们正在测试一个保证会以某种方式改变其输入的函数，但是输入被改变的方式取决于我们运行测试的星期几，那么最好断言的可能是函数的输出不等于输入。

在底层，`assert_eq!` 和 `assert_ne!` 宏分别使用运算符 `==` 和 `!=`。当断言失败时，这些宏使用调试格式打印它们的参数，这意味着被比较的值必须实现 `PartialEq` 和 `Debug` 特性。所有基本类型和大多数标准库类型都实现了这些特性。对于你自己定义的结构体和枚举，你需要实现 `PartialEq` 来断言这些类型的相等性。当断言失败时，你还需要实现 `Debug` 来打印这些值。如清单 5 - 12 中所述，因为这两个特性都是可派生特性，所以这通常就像在你的结构体或枚举定义中添加 `#[derive(PartialEq, Debug)]` 注解一样简单。有关这些和其他可派生特性的更多详细信息，请参阅附录 C。
