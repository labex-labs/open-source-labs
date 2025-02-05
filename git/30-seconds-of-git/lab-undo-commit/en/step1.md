# Undo a Commit

Suppose you have made a commit to your Git repository, but you realize that it contains a mistake. You want to undo the commit without rewriting the history of your repository. How can you do this?

To demonstrate how to undo a commit, let's use the repository from `https://github.com/labex-labs/git-playground`. Follow these steps:

1. Clone the repository, navigate to the directory and configure the identity:
   ```
   git clone https://github.com/labex-labs/git-playground
   cd git-playground
   git config --global user.name "your-username"
   git config --global user.email "your-email"
   ```
2. View the commit history:
   ```
   git log
   ```
   You should see a list of commits, each with a unique identifier (a long string of letters and numbers).
3. Select a commit with the message "Added file1.txt" and copy its identifier.
4. Revert the commit using the `git revert` command:
   ```
   git revert <commit>
   ```
   Replace `<commit>` with the identifier of the commit you want to revert.
5. Git will open a text editor and let you enter a commit message, leaving the default message in place.
6. Save and close the text editor.
7. View the commit history again:
   ```
   git log
   ```
   You should see a new commit that undoes the changes made by the original commit.

This is the result of running the `git log` command:

```
commit 0d01f357a798f8960959546750d89a7e56a04a44 (HEAD -> master)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Mon Jul 24 21:52:43 2023 +0800

    Revert "Added file1.txt"

    This reverts commit cf80005e40a3c661eb212fcea5fad06f8283f08f.
```
