# Undo the Last Commit

## Problem

You have just committed changes to your Git repository, but you realize that you made a mistake. You want to undo the last commit without losing any of the changes you made. How can you do this?

## Example

For this challenge, let's use the repository from `https://github.com/labex-labs/git-playground`.

1. Check the commit history.
2. Undo the last commit, creating a new commit with the inverse of the commit's changes.

This is the result of running the `git log --oneline` command:

```shell
532b49b (HEAD -> master) Revert "Added file2.txt"
d22f46b (origin/master, origin/HEAD) Added file2.txt
cf80005 Added file1.txt
b00b937 Initial commit
```
