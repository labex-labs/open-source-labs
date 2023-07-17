# Merge a Branch

## Problem

Your task is to merge a branch into the current branch using Git. You will need to switch to the target branch and then merge the source branch into it. This can be useful when you want to combine changes from a feature branch into the main branch of your project.

## Example

To complete this challenge, you will use the Git repository git-playground from your GitHub account, which comes from a fork of https://github.com/labex-labs/git-playground.git.

1. Clone the repository to your local machine from `https://github.com/your-username/git-playground`, navigate to the directory and configure the identity.
2. Create and switch to `feature-branch-A`, add "hello" to `file2.txt`, add it to the staging area and commit it, the commit message will be "fix file2.txt".
3. Switch to the `master` branch and merge the `feature-branch-A` into the `master` branch.
4. Resolve any conflicts that may arise during the merge process.
5. Push the changes to the remote repository.

This is the final result:
```shell
commit 742e0d4feeec7c5989e2336de7526600301e284e (HEAD -> master, feature-branch-A)
Author: xiaoshengyunan <1797063828@qq.com>
Date:   Mon Jul 17 20:35:15 2023 +0800

    fix file2.txt
```