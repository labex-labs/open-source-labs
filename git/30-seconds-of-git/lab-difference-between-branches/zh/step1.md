# 分支之间的差异

你一直在和团队一起处理一个项目，并且创建了一个名为 `feature-1` 的分支来处理一项新功能。你的同事也创建了一个名为 `feature-2` 的分支来处理另一项不同的功能。你想要比较这两个分支之间的更改，看看添加了什么、修改了什么或删除了什么。你该如何查看这两个分支之间的差异呢？

假设你的 GitHub 账户从 `https://github.com/labex-labs/git-playground.git` 克隆了一个名为 `git-playground` 的仓库。请按照以下步骤操作：

1. 使用命令 `cd git-playground` 切换到仓库目录。
2. 使用命令 `git config --global user.name "你的名字"` 和 `git config --global user.email "你的邮箱地址"` 在这个环境中配置你的 GitHub 账户。
3. 使用命令 `git checkout -b feature-1` 创建并切换到 `feature-1` 分支，在 `README.md` 文件中添加 "hello"，将其添加到暂存区并提交，提交消息为 "Add new content to README.md"，使用命令 `echo "hello" >> README.md `、`git add.` 和 `git commit -am "Add new content to README.md"`。
4. 切换回 `master` 分支。
5. 使用命令 `git checkout -b feature-2` 创建并切换到 `feature-2` 分支，在 `index.html` 文件中添加 "world"，将其添加到暂存区并提交，提交消息为 "Update index.html file"，使用命令 `echo "world" > index.htm`、`git add.` 和 `git commit -am "Update index.html file"`。
6. 使用命令 `git diff feature-1..feature-2` 查看这两个分支之间的差异。

输出应该显示 `feature-1` 和 `feature-2` 分支之间的差异。这展示了最终结果的样子：

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
