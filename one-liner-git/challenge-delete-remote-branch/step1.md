# Delete a Remote Branch

## Problem

Sometimes, you may need to delete a remote branch that is no longer needed. For example, if a feature branch has been merged into the main branch, you may want to delete the remote feature branch to keep the repository clean.

## Example

Suppose you have a Git repository named `git-playground` hosted on GitHub. You want to delete the remote branch named `feature-branch` that is no longer needed. Here are the steps to delete the remote branch:

1. Open the terminal and navigate to the local repository directory.
2. Use the `git branch -r` command to list all the remote branches.
   ```shell
   git branch -r
   ```
   The output should include the `feature-branch` remote branch:
   ```
   origin/HEAD -> origin/main
   origin/main
   origin/feature-branch
   ```
3. Use the `git push -d <remote> <branch>` command to delete the specified remote `<branch>` on the given `<remote>`.
   ```shell
   git push -d origin feature-branch
   ```
   This command deletes the `feature-branch` remote branch on the `origin` remote repository.
4. Use the `git branch -r` command again to verify that the remote branch has been deleted.
   ```shell
   git branch -r
   ```
   The output should not include the `feature-branch` remote branch:
   ```
   origin/HEAD -> origin/main
   origin/main
   ```
