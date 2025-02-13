# 查看更改差异

作为一名开发者，你可能想要查看暂存或未暂存的更改与上次提交之间的差异。当你想要在提交更改之前检查这些更改，或者想要查看自上次提交以来所做的更改时，这会很有用。

## 任务

为了演示如何查看更改差异，我们将使用 `git-playground` 仓库。假设你对 `README.md` 文件做了一些更改，并想要查看这些更改与上次提交之间的差异。

1. 打开你的终端，并导航到 `git-playground` 目录。
2. 查看未暂存更改与上次提交之间的差异。
3. 查看暂存更改与上次提交之间的差异。

这是完成步骤 2 的结果：

```
diff --git a/file1.txt b/file1.txt
index bfccc4a..ee23125 100644
--- a/file1.txt
+++ b/file1.txt
@@ -1 +1,2 @@
 This is file1.
+hello,labex
```

这是完成步骤 3 的结果：

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
