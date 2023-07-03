# View Current Status

## Problem

As a developer, it's important to know the current status of your Git repository. This includes information about which files have been modified, which files are staged for commit, and which files are untracked.

Your task is to view the current status of the Git repository located at `https://github.com/labex-labs/git-playground`. You should pay attention to the output of the command and try to understand what it means.

## Example

To complete this challenge, you will need to clone the Git repository located at `https://github.com/labex-labs/git-playground`. 

1. Once you have cloned the repository, navigate to the root directory of the repository.
2. View the current status of the Git repository.

This will output the current status of the working tree. You should see information about which branch you are currently on, whether your branch is up to date with the remote repository, and any untracked or modified files.

The output looks like this:
```shell
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
```
