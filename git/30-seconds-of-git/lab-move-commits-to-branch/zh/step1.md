# 将提交移动到新分支

对于这个实验，让我们使用来自 `https://github.com/labex-labs/git-playground` 的仓库。你一直在 `master` 分支上处理一个项目。你意识到你所做的一些更改应该在一个单独的分支上进行。你想将这些更改移动到一个名为 `feature` 的新分支上。

1. 克隆仓库，导航到该目录并配置身份：

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "你的用户名"
git config --global user.email "你的邮箱"
```

2. 检出 `master` 分支：

```shell
git checkout master
```

3. 创建一个名为 `hello.txt` 的文件，在其中添加 "hello, world"，将其添加到暂存区并使用消息 "添加了 hello.txt" 提交：

```shell
echo "hello,world" >> hello.txt
git add.
git commit -m "添加了 hello.txt"
```

4. 创建一个名为 `feature` 的新分支但不切换到它。当你在 `master` 分支上创建一个新分支时，新分支的状态与 `master` 分支相同，即新分支中的文件与 `master` 分支中的文件相同，具有相同的内容和版本历史：

```shell
git branch feature
```

5. 撤销 `master` 上的最后一次提交：

```shell
git reset HEAD~1 --hard
```

6. 检查 `master` 分支上的提交历史和 `feature` 分支上的提交历史以验证结果：

```shell
git log
git checkout feature
git log
```

这是运行 `git log` 的结果：

```shell
commit 7969ab5d6606e2a40c9fd826c732206b835976e9 (HEAD -> feature)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 20:19:22 2023 +0800

    添加了 hello.txt
```
