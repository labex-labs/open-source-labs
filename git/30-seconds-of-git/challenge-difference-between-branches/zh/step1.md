# 分支之间的差异

你一直在和团队一起处理一个项目，并且创建了一个名为 `feature-1` 的分支来处理一个新功能。你的同事也创建了一个名为 `feature-2` 的分支来处理另一个不同的功能。你想要比较这两个分支之间的差异，看看添加、修改或删除了哪些内容。你该如何查看这两个分支之间的差异呢？

## 任务

假设你的 GitHub 账户从 `https://github.com/labex-labs/git-playground.git` 克隆了一个名为 `git-playground` 的仓库。

1. 导航到仓库目录并配置你的 GitHub 身份。
2. 切换到 `feature-1` 分支，并在 `README.md` 文件中添加 "hello"，将其添加到暂存区并提交，提交消息为 "Add new content to README.md"。
3. 切换到 `feature-2` 分支，并在 `index.html` 文件中添加 "world"，将其添加到暂存区并提交，提交消息为 "Update index.html file"。
4. 查看这两个分支之间的差异。

输出应显示 `feature-1` 和 `feature-2` 分支之间的差异。这展示了最终结果的样子：

```shell
diff --git a/README.md b/README.md
index b66215f..0164284 100644
--- a/README.md
+++ b/README.md
@@ -1,3 +1,2 @@
# git-playground
Git Playground
-hello
diff --git a/index.html b/index.html
new file mode 100644
index 0000000..cc628cc
--- /dev/null
+++ b/index.html
@@ -0,0 +1 @@
+world
```
