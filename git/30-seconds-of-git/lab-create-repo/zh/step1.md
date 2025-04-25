# 创建一个新仓库

我们已经学习了如何克隆一个现有的 Git 仓库。现在，让我们从头开始创建一个新的 Git 仓库。

打开你的终端或命令提示符，并按照以下步骤创建一个新的 Git 仓库：

```bash
cd ~/project
git init my_repo
```

这将在你当前的工作目录中创建一个名为 `my_repo` 的新目录，并在其中初始化一个新的 Git 仓库。

让我们看看 `my_repo` 目录里面有什么：

```bash
ls -a my_repo
```

你应该会看到以下文件和目录：

```plaintext
. .. .git
```

`.` 和 `..` 目录是特殊目录，分别表示当前目录和父目录。

`.git` 目录是 Git 存储仓库所有配置文件和版本历史的地方。

尝试运行以下命令，查看 `.git` 目录中的文件和目录：

```bash
ls -a my_repo/.git
```

你应该会看到以下文件和目录：

```plaintext
. ..  branches  config  description  HEAD  hooks  info  objects  ref
```

- `branches` 目录包含对仓库中分支的引用。
- `config` 文件包含特定于仓库的配置设置。
- `description` 文件包含仓库的简短描述。
- `HEAD` 文件包含对当前检出分支的引用。
- `hooks` 目录包含可由 Git 事件触发的脚本。
- `info` 目录包含全局信息文件。
- `objects` 目录包含仓库中的所有对象。
- `ref` 目录包含对仓库中提交的引用。

目前我们无需担心 `.git` 目录的内容。只需记住它是 Git 存储有关仓库所有信息的地方。
