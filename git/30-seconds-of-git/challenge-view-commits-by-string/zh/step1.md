# 查找操作特定字符串的提交记录

作为一名开发者，你可能需要在代码库中查找所有修改了特定字符串的提交记录。例如，你可能想要找出所有添加或删除了特定函数名或变量的提交记录。这在调试问题或追踪错误源头时会很有用。

## 任务

假设你正在处理一个托管在 GitHub 上名为 `git-playground` 的项目。你想要找出在 `README.md` 文件中修改了字符串“Git Playground”的所有提交记录。以下是操作方法：

1. 导航到仓库目录。
2. 找出在 `README.md` 文件中修改了字符串“Git Playground”的所有提交记录，并使用箭头键浏览提交记录列表。按 <kbd>Q</kbd> 键退出日志。

Git 将输出在 `README.md` 文件中修改了字符串“Git Playground”的所有提交记录列表：

```shell
commit b00b9374a7c549d1af111aa777fdcc868d8a2a01
Author: Hang <huhuhang@gmail.com>
Date:   Wed Apr 26 14:16:00 2023 +0800

    Initial commit
```
