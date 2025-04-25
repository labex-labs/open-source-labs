# 集成测试中的子模块

随着你添加更多的集成测试，你可能想要在 `tests` 目录中创建更多文件来帮助组织它们；例如，你可以根据测试的功能将测试函数分组。如前所述，`tests` 目录中的每个文件都作为一个独立的包进行编译，这对于创建单独的作用域以更紧密地模仿最终用户使用你的包的方式很有用。然而，这意味着 `tests` 目录中的文件与 `src` 中的文件行为不同，正如你在第 7 章中学到的关于如何将代码分离到模块和文件中的内容。

当你有一组辅助函数要在多个集成测试文件中使用，并且尝试按照“将模块分离到不同文件”中的步骤将它们提取到一个公共模块中时，`tests` 目录文件的不同行为最为明显。例如，如果我们创建 `tests/common.rs` 并在其中放置一个名为 `setup` 的函数，我们可以在 `setup` 中添加一些我们希望从多个测试文件中的多个测试函数调用的代码：

文件名：`tests/common.rs`

```rust
pub fn setup() {
    // 特定于你的库的测试的设置代码将放在这里
}
```

当我们再次运行测试时，我们会在测试输出中看到 `common.rs` 文件的一个新部分，即使这个文件不包含任何测试函数，而且我们也没有从任何地方调用 `setup` 函数：

    running 1 test
    test tests::internal... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

         Running tests/common.rs (target/debug/deps/common-
    92948b65e88960b4)

    running 0 tests

    test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

         Running tests/integration_test.rs
    (target/debug/deps/integration_test-92948b65e88960b4)

    running 1 test
    test it_adds_two... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

       Doc-tests adder

    running 0 tests

    test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

让 `common` 在测试结果中显示为 `running 0 tests` 并不是我们想要的。我们只是想与其他集成测试文件共享一些代码。为了避免 `common` 出现在测试输出中，我们将创建 `_tests/common/mod.rs`，而不是创建 `tests/common.rs`。项目目录现在看起来像这样：

    ├── Cargo.lock
    ├── Cargo.toml
    ├── src
    │   └── lib.rs
    └── tests
        ├── common
        │   └── mod.rs
        └── integration_test.rs

这是 Rust 也理解的旧命名约定，我们在“备用文件路径”中提到过。以这种方式命名文件会告诉 Rust 不要将 `common` 模块视为集成测试文件。当我们将 `setup` 函数代码移动到 `tests/common/mod.rs` 并删除 `tests/common.rs` 文件时，测试输出中的该部分将不再出现。`tests` 目录子目录中的文件不会作为单独的包进行编译，也不会在测试输出中有相应部分。

在我们创建了 `tests/common/mod.rs` 之后，我们可以从任何集成测试文件中将其作为一个模块使用。以下是在 `tests/integration_test.rs` 中从 `it_adds_two` 测试调用 `setup` 函数的示例：

文件名：`tests/integration_test.rs`

```rust
use adder;

mod common;

#[test]
fn it_adds_two() {
    common::setup();
    assert_eq!(4, adder::add_two(2));
}
```

请注意，`mod common;` 声明与我们在清单 7-21 中演示的模块声明相同。然后，在测试函数中，我们可以调用 `common::setup()` 函数。
