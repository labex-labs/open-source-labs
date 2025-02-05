# 故障排除

要检查 Rust 是否安装正确，打开一个**新的 shell** 并输入以下命令：

```bash
# 首先打开一个新的终端！
rustc --version
```

你应该会看到已发布的最新稳定版本的版本号、提交哈希和提交日期，格式如下：

```bash
rustc x.y.z (abcabcabc yyyy-mm-dd)
```

如果你看到了这些信息，说明你已成功安装 Rust！如果你没有看到这些信息，请按如下方式检查 Rust 是否在你的 `%PATH%` 系统变量中。

在 Linux 中，使用：

```bash
echo $PATH
```

如果上述所有操作都正确，但 Rust 仍然无法正常工作，你可以通过多种途径获得帮助。在社区页面 *https://www.rust-lang.org/community* 上了解如何与其他 Rustaceans（我们给自己起的一个有趣昵称）取得联系。
