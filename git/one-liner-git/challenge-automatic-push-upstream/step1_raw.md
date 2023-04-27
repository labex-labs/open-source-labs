---
title: Automate upstream branch creation
---

Configures the repository to automatically create upstream branches on push.

- Use `git config --add --bool` to enable automatic upstream branch creation on push.
- You can use the `--global` flag to enable this setting globally.

```shell
git config [--global] --add --bool
```

```shell
git config --global --add --bool
# `git push` will automatically create new branches, if they don't exist
```
