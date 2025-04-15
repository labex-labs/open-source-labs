# 除非特别请求，否则忽略某些测试

有时，一些特定的测试执行起来可能非常耗时，所以你可能希望在大多数 `cargo test` 运行期间排除它们。你可以使用 `ignore` 属性来注释这些耗时的测试，而不是将所有你想要运行的测试都作为参数列出，如下所示：

文件名：`src/lib.rs`

```rust
#[test]
fn it_works() {
    let result = 2 + 2;
    assert_eq!(result, 4);
}

#[test]
#[ignore]
fn expensive_test() {
    // 运行耗时一小时的代码
}
```

在 `#[test]` 之后，我们在想要排除的测试上添加 `#[ignore]` 行。现在当我们运行测试时，`it_works` 会运行，但 `expensive_test` 不会：

```bash
[object Object]
```

`expensive_test` 函数被列为 `ignored`。如果我们只想运行被忽略的测试，可以使用 `cargo test -- --ignored`：

```bash
[object Object]
```

通过控制运行哪些测试，你可以确保 `cargo test` 的结果能快速返回。当你到了检查被忽略测试结果的阶段，并且有时间等待结果时，可以改为运行 `cargo test -- --ignored`。如果你想运行所有测试，无论它们是否被忽略，可以运行 `cargo test -- --include-ignored`。
