# 手动查找引入错误的提交

你的任务是手动在 `git-playground` 仓库中找到引入错误的提交。该仓库可在 `https://github.com/labex-labs/git-playground` 找到。错误是 `file2.txt` 文件应打印 “This is file2.txt.”，而不是 “This is file2.”。

要完成此实验，你需要使用 `git bisect` 命令在仓库的提交历史中进行二分查找。你需要将提交标记为 “好”（无错误）或 “坏”（有错误），直到你缩小到引入错误的提交。

1. 切换到仓库目录：

```
cd git-playground
```

2. 启动 `git bisect` 进程：

```
git bisect start
```

3. 将当前提交标记为 “坏”：

```
git bisect bad HEAD
```

4. 将带有 “Initial commit” 消息的提交标记为 “好”。Git 将自动为你检出一个新的提交进行测试：

```
git bisect good 3050fc0de
```

Git 将自动为你检出一个新的提交进行测试。5. 如果检出的 `file2.txt` 文件内容与错误不匹配，将其标记为 “好”：

```
cat file2.txt
git bisect good
```

6. 如果检出的 `file2.txt` 文件内容与错误匹配，将其标记为 “坏”：

```
git bisect bad
```

7. 一旦你找到了有错误的提交，重置 `git bisect` 进程：

```
git bisect reset
```

现在你可以检查有错误的提交中的代码更改，以找到错误的根源。

这是测试结果：

```
d22f46ba8c2d4e07d773c5126e9c803933eb5898 是第一个有错误的提交
commit d22f46ba8c2d4e07d773c5126e9c803933eb5898
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt

 file2.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 file2.txt
```
