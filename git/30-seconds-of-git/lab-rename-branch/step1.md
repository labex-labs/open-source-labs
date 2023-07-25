# Rename a Branch

As a developer, you may need to rename a branch for various reasons, such as to make it more descriptive or to follow a naming convention. Renaming a branch can be a simple task, but it requires some knowledge of Git commands. In this challenge, you will learn how to rename a branch using Git.

For this lab, we will use the Git repository named `https://github.com/labex-labs/git-playground`.

Suppose you will create a branch named `old-branch` to work on a new feature. After completing the feature, you realize that the branch name is not descriptive enough. You want to rename the branch to `new-branch` to make it more meaningful. To rename the branch, follow these steps:

1. Open the terminal and navigate to the local repository directory.
2. Use the `git checkout -b old-branch` command to create a branch named `old-branch` and use the `git branch -m <old-name> <new-name>` command to rename the branch. In our example, the command would be `git branch -m old-branch new-branch`.
3. Verify that the branch has been renamed by using the `git branch` command. 

The output should show the new branch name:
```shell
master
* new-branch
```
