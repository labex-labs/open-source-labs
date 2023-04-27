```shell
git cherry-pick (<commit>... | <first-commit>..<last-commit>)
```

```shell
git cherry-pick 3050fc0de # Picks changes from the commit `3050fc0de`

git cherry-pick 3050fc0de c191f90c7
# Picks changes from the commits `3050fc0de`, `c191f90c7` and `0b552a6d4`

git cherry-pick 3050fc0de..c191f90c7
# Picks changes from the commits in the range `3050fc0de` - `c191f90c7`
```
