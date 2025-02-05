# 列出所有贮藏

你正在一个 Git 仓库中处理一个项目，并且已经做了一些尚未准备好提交的更改。你决定贮藏这些更改，以便能够处理不同的任务。之后，你想要查看已创建的所有贮藏的列表，以便决定应用哪一个。如何列出 Git 仓库中的所有贮藏呢？

1. 导航到 `git-playground` 目录：

```
cd git-playground
```

2. 创建一个名为 `test.txt` 的新文件，并向其中添加一些内容：

```
echo "hello,world" > test.txt
git add.
```

3. 使用以下命令贮藏你的更改：

```
git stash save "Added test.txt"
```

4. 创建另一个名为 `test2.txt` 的新文件，并向其中添加一些内容：

```
echo "hello,labex" > test2.txt
git add.
```

5. 使用以下命令贮藏你的更改：

```
git stash save "Added test2.txt"
```

6. 使用以下命令列出所有贮藏：

```
git stash list
```

你应该会看到类似于以下的输出：

```
stash@{0}: On master: Added test2.txt
stash@{1}: On master: Added test.txt
```
