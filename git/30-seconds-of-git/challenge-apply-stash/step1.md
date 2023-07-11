# Apply a stash

## Problem

You are working on a feature branch in the `git-playground` repository and you need to switch to another branch to work on a bug fix. However, you have some changes that are not ready to be committed yet. You want to save these changes and switch to the other branch. Once you are done with the bug fix, you want to apply the stash and continue working on your feature branch.

## Example

The changes have been stashed on the `feature-branch` branch, and the stash message is "my changes".

1. Change to the `git-playground` directory.
2. Switch to the `master` branch and stash it after fixing the bug, the stash message is "fixing bug". Fix the bug by updating the contents of the `file1.txt` file to "hello,world".
3. Switch to the `feature-branch` branch, look at the list of stashes, and apply the stash whose information is "my changes".

This is the contents of the `README.md` file:
```
# git-playground
Git Playground
some changes
```

You should see that the changes you made before stashing are now applied.
