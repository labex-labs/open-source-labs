# Discard Untracked Changes

You are working on a project using Git and have made some changes to your working directory. However, you realize that you don't need these changes and want to discard them. You want to discard all untracked changes to the current branch.

To complete this lab, you will use the Git repository named `https://github.com/labex-labs/git-playground`. Follow these steps:

1. Navigate to the repository directory:

```shell
cd git-playground
```

2. Check the status of your working directory:

```shell
git status
```

You should see the following output:

```shell
[object Object]
```

3. Discard all untracked changes to the current branch:

```shell
git clean -f -d
```

4. Check the status of your working directory again:

```shell
git status
```

You should see the following output:

```shell
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```

The `git clean -f -d` command has discarded all untracked changes to the current branch.
