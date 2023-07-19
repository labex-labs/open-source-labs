```shell
git reset [--hard] <commit>

git reset 3050fc0d3
# Rewinds back to `3050fc0d3` but keeps changes in the working directory

git reset --hard c0d30f305
# Rewinds back to `c0d30f305` and deletes changes
```

```shell
cd git-playground
git log --oneline
git reset 3050fc0d3 #the "Initial commit" commit hash
```
