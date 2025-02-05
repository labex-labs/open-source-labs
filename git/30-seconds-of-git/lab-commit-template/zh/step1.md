# 添加提交消息模板

如果没有提交消息模板，开发人员可能会倾向于编写模糊或缺乏信息的提交消息，例如“修复了错误”或“更新了代码”。这使得其他人很难理解更改的目的，并可能导致后续的混乱或错误。通过设置提交消息模板，可以鼓励开发人员提供更详细、更有信息的提交消息，从而提高协作效率和生产力。

对于本实验，让我们使用来自 `https://github.com/labex-labs/git-playground` 的仓库。按照以下步骤为该仓库设置提交消息模板：

1. 使用命令 `git clone https://github.com/labex-labs/git-playground` 将仓库克隆到你的本地机器。
2. 使用命令 `cd git-playground` 导航到仓库目录，并使用命令 `git config --global user.name "你的用户名"` 和 `git config --global user.email "你的邮箱"` 配置你的 GitHub 账户。
3. 使用命令 `vim commit-template` 在仓库目录中创建一个名为 `commit-template` 的新文件。
4. 在文本编辑器中打开 `commit-template` 文件，并添加以下行：

```shell
# <类型>: <主题>

# <正文>

# <页脚>

#这创建了一个包含三个部分的模板，其中 "<类型>" 表示提交的类型，例如 "feat" 或 "fix"，"<主题>" 是描述提交内容的简短摘要，"<正文>" 是更详细的描述，"<页脚>" 可以包含其他元数据，例如相关的问题编号或其他注释。
```

5. 按 <kbd>Esc</kbd> 键并输入 <kbd>:wq</kbd> 命令，然后按 <kbd>Enter</kbd> 键保存更改并退出 `commit-template` 文件编辑器。
6. 使用命令 `git add commit-template` 将 `commit-template` 文件添加到暂存区。
7. 使用命令 `git config commit.template commit-template` 将 `commit-template` 文件设置为仓库的提交消息模板。
8. 使用命令 `git commit` 打开提交消息编辑器，并注意到提交消息编辑器现在包含你在步骤 4 中创建的提交消息模板。
9. 按 <kbd>Esc</kbd> 键并输入 <kbd>:q</kbd> 命令，然后按 <kbd>Enter</kbd> 键退出提交消息编辑器。
