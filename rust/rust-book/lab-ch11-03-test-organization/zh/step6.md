# “tests” 目录

我们在项目目录的顶层，即 `src` 旁边创建一个 `tests` 目录。Cargo 知道要在这个目录中查找集成测试文件。然后我们可以根据需要创建任意数量的测试文件，Cargo 会将每个文件作为一个独立的包进行编译。

让我们创建一个集成测试。假设 `src/lib.rs` 文件中仍然保留清单 11-12 中的代码，创建一个 `tests` 目录，并创建一个名为 `integration_test.rs` 的新文件。你的目录结构应该如下所示：

    adder
    ├── Cargo.lock
    ├── Cargo.toml
    ├── src
    │   └── lib.rs
    └── tests
        └── integration_test.rs

将清单 11-13 中的代码输入到 `integration_test.rs` 文件中。

文件名：`tests/integration_test.rs`

```rust
use adder;

#[test]
fn it_adds_two() {
    assert_eq!(4, adder::add_two(2));
}
```

清单 11-13：对 `adder` 包中一个函数的集成测试

`tests` 目录中的每个文件都是一个独立的包，所以我们需要将我们的库引入到每个测试包的作用域中。因此，我们在代码顶部添加 `use adder;`，这在单元测试中是不需要的。

我们不需要用 `#[cfg(test)]` 注解 `tests/integration_test.rs` 中的任何代码。Cargo 对 `tests` 目录有特殊处理，只有当我们运行 `cargo test` 时，才会编译这个目录中的文件。现在运行 `cargo test`：

```bash
$ cargo test
   Compiling adder v0.1.0 (file:///projects/adder)
    Finished test [unoptimized + debuginfo] target(s) in 1.31s
     Running unittests src/lib.rs (target/debug/deps/adder-
1082c4b063a8fbe6)

1 running 1 test
test tests::internal... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
filtered out; finished in 0.00s

   2 Running tests/integration_test.rs
(target/debug/deps/integration_test-1082c4b063a8fbe6)

running 1 test
3 test it_adds_two... ok

4 test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
filtered out; finished in 0.00s

   Doc-tests adder

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0
filtered out; finished in 0.00s
```

输出的三个部分包括单元测试、集成测试和文档测试。请注意，如果某一部分中的任何测试失败，后续部分将不会运行。例如，如果一个单元测试失败，那么集成测试和文档测试将不会有任何输出，因为只有在所有单元测试都通过的情况下，这些测试才会运行。

单元测试的第一部分 \[1\] 与我们之前看到的相同：每个单元测试一行（我们在清单 11-12 中添加了一个名为 `internal` 的测试），然后是单元测试的总结行。

集成测试部分以 `Running tests/integration_test.rs` 这一行开始 \[2\]。接下来，在该集成测试中的每个测试函数都有一行 \[3\]，并且在 `Doc-tests adder` 部分开始之前，有一行是集成测试结果的总结行 \[4\]。

每个集成测试文件都有自己的部分，所以如果我们在 `tests` 目录中添加更多文件，将会有更多的集成测试部分。

我们仍然可以通过将测试函数的名称作为参数传递给 `cargo test` 来运行特定的集成测试函数。要运行特定集成测试文件中的所有测试，使用 `cargo test` 的 `--test` 参数，后跟文件名：

```bash
$ cargo test --test integration_test
    Finished test [unoptimized + debuginfo] target(s) in 0.64s
     Running tests/integration_test.rs
(target/debug/deps/integration_test-82e7799c1bc62298)

running 1 test
test it_adds_two... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
filtered out; finished in 0.00s
```

此命令仅运行 `integration_test.rs` 文件中的测试。
