# Git Challenge: View Differences in Changes

## Problem

As a developer, you may want to view the differences between your staged or unstaged changes and the last commit. This is useful when you want to review your changes before committing them or when you want to see what changes you have made since the last commit.

## Example

To demonstrate how to view differences in changes, we will use the `git-playground` repository. Suppose you have made some changes to the `README.md` file and want to view the differences between your changes and the last commit.

1. Open your terminal and navigate to the `git-playground` directory.

```shell
cd git-playground
```

2. Use the `git diff` command to view the differences between your unstaged changes and the last commit.

```shell
git diff
```

3. Alternatively, you can use the `--staged` option to view the differences between your staged changes and the last commit.

```shell
git diff --staged
```
