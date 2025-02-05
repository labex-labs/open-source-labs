# 查看更改差异

作为一名开发者，你可能想要查看暂存或未暂存的更改与上次提交之间的差异。当你想要在提交更改之前检查这些更改，或者想看看自上次提交以来做了哪些更改时，这会很有用。

为了演示如何查看更改差异，我们将使用 `git-playground` 仓库。假设你对 `README.md` 文件做了一些更改，并想查看这些更改与上次提交之间的差异。

1. 打开终端并导航到 `git-playground` 目录：

```shell
cd git-playground
```

2. 使用 `git diff` 命令查看未暂存的更改与上次提交之间的差异：

```shell
git diff
```

3. 或者，你可以使用 `--staged` 选项查看暂存的更改与上次提交之间的差异：

```shell
git diff --staged
```

这是完成步骤2后的结果：

```
diff --git a/file1.txt b/file1.txt
index bfccc4a..ee23125 100644
--- a/file1.txt
+++ b/file1.txt
@@ -1 +1,2 @@
 This is file1.
+hello,labex
```

这是完成步骤3后的结果：

```
diff --git a/README.md b/README.md
index 0164284..f47591b 100644
--- a/README.md
+++ b/README.md
@@ -1,2 +1,3 @@
 # git-playground
 Git Playground
+hello,world
```
