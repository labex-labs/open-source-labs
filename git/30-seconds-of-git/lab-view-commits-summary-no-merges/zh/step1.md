# 查看排除合并提交后的提交简短摘要

你一直在与其他几位开发人员共同处理一个项目，你想要查看对存储库所做的所有提交的摘要。但是，你不想看到合并提交，因为它们不包含对代码的任何实际更改。你如何查看排除合并提交后的所有提交的摘要呢？

对于本实验，让我们使用来自 `https://github.com/labex-labs/git-playground` 的存储库。

1. 克隆存储库，导航到该目录并配置身份：

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "你的用户名"
git config --global user.email "你的邮箱"
```

2. 创建并切换到名为 `feature1` 的分支，创建一个名为 `file.txt` 的文件，并在其中写入 `feature 1`，将其添加到暂存区并使用消息“添加功能 1”提交：

```shell
git checkout -b feature1
echo "Feature 1" >> file.txt
git add.
git commit -m "添加功能 1"
```

3. 切换回 `master` 分支，合并 `feature1` 分支，禁用快进合并，保存并退出而不更改文本：

```shell
git checkout master
git merge --no-ff feature1
```

4. 查看排除合并提交后的所有提交的简短摘要：

```shell
git log --oneline --no-merges
```

这将输出对存储库所做的所有提交的列表，不包括任何合并提交。输出将如下所示：

```shell
430b986 (feature1) 添加功能 1
d22f46b (origin/master, origin/HEAD) 添加了 file2.txt
cf80005 添加了 file1.txt
b00b937 初始提交
```
