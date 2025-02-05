# 筛选以运行多个测试

我们可以指定测试名称的一部分，任何名称与该值匹配的测试都将运行。例如，因为我们的两个测试名称中包含 `add`，所以我们可以通过运行 `cargo test add` 来运行这两个测试：

```bash
$ cargo test add
   Compiling adder v0.1.0 (file:///projects/adder)
    Finished test [unoptimized + debuginfo] target(s) in 0.61s
     Running unittests src/lib.rs (target/debug/deps/adder-
92948b65e88960b4)

running 2 tests
test tests::add_three_and_two... ok
test tests::add_two_and_two... ok

test result: ok. 2 passed; 0 failed; 0 ignored; 0 measured; 1
filtered out; finished in 0.00s
```

此命令运行了所有名称中包含 `add` 的测试，并筛选掉了名为 `one_hundred` 的测试。还要注意，测试所在的模块会成为测试名称的一部分，所以我们可以通过按模块名称进行筛选来运行模块中的所有测试。
