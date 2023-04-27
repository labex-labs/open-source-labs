# Disable Fast Forward Merging

## Problem

By default, Git uses fast forward merging to merge branches that have no divergent commits. This means that if you have a branch with no new commits, Git will simply move the pointer of the branch you are merging into to the latest commit of the branch you are merging from. While this can be useful in some cases, it can also cause issues, especially when working on larger projects with multiple contributors. For example, if two developers are working on the same branch and both make changes, fast forward merging can cause conflicts that are difficult to resolve.

## Example

To disable fast forward merging, you can use the `git config` command. First, clone the `git-playground` repository:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

Next, navigate to the repository directory:

```shell
cd git-playground
```

Now, run the following command to disable fast forward merging:

```shell
git config --add merge.ff false
```

This will disable fast forward merging for all branches, even if it is possible. You can use the `--global` flag to configure this option globally:

```shell
git config --global --add merge.ff false
```

Now, if you try to merge a branch into another branch, Git will always create a merge commit, even if it is possible to fast forward:

```shell
git checkout master
git merge my-branch
```
