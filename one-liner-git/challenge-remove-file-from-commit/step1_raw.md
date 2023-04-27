---
title: Remove a file from the last commit
---

Removes a file from the last commit without changing its message.

- Use `git rm —-cached <file>` to remove the specified `<file>` from the index.
- Use `git commit —-amend` to update the contents of the last commit, without changing its message.

```shell
git rm —-cached <file>
git commit —-amend
```

```shell
git rm —-cached "git-playground.txt"
git commit —-amend
# Removes `git-playground.txt` from the last commit
```
