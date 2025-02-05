# 更改远程仓库 URL

你已经从 GitHub 克隆了一个仓库并对其进行了一些更改。然而，你现在意识到需要更改远程仓库的 URL。这可能是因为原始仓库已被移动到不同的位置，或者因为你想将更改推送到不同的远程仓库。你的任务是使用 Git 命令更改仓库的远程 URL。

你需要将仓库 `https://github.com/labex-labs/git-playground` 克隆到你的本地机器。要将仓库的远程 URL 更改为 `https://github.com/your-username/git-playground`，请按照以下步骤操作：

1. 打开终端或命令提示符，克隆仓库并导航到本地仓库。
   ```
   git clone https://github.com/labex-labs/git-playground
   cd git-playground
   ```
2. 使用以下命令查看当前的远程 URL：
   ```
   git remote -v
   ```
3. 使用以下命令将远程 URL 更改为新的 URL：
   ```
   git remote set-url origin https://github.com/your-username/git-playground
   ```
4. 使用以下命令验证远程 URL 是否已更改：
   ```
   git remote -v
   ```

输出应显示新的 URL 而不是旧的 URL：

![更新后的远程 URL 输出](../assets/challenge-change-remote-url-step1-1.png)
