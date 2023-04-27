```shell
git checkout <commit>^ -- <file>
```

```shell
# "labex.txt" was deleted in the commit `3050fc0de`
git checkout 3050fc0de^ -- "labex.txt"
# Restores the labex.txt file
```
