# 自动创建上游分支

作为一名开发者，你希望在推送时自动创建上游分支，以避免在远程仓库上手动创建分支的麻烦。

在这个实验中，你将把 `https://github.com/labex-labs/git-playground` 仓库复刻到你的账户，使用你账户上的 `git-playground` 仓库在推送时自动创建上游分支。

1. 在 GitHub 网站上，登录你的账户，找到 `https://github.com/labex-labs/git-playground` 并将该仓库复刻到你的账户。
2. 在你自己复刻仓库的页面上，点击 `Code` 按钮并复制仓库的 URL。
3. 克隆该仓库，进入目录并配置身份：

```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

4. 使用以下命令在推送时启用自动上游分支创建：

```shell
git config --global push.default current
```

5. 推送一个名为 `new-feature` 的新分支，该分支在远程仓库中不存在：

```shell
git checkout -b new-feature
git push
```

6. 验证新分支是否已在远程仓库上创建：

```shell
git ls-remote --heads origin
```

这是完成实验后的结果：

![自动上游分支结果](../assets/challenge-automatic-push-upstream-step1-1.png)
