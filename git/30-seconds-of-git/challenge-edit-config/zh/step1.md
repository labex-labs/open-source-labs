# 编辑 Git 配置文件

作为一名开发者，你可能需要修改 Git 配置文件以定制 Git 的行为。Git 配置文件是一个纯文本文件，它以键值对的形式包含各种设置。该文件可以使用任何文本编辑器进行编辑，但 Git 提供了一个内置的文本编辑器，可用于修改配置文件。

## 任务

在这个示例中，我们将使用名为 `https://github.com/labex-labs/git-playground` 目录下的 Git 仓库。

1. 打开终端并导航到 Git 仓库目录。
2. 使用 Git 文本编辑器打开 Git 配置文件。
3. 修改设置，将用户名设置为 `labex_git`，用户邮箱设置为 `labex_git@example.com`。
4. 完成必要的更改后，按下 <kbd>Esc</kbd> 键并输入 <kbd>:wq</kbd> 命令，然后按下 <kbd>Enter</kbd> 键保存更改并退出编辑器。

这是完成后的结果：

```shell
# 这是 Git 的 per-user 配置文件。
[user]
name = labex_git
email = labex_git@example.com
# 请调整并取消注释以下行：
#   name =
#   email = labex@64b8c76af840a200973e9d16.(none)
```
