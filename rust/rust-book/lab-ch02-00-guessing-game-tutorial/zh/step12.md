# 更新包以获取新版本

当你确实想要更新一个包时，Cargo 提供了 `update` 命令，它会忽略 _Cargo.lock_ 文件，并找出 `Cargo.toml` 中符合你指定要求的所有最新版本。然后，Cargo 会将这些版本写入 _Cargo.lock_ 文件。否则，默认情况下，Cargo 只会查找大于 0.8.5 且小于 0.9.0 的版本。如果 `rand` 包发布了 0.8.6 和 0.9.0 这两个新版本，当你运行 `cargo update` 时，你会看到以下内容：

```bash
$ cargo update
Updating crates.io index
Updating rand v0.8.5 - > v0.8.6
```

Cargo 会忽略 0.9.0 版本。此时，你还会注意到 _Cargo.lock_ 文件有变化，表明你现在使用的 `rand` 包版本是 0.8.6。要使用 0.9.0 版本的 `rand` 或 0.9._x_ 系列中的任何版本，你需要将 `Cargo.toml` 文件更新为如下内容：

```rust
[dependencies]
rand = "0.9.0"
```

下次你运行 `cargo build` 时，Cargo 会更新可用包的注册表，并根据你指定的新版本重新评估你对 `rand` 的需求。

关于 Cargo 及其生态系统还有很多内容可说，我们将在第 14 章讨论，但目前，这些就是你需要知道的全部内容。Cargo 使得重用库变得非常容易，所以 Rust 开发者能够编写由多个包组装而成的更小的项目。
