---
title: Copy a file from another branch
---

Copies a file from another branch to the current branch.

- Use `git checkout <branch> <file>` to copy the specified `<file>` from the specified `<branch>`.

```shell
git checkout <branch> <file>
```

```shell
git checkout patch-2
git checkout patch-1 "labex.txt"
# `patch-2` branch now contains the labex.txt file from `patch-1`
```
