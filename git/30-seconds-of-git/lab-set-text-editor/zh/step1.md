# 配置 Git 的文本编辑器

对于本实验，我们使用来自 `https://github.com/labex-labs/git-playground` 的仓库。你需要将 Git 使用的文本编辑器配置为你喜欢的编辑器。

1. 克隆 `git-playground` 仓库：

```shell
git clone https://github.com/labex-labs/git-playground
```

2. 进入克隆的仓库并配置身份：

```shell
cd git-playground
git config --global user.name "你的用户名"
git config --global user.email "你的邮箱"
```

3. 配置 Git 使用你喜欢的文本编辑器（在本示例中，我们将使用 vim）：

```shell
git config --global core.editor "vim"
```

4. 对文件进行更改并将其暂存以准备提交：

```shell
echo "Hello, Git" > hello.txt
git add hello.txt
```

5. 提交更改：

```shell
git commit
```

6. 你喜欢的文本编辑器（在本示例中为 vim）应会打开并显示提交消息。写下你的提交消息“Update hello.txt”并保存文件。
7. 关闭文本编辑器。提交将使用你编写的消息进行。

这是最终结果：

```shell
commit 1f19499s5387a1549f1bb5286d3d0a2b993f87e0 (HEAD -> master)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 19:26:57 2023 +0800

    Update hello.txt
```
