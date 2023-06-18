```shell
git reset [--hard] HEAD~<n>
```

```shell
git reset HEAD~1
# Rewinds back 1 commits but keeps changes in the working directory

git reset --hard HEAD~3
# Rewinds back 3 commits and deletes changes
git push -f origin rewind-commits
```
