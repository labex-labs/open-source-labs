# 执行交互式变基

你正在和一组开发者共同参与一个项目，并且你已经在自己的分支上进行了多次提交。然而，你意识到其中一些提交是不必要的或者需要合并。你希望清理你的提交历史并使其更加有条理。

在这个实验中，让我们使用来自 `https://github.com/labex-labs/git-playground` 的仓库。按照以下步骤操作：

1. 导航到该目录：
   ```shell
   cd git-playground
   ```
2. 对最后两次提交执行交互式变基：
   ```shell
   git rebase -i HEAD~2
   ```
   交互式变基文件将在你的默认文本编辑器中打开。你可以修改提交的顺序以及为每个提交执行的操作（挑选、压缩、丢弃、修改等）。
3. 在提交消息“Added file2.txt”中将“pick”改为“squash”，按下 <kbd>Esc</kbd> 键并输入 <kbd>:wq</kbd> 命令，然后按下 <kbd>Enter</kbd> 键保存更改并退出编辑器，以同样的方式将提交消息改为“Added file1.txt and file2.txt”并退出。
4. 如果存在合并冲突或者你需要进行更改，你可以在准备好时使用 `git rebase --continue` 继续变基，或者使用 `git rebase --abort` 中止变基。

运行 `git log` 将得到如下结果：

```shell
commit 7575ded485555c28ecb09487c68e90639bebbe9d (HEAD -> master)
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file1.txt and file2.txt

commit b00b9374a7c549d1af111aa777fdcc868d8a2a01
Author: Hang <huhuhang@gmail.com>
Date:   Wed Apr 26 14:16:00 2023 +0800

    Initial commit
```
