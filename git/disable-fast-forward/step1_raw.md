---
title: Disable fast forward merging by default
---

Disables the default fast forwarding on merge commits.

- Use `git config --add merge.ff false` to disable fast-forward merging for all branches, even if it is possible.
- You can use the `--global` flag to configure this option globally.

```shell
git config [--global] --add merge.ff false
```

```shell
git config --global --add merge.ff false

git checkout master
git merge my-branch
# Will never fast forward even if it's possible
```
