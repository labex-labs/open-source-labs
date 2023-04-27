```shell
git checkout <branch>
git rebase <base-branch>
```

```shell
git checkout patch-1
git rebase master
# `patch-1` is rebased onto `master`

git checkout patch-2
git fetch origin # Fetch latest remote branches
git rebase origin/master
# `patch-2` is rebased onto the latest remote `master`
```
