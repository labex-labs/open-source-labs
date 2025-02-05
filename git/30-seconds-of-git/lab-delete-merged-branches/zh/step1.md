# 删除已合并的分支

你的任务是删除所有已合并到 `https://github.com/labex-labs/git-playground` 仓库的 `master` 分支中的本地分支。

1. 切换到仓库目录：

```shell
cd git-playground
```

2. 列出所有已合并到 `master` 的本地分支：

```shell
git branch --merged
```

输出：

```
* master
  new-branch
  new-branch-1
  new-branch-2
  new-branch-3
```

3. 删除所有已合并的分支：

```shell
git branch --merged master | awk '!/^[ *]*$/ &&!/master/ {print $1}' | xargs git branch -d
```

4. 再次列出所有分支：

```shell
git branch
```

这是最终结果：

```
* master
```
