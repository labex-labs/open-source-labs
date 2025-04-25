# 查看排除合并提交后的提交简短摘要

你一直在与其他几位开发人员共同处理一个项目，你想查看对存储库所做的所有提交的摘要。但是，你不想看到合并提交，因为它们不包含对代码的任何实际更改。你如何查看排除合并提交后的所有提交的摘要？

## 任务

对于这个挑战，让我们使用来自 `https://github.com/labex-labs/git-playground` 的存储库。

1. 导航到该目录并配置身份。
2. 创建并切换到名为 `feature1` 的分支，创建一个名为 `file.txt` 的文件，并在其中写入“feature 1”，将其添加到暂存区并使用消息“Add feature 1”提交。
3. 切换回 `master` 分支，合并 `feature1` 分支，禁用前向合并，保存并退出，不更改文本。
4. 查看排除合并提交后的所有提交的简短摘要。

这将输出对存储库所做的所有提交的列表，不包括任何合并提交。输出将如下所示：

```shell
430b986 (feature1) Add feature 1
d22f46b (origin/master, origin/HEAD) Added file2.txt
cf80005 Added file1.txt
b00b937 Initial commit
```
