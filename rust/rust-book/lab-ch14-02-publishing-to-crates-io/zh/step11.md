# 使用 cargo yank 从 Crates.io 弃用版本

虽然你不能删除 crate 的先前版本，但你可以阻止未来的任何项目将它们作为新的依赖项添加。当 crate 版本由于某种原因出现问题时，这很有用。在这种情况下，Cargo 支持弃用 crate 版本。

**弃用** 一个版本可防止新项目依赖该版本，同时允许所有依赖它的现有项目继续使用。本质上，弃用意味着所有包含 _Cargo.lock_ 的项目不会中断，并且未来生成的任何 _Cargo.lock_ 文件都不会使用被弃用的版本。

要弃用 crate 的某个版本，在你之前发布的 crate 所在目录中，运行 `cargo yank` 并指定你要弃用的版本。例如，如果我们发布了一个名为 `guessing_game` 的 crate 版本 1.0.1，并且我们想要弃用它，在 `guessing_game` 的项目目录中我们会运行：

```bash
$ cargo yank --vers 1.0.1
Updating crates.io index
Yank guessing_game@1.0.1
```

通过在命令中添加 `--undo`，你还可以撤销弃用并允许项目再次开始依赖该版本：

```bash
$ cargo yank --vers 1.0.1 --undo
Updating crates.io index
Unyank guessing_game@1.0.1
```

弃用 **不会** 删除任何代码。例如，它不能删除意外上传的机密信息。如果发生这种情况，你必须立即重置这些机密信息。
