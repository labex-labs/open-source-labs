# Rebase onto Another Branch

## Problem

As a developer, you are working on a project with multiple branches. You have made changes to your branch and want to incorporate those changes into another branch. However, you don't want to merge the branches because you want to maintain a clean and linear history.

## Example

For this challenge, let's use the repository from `https://github.com/labex-labs/git-playground`.

1. Navigate to the directory and configure the identity.
2. Create and switch to a branch called `one-branch`.
3. Add "hello,world" to the `README.md` file, add it to the staging area and commit it with the message "Added some changes to README.md".
4. Switch to the `master` branch.
5. Ensure that your local `master` branch is up to date with the remote repository.
6. Rebase the `one-branch` onto the `master` branch.
7. Resolve any conflicts that arise during the rebase process.

This is the result of running `git log`:
```shell
commit eccff423dd6bf5335f76f2f364fa3b95130ff805 (HEAD -> master, one-branch)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Sat Jul 22 23:10:04 2023 +0800

    Added some changes to README.md
```