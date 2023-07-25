# Disable Fast Forward Merging

## Problem

By default, Git uses fast forward merging to merge branches that have no divergent commits. This means that if you have a branch with no new commits, Git will simply move the pointer of the branch you are merging into to the latest commit of the branch you are merging from. While this can be useful in some cases, it can also cause issues, especially when working on larger projects with multiple contributors. For example, if two developers are working on the same branch and both make changes, fast forward merging can cause conflicts that are difficult to resolve.

## Example

To disable fast forward merging, let's use the repository from `https://github.com/labex-labs/git-playground`.

1. Navigate to the directory and configure the identity.
2. Create and switch to a branch called `my-branch`, create a `hello.txt` file and add "hello,world" to it, add it to the staging area and commit it with the message "Added hello.txt".
3. Disable fast forward merging for all branches.
4. Switch back to the `mater` branch and merge the `my-branch` branch, save and exit without changing the text.

Now, Git will always create a merge commit, even if it is possible to fast forward:
```shell
commit 6e17a776ab51a89ace069614b0caf1c07915a92c (HEAD -> master)
Merge: ec5ea6d 6d7de91
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Mon Jul 17 13:30:44 2023 +0800

    Merge branch 'my-branch'
```
