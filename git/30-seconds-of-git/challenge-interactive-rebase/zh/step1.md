# 执行交互式变基

你正在与一组开发者共同参与一个项目，并且你已经在自己的分支上进行了多次提交。然而，你意识到其中一些提交是不必要的，或者需要合并。你希望清理你的提交历史并使其更加有条理。

## 任务

对于这个挑战，我们使用来自 `https://github.com/labex-labs/git-playground` 的仓库。

1. 导航到该目录。
2. 对最后两次提交执行交互式变基。
3. 在提交消息 “Added file2.txt” 中将 “pick” 改为 “squash”，按下 <kbd>Esc</kbd> 并输入 <kbd>:wq</kbd> 命令，然后按下 <kbd>Enter</kbd> 保存更改并退出编辑器，以同样的方式将提交消息改为 “Added file1.txt and file2.txt” 并退出。

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
