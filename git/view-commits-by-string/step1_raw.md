---
title: View commits that manipulated a specific string
---

Prints a list of all commits that manipulated a given string.

- Use `git log -S<string>` to find all commits that manipulated the specified `<string>`.
- Use arrow keys to navigate, press <kbd>Q</kbd> to exit.

```shell
git log -S<string>
```

```shell
git log -S"git-playground"
# commit c191f90c7766ee6d5f24e90b552a7d446f0d02e4
# Author: labex
# Date: Tue Apr 26 10:10:08 2023 +0300
# [...]
```
