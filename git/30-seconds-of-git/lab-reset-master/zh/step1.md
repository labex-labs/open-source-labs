# 将本地主分支重置为与远程分支匹配

你一直在处理一个项目，并对本地的 `master` 分支进行了更改。然而，你意识到远程 `master` 分支已经更新了一些你本地分支中没有的新更改。你需要将本地 `master` 分支重置为与远程分支匹配。

1. 切换到 `master` 分支：
   ```shell
   git checkout master
   ```
2. 从远程获取最新更新：
   ```shell
   git fetch origin
   ```
3. 查看当前分支的提交历史：
   ```shell
   git log
   ```
4. 将本地 `master` 分支重置为与远程分支匹配：
   ```shell
   git reset --hard origin/master
   ```
5. 验证本地 `master` 分支现在是否与远程 `master` 分支同步：
   ```shell
   git log
   ```

这是最终结果：

```shell

```
