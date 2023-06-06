# Git Challenge: Rewind Commits

## Problem

As a developer, you have been working on a project and have made several commits. However, you realize that the last few commits contain errors and you need to go back to a previous version of your code. You need to use Git to rewind your commits and get back to the previous version of your code.

## Example

To complete this experiment, you will use the Git repository `git-playground` from your GitHub account, which comes from a fork of `https://github.com/labex-labs/git-playground.git`.

1. Clone the repository to your local machine.
2. Create a new branch called `rewind-commits`.
3. Create a new file called `hello.py` with the text "Hello, World" and add it to the Git staging area. Then commit the changes with the message "Add hello.py file".
4. Update the contents of the file `hello.py` to "Hello, Git" and add the changes to the Git staging area. Then use the "Update hello.py file" message to commit the changes.
5. Realize that the last few commits contain errors and you need to go back to the previous version of your code.
6. Use Git to rewind your commits by 1.
7. Verify that you have successfully rewound your commits by checking the code in your working directory.
8. Push your changes to the `rewind-commits` branch.

This is the final result:

![result](./assets/challenge-rewind-n-commits-step1-1.png)


当然，下面是使用 Git 存储库 `https://github.com/labex-labs/git-playground` 完成挑战的具体示例：

1. 将存储库克隆到本地计算机：

```
git clone https://github.com/labex-labs/git-playground.git
cd git-playground
```

2. 创建名为 `rewind-commits` 的新分支：

```
git checkout -b rewind-commits
```

3. Create a new file called `hello.py` with the text "Hello, World" and add it to the Git staging area. Then commit the changes with the message "Add hello.py file".
4. Create a new file called hello.py with the text "Hello, World" and add it to the Git staging area. Then commit the changes with the message "Add hello.py file".
5. Update the contents of the file `hello.py` to "Hello, Git" and add the changes to the Git staging area. Then use the "Update hello.py file" message to commit the changes.

5. 意识到最近的几个提交包含错误，需要返回到代码的上一个版本。

6. 使用 Git 将提交回退 2 次：

```
git reset HEAD~1 --hard
```

这将删除最后两个提交并将代码恢复到在进行最后两个提交之前的状态。

7. 通过检查工作目录中的代码来验证是否成功回退了提交：

```
cat hello.py
```

这应该将 `hello.py` 文件的内容输出为 `print('Hello, World!')`，这是在进行最后两个提交之前的内容。

8. 将更改推送到 `rewind-commits` 分支：

```
git push --force origin rewind-commits
```

这将强制推送 `rewind-commits` 分支到远程存储库，覆盖历史记录与新提交。请注意，由于我们回退了提交，因此远程存储库的历史记录与本地存储库不同，因此需要使用 `--force`。