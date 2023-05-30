```shell
git rebase -i [--autosquash] <commit>
```

```shell
git rebase -i 3050fc0de
# Performs an interactive rebase starting from `3050fc0de`

git rebase -i --autosquash HEAD~5
# Performs an interactive rebase of the last 5 commits,
# automatically squashing fixup commits
```       
