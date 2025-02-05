# 发布到 Crates.io

既然你已经创建了账户、保存了 API 令牌、为你的 crate 选择了名称并指定了所需的元数据，那么你就准备好发布了！发布一个 crate 会将特定版本上传到 *https://crates.io* 供其他人使用。

要小心，因为发布是 **永久性的**。版本永远不能被覆盖，代码也不能被删除。Crates.io 的一个主要目标是充当代码的永久存档，以便所有依赖于 *https://crates.io* 上 crate 的项目构建能够继续正常工作。允许删除版本会使实现该目标变得不可能。然而，你可以发布的 crate 版本数量没有限制。

再次运行 `cargo publish` 命令。现在它应该会成功：

```bash
$ cargo publish
    Updating crates.io index
   Packaging guessing_game v0.1.0 (file:///projects/guessing_game)
   Verifying guessing_game v0.1.0 (file:///projects/guessing_game)
   Compiling guessing_game v0.1.0
(file:///projects/guessing_game/target/package/guessing_game-0.1.0)
    Finished dev [unoptimized + debuginfo] target(s) in 0.19s
   Uploading guessing_game v0.1.0 (file:///projects/guessing_game)
```

恭喜！你现在已经与 Rust 社区共享了你的代码，任何人都可以轻松地将你的 crate 添加为他们项目的依赖项。
