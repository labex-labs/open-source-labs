# 运行单个测试

我们可以将任何测试函数的名称传递给 `cargo test`，以仅运行该测试：

```bash
$ cargo test one_hundred
   Compiling adder v0.1.0 (file:///projects/adder)
    Finished test [unoptimized + debuginfo] target(s) in 0.69s
     Running unittests src/lib.rs (target/debug/deps/adder-
92948b65e88960b4)

running 1 test
test tests::one_hundred... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 2
filtered out; finished in 0.00s
```

只有名为 `one_hundred` 的测试运行了；其他两个测试与该名称不匹配。测试输出在结尾处显示 `2 filtered out`，让我们知道还有更多测试未运行。

我们不能以这种方式指定多个测试的名称；传递给 `cargo test` 的第一个值将是唯一被使用的。但是有一种方法可以运行多个测试。
