# 查看已合并的分支

你的任务是打印出名为 `https://github.com/labex-labs/git-playground` 的 Git 仓库中所有已合并的本地分支列表。你需要使用命令 `git branch -a --merged` 来显示已合并分支的列表。获取列表后，你应该能够使用箭头键浏览它，并通过按 <kbd>Q</kbd> 退出。

1. 导航到仓库目录：

```shell
cd git-playground
```

2. 查看已合并分支的列表：

```shell
git branch -a --merged
```

这是最终结果：

```
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/feature-branch
  remotes/origin/master
```
