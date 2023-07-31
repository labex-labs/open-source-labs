# Add a Commit Message Template

Without a commit message template, developers may be tempted to write vague or uninformative commit messages, such as "fixed bug" or "updated code". This makes it difficult for others to understand the purpose of the change and can lead to confusion or mistakes down the line. By setting up a commit message template, developers are encouraged to provide more detailed and informative commit messages, which can improve collaboration and productivity.

For this lab, let's use the repository from `https://github.com/labex-labs/git-playground`. Follow these steps to set up a commit message template for this repository:

1. Clone the repository to your local machine using the command `git clone https://github.com/labex-labs/git-playground`.
2. Navigate to the repository directory using the command `cd git-playground` and configure your GitHub account using the commands `git config --global user.name "your-username"` and `git config --global user.email "your-email"`.
3. Create a new file named `commit-template` in the repository directory using the command `vim commit-template`.
4. Open the `commit-template` file in a text editor and add the following lines:
```shell
# <type>: <subject>

# <body>

# <footer>

#This creates a template with three sections, where "<type>" indicates the type of submission, such as "feat" or "fix", "<subject>" is a short #summary describing the content of the submission, "<body>" is a more detailed description, and "<footer>" can contain other metadata, such as the #associated issue number or other comments.
```
5. Press <kbd>Esc</kbd> and enter the <kbd>:wq</kbd> command, then press <kbd>Enter</kbd> to save your changes and exit the `commit-template` file editor.
6. Use the command `git add commit-template`to add `commit-template` files to the staging area.
7. Use the command `git config commit.template commit-template` to set the `commit-template` file as the commit message template for the repository.
8. Use the command `git commit` to open the commit message editor and notice that the commit message editor now contains the commit message template you created in step 4.
9. Press <kbd>Esc</kbd> and enter the <kbd>:q</kbd> command, then press <kbd>Enter</kbd> to exit the commit message editor.
