# 向工作区添加测试

作为另一项改进，让我们在 `add_one` 板条箱中添加对 `add_one::add_one` 函数的测试：

文件名：`add_one/src/lib.rs`

```rust
pub fn add_one(x: i32) -> i32 {
    x + 1
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        assert_eq!(3, add_one(2));
    }
}
```

现在在顶层的 `add` 目录中运行 `cargo test`。在像这样构建的工作区中运行 `cargo test` 将运行工作区中所有板条箱的测试：

```bash
$ cargo test
   Compiling add_one v0.1.0 (file:///projects/add/add_one)
   Compiling adder v0.1.0 (file:///projects/add/adder)
    Finished test [unoptimized + debuginfo] target(s) in 0.27s
     Running unittests src/lib.rs (target/debug/deps/add_one-f0253159197f7841)

running 1 test
test tests::it_works... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s

     Running unittests src/main.rs (target/debug/deps/adder-49979ff40686fa8e)

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s

   Doc-tests add_one

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s
```

输出的第一部分表明 `add_one` 板条箱中的 `it_works` 测试通过了。下一部分表明在 `adder` 板条箱中未找到测试，最后一部分表明在 `add_one` 板条箱中未找到文档测试。

我们还可以通过使用 `-p` 标志并指定要测试的板条箱名称，从顶层目录为工作区中的一个特定板条箱运行测试：

```bash
$ cargo test -p add_one
    Finished test [unoptimized + debuginfo] target(s) in 0.00s
     Running unittests src/lib.rs (target/debug/deps/add_one-b3235fea9a156f74)

running 1 test
test tests::it_works... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s

   Doc-tests add_one

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s
```

此输出表明 `cargo test` 仅运行了 `add_one` 板条箱的测试，而未运行 `adder` 板条箱的测试。

如果你将工作区中的板条箱发布到 *https://crates.io*，工作区中的每个板条箱都需要单独发布。与 `cargo test` 类似，我们可以通过使用 `-p` 标志并指定要发布的板条箱名称来发布工作区中的特定板条箱。

作为额外的练习，以与添加 `add_one` 板条箱类似的方式向此工作区添加一个 `add_two` 板条箱！

随着你的项目不断发展，可以考虑使用工作区：与一大块代码相比，它提供了更易于理解、更小的独立组件。此外，如果多个板条箱经常同时更改，将它们保存在工作区中可以使板条箱之间的协调更加容易。
