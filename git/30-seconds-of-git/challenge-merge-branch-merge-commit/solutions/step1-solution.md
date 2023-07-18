```shell
git checkout <target-branch>
git merge --no-ff -m <message> <source-branch>
```

```shell
git checkout master
git merge --no-ff -m "Merge feature-branch" feature-branch
# Merges the `feature-branch` branch into `master` and creates a commit
# with the message "Merge feature-branch"
```
