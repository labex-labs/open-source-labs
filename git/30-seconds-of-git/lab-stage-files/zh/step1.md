# 将文件添加到暂存区

你一直在处理存储在名为 `https://github.com/labex-labs/git-playground` 的 Git 仓库中的一个项目。你已经对代码库做了一些更改，并想将这些更改提交到仓库。然而，你只想提交特定的更改，而不是你所做的所有更改。要做到这一点，你需要将文件添加到暂存区。

1. 你将在 `git-playground` 目录中进行一些更改：

```shell
echo "hello" > index.html
echo "world" > style.css
echo "git" > one.js
echo "labex" > two.js
echo "hello git" > 1.py
echo "hello labex" > 2.py
```

2. 将这些文件添加到暂存区：

```shell
git add index.html style.css
```

3. 查看当前工作目录和暂存区的状态，包括哪些文件被修改、哪些文件已被添加到暂存区等信息：

```shell
git status
```

4. 或者，添加所有扩展名为 `.js` 的文件：

```shell
git add *.js
```

5. 再次查看当前工作目录和暂存区的状态：

```shell
git status
```

6. 你也可以将所有更改添加到暂存区：

```shell
git add.
```

7. 再次查看当前工作目录和暂存区的状态：

```shell
git status
```

这是最终结果：

![Git staging area status](../assets/challenge-stage-files-step1-1.png)
