---
title: Add a submodule
---

Adds a new submodule to the repository.

- Use `git submodule add <upstream-path> <local-path>` to add a new submodule from `<upstream-path>` to `<local-path>`.

```shell
git submodule add <upstream-path> <local-path>
```

```shell
git submodule add https://github.com/labex-labs/git-playground.git ./git-playground
# Creates the directory `30code` containing the submodule from
# "https://github.com/labex-labs/git-playground.git"
```
