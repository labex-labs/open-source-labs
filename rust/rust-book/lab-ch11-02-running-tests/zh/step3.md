# 显示函数输出

默认情况下，如果一个测试通过，Rust 的测试库会捕获所有输出到标准输出的内容。例如，如果我们在一个测试中调用 `println!` 并且测试通过，我们不会在终端中看到 `println!` 的输出；我们只会看到表明测试通过的那一行。如果一个测试失败，我们会在失败消息的其余部分中看到输出到标准输出的任何内容。

作为一个例子，清单 11-10 中有一个简单的函数，它会打印其参数的值并返回 10，还有一个通过的测试和一个失败的测试。

文件名：`src/lib.rs`

```rust
fn prints_and_returns_10(a: i32) -> i32 {
    println!("I got the value {a}");
    10
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn this_test_will_pass() {
        let value = prints_and_returns_10(4);
        assert_eq!(10, value);
    }

    #[test]
    fn this_test_will_fail() {
        let value = prints_and_returns_10(8);
        assert_eq!(5, value);
    }
}
```

清单 11-10：对调用 `println!` 的函数进行的测试

当我们使用 `cargo test` 运行这些测试时，我们会看到以下输出：

    running 2 tests
    test tests::this_test_will_pass... ok
    test tests::this_test_will_fail... FAILED

    failures:

    ---- tests::this_test_will_fail stdout ----
    1 I got the value 8
    thread 'main' panicked at 'assertion failed: `(left == right)`
      left: `5`,
     right: `10`', src/lib.rs:19:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace

    failures:
        tests::this_test_will_fail

    test result: FAILED. 1 passed; 1 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

请注意，在这个输出中，我们在任何地方都看不到通过的测试运行时打印的 `I got the value 4`。该输出已被捕获。失败的测试的输出 `I got the value 8` \[1\] 出现在测试总结输出的部分中，该部分还显示了测试失败的原因。

如果我们也想看到通过的测试的打印值，我们可以告诉 Rust 使用 `--show-output` 来显示成功测试的输出：

```bash
cargo test -- --show-output
```

当我们使用 `--show-output` 标志再次运行清单 11-10 中的测试时，我们会看到以下输出：

    running 2 tests
    test tests::this_test_will_pass... ok
    test tests::this_test_will_fail... FAILED

    successes:

    ---- tests::this_test_will_pass stdout ----
    I got the value 4


    successes:
        tests::this_test_will_pass

    failures:

    ---- tests::this_test_will_fail stdout ----
    I got the value 8
    thread 'main' panicked at 'assertion failed: `(left == right)`
      left: `5`,
     right: `10`', src/lib.rs:19:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace

    failures:
        tests::this_test_will_fail

    test result: FAILED. 1 passed; 1 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s
