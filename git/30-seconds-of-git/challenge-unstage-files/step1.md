# Remove Files from the Staging Area

## Problem

You are working on a project in the `git-playground` repository. You have made some changes to the files and added them to the staging area. However, you realize that you accidentally added a file that you don't want to commit. You need to remove this file from the staging area.

## Example

1. View current working directory status.
2. Remove the `newfile.txt` file from the staging area.
3. Verify that the file has been removed from the staging area.

This is the final result:

```shell
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        newfile.txt
```
