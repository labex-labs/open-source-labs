# 编辑上一次提交

你刚刚将一些更改提交到了你的 Git 仓库，但你意识到你忘记包含一个文件或者做一个小的修改。你不想仅仅为了这个小修改就创建一个新的提交，但你也不想更改提交消息。你如何在不更改提交消息的情况下编辑上一次提交呢？

为了演示如何编辑上一次提交，让我们使用来自 `https://github.com/labex-labs/git-playground` 的仓库。

1. 克隆仓库，导航到该目录并配置身份：

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "你的用户名"
git config --global user.email "你的邮箱"
```

2. 意识到你忘记包含一个文件或者做一个小的修改。将文本“新内容”添加到 `README.md` 文件的末尾。将任何暂存的更改添加到上一次提交中，而不更改其消息：

```shell
echo "New content" >> README.md
git add README.md
git commit --amend --no-edit
```

3. 验证上一次提交现在是否包含你所做的更改：

```shell
git show HEAD
```

这是最新提交的内容：
![更新后的提交内容显示](../assets/challenge-update-commit-contents.png)
