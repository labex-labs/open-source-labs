# 从另一个分支复制文件

你正在处理一个位于 Git 仓库 `https://github.com/labex-labs/git-playground.git` 中的项目。你有两个分支，分别名为 `feature-1` 和 `feature-2`。你需要将 `hello.txt` 文件从 `feature-1` 分支复制到 `feature-2` 分支。

## 任务

1. 导航到该目录并配置身份。
2. 创建并切换到 `feature-1` 分支，创建一个名为 `hello.txt` 的文本文件，并在其中写入字符串 "hello,world"，然后使用提交消息 "add hello.txt" 提交该文件。
3. 切换到 `master` 分支后，创建并切换到 `feature-2` 分支。
4. 将 `hello.txt` 文件从 `feature-1` 分支复制到 `feature-2` 分支，并使用提交消息 "copy hello.txt" 提交。
5. 验证 `hello.txt` 文件是否已复制到 `feature-2` 分支。

你应该在 `feature-2` 分支的文件列表中看到 `hello.txt` 文件：

```
-rw-r--r-- 1 labex labex 15 Jul 12 22:43 file1.txt
-rw-r--r-- 1 labex labex 15 Jul 12 22:43 file2.txt
-rw-r--r-- 1 labex labex 12 Jul 12 22:50 hello.txt
-rw-r--r-- 1 labex labex 32 Jul 12 22:43 README.md
```
