```shell
git fetch --all --prune
```

```shell
git checkout master
git branch
# master
# patch-1
# patch-2

# Assuming `patch-1` is detached
git fetch --all --prune

git branch
# master
# patch-2
```
