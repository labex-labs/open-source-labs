# 集成测试

单元测试每次单独测试一个模块：它们规模小，并且可以测试私有代码。集成测试位于你的包外部，并且与其他任何代码一样，仅使用其公共接口。其目的是测试你的库的多个部分能否正确协同工作。

Cargo 在 `src` 旁边的 `tests` 目录中查找集成测试。

文件 `src/lib.rs`：

```rust
// 在名为 `adder` 的包中定义此函数。
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}
```

测试文件：`tests/integration_test.rs`：

```rust
#[test]
fn test_add() {
    assert_eq!(adder::add(3, 2), 5);
}
```

使用 `cargo test` 命令运行测试：

```shell
$ cargo test
running 0 tests

test result: ok. 0 passed
0 failed
0 ignored
0 measured
0 filtered out

Running target/debug/deps/integration_test-bcd60824f5fbfe19

running 1 test
test test_add... ok

test result: ok. 1 passed
0 failed
0 ignored
0 measured
0 filtered out

Doc-tests adder

running 0 tests

test result: ok. 0 passed
0 failed
0 ignored
0 measured
0 filtered out
```

`tests` 目录中的每个 Rust 源文件都作为一个单独的包进行编译。为了在集成测试之间共享一些代码，我们可以创建一个具有公共函数的模块，并在测试中导入和使用它。

文件 `tests/common/mod.rs`：

```rust
pub fn setup() {
    // 一些设置代码，比如创建所需的文件/目录、启动
    // 服务器等。
}
```

测试文件：`tests/integration_test.rs`

```rust
// 导入公共模块。
mod common;

#[test]
fn test_add() {
    // 使用公共代码。
    common::setup();
    assert_eq!(adder::add(3, 2), 5);
}
```

将模块创建为 `tests/common.rs` 也可行，但不推荐，因为测试运行器会将该文件视为一个测试包，并尝试在其中运行测试。
