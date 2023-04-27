```shell
git checkout <target-branch>
git merge --no-ff -m <message> <source-branch>
```

```shell
git checkout master
git merge --no-ff -m "Merge patch-1" patch-1
# Merges the `patch-1` branch into `master` and creates a commit
# with the message "Merge patch-1"
```
