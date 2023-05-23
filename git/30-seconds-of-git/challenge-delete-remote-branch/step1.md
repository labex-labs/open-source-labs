# Delete a Remote Branch

## Problem

Sometimes, you may need to delete a remote branch that is no longer needed. For example, if a feature branch has been merged into the main branch, you may want to delete the remote feature branch to keep the repository clean.

## Example

Suppose that a GitHub repository called `git-playground` has been cloned from your GitHub account, which comes from a fork of `https://github.com/labex-labs/git-playground.git`. You want to delete the remote branch named `feature-branch` that is no longer needed. 

1. Open the terminal and navigate to the local repository directory.
2. List all the remote branches.
3. Deletes the `feature-branch` remote branch on the `origin` remote repository.
4. Verify that the remote branch has been deleted.

The output should not include the `feature-branch` remote branch:
```
origin/HEAD -> origin/master
origin/master
```
