# 创建修正提交

假设你正在和其他几位开发者一起处理一个项目，你发现几天前提交的一个内容中有个小错误。你想修复这个错误，但又不想创建一个新的提交并干扰其他开发者的工作。这时修正提交就派上用场了。通过创建一个修正提交，你可以进行必要的更改而无需创建新的提交，并且在下次变基（rebase）时，修正提交会自动与原始提交合并。

例如，你的任务是将字符串“hello,world”写入`hello.txt`文件，并将其作为一个“修正”提交添加到提交信息为“添加了file1.txt”的提交中，以便在后续的变基操作中能自动合并。

对于这个实验，我们使用来自`https://github.com/labex-labs/git-playground`的仓库。

1. 克隆仓库，进入该目录并配置身份：

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "你的用户名"
git config --global user.email "你的邮箱"
```

2. 创建一个`hello.txt`文件，在其中写入“hello,world”并将其添加到暂存区：

```shell
echo "hello,world" > hello.txt
git add.
```

3. 要创建一个修正提交，你可以使用`git commit --fixup <提交>`命令：

```shell
git commit --fixup cf80005
# 这是提交信息为“添加了file1.txt”的提交的哈希值。
```

这将为指定的提交创建一个修正提交。请注意，在创建修正提交之前，你必须先暂存你的更改。4. 创建修正提交后，你可以使用`git rebase --interactive --autosquash`命令在下次变基时自动将修正提交与原始提交合并。例如：

```shell
git rebase --interactive --autosquash HEAD~3
```

打开交互式编辑器时，你无需更改文本，保存即可退出。这将对最后3次提交执行变基操作，并自动将任何修正提交与其对应的原始提交合并。

这是运行`git show HEAD~1`命令的结果：

```shell
commit 6f0b8bbfac939af197a44ecd287ef84153817e9d
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file1.txt

diff --git a/file1.txt b/file1.txt
new file mode 100644
index 0000000..bfccc4a
--- /dev/null
+++ b/file1.txt
@@ -0,0 +1 @@
+This is file1.
diff --git a/hello.txt b/hello.txt
new file mode 100644
index 0000000..2d832d9
--- /dev/null
+++ b/hello.txt
@@ -0,0 +1 @@
+hello,world
```
