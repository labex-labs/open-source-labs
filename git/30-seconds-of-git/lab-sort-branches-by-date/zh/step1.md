# 按日期对 Git 分支进行排序

你有一个包含多个分支的 Git 仓库，你想按日期对它们进行排序。这将使你能够查看哪些分支最近有更新，哪些没有。按日期对分支进行排序还可以帮助你识别可能需要关注或合并的分支。

对于这个实验，我们使用来自 `https://github.com/labex-labs/git-playground` 的仓库。

1. 将仓库克隆到你的本地机器：

```shell
git clone https://github.com/labex-labs/git-playground
```

2. 导航到仓库目录并配置你的 GitHub 身份：

```shell
cd git-playground
git config --global user.name "你的用户名"
git config --global user.email "你的邮箱"
```

3. 创建一个名为 `one` 的分支，修改代码并提交：

```shell
git checkout -b one
touch hello.txt
git add.
git commit -m "hello.txt"
```

4. 切换到名为 `master` 的分支并创建一个名为 `two` 的分支：

```shell
git checkout master
git checkout -b two
```

5. 现在，要按日期对分支进行排序，请使用以下命令：

```shell
git branch --sort=-committerdate
```

这将显示所有本地分支的列表，并根据它们最后一次提交的日期进行排序。你可以使用箭头键浏览列表，然后按 <kbd>Q</kbd> 退出。

这是最终结果：

![按日期排序的 Git 分支列表](../assets/challenge-sort-branches-by-date.png)
