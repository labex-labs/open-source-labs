---
title: Restore a deleted file
---

Restores a file deleted in a specific commit.

- Use `git checkout <commit>^ -- <file>` to restore the specified `<file>` deleted in the specified `<commit>`.

```shell
git checkout <commit>^ -- <file>
```

```shell
# "labex.txt" was deleted in the commit `3050fc0de`
git checkout 3050fc0de^ -- "labex.txt"
# Restores the labex.txt file
```
