# 设置默认推送分支名称

将更改推送到远程存储库时，Git 会使用当前本地分支的名称作为远程分支的默认名称。但是，有时你可能希望将更改推送到不同的分支。在这种情况下，每次推送更改时都需要显式指定远程分支的名称。这可能会很繁琐且容易出错，尤其是在处理多个分支时。

要完成本实验，你将使用 GitHub 账户中的 Git 存储库 `git-playground`，它是从 `https://github.com/labex-labs/git-playground.git` 派生而来的。按照以下步骤设置默认推送分支名称：

1. 使用以下命令克隆存储库：
   ```
   git clone https://github.com/your-username/git-playground.git
   ```
2. 切换到存储库目录：
   ```
   cd git-playground
   ```
3. 将默认推送分支名称设置为当前本地分支的名称：
   ```
   git config push.default current
   ```
4. 创建一个新分支并切换到该分支：
   ```
   git checkout -b my-branch
   ```
5. 对存储库进行一些更改并提交：
   ```
   echo "Hello, World" > hello.txt
   git add hello.txt
   git commit -m "Add hello.txt"
   ```
6. 将你的更改推送到远程存储库：
   ```
   git push -u
   ```
   Git 将把你的更改推送到远程存储库中名为 `my-branch` 的分支。

这是运行 `git log` 的结果：

```shell
ADD hello.txt
```
