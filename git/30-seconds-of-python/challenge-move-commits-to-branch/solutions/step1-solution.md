```shell
git branch <branch>
git reset HEAD~<n> --hard
git checkout <branch>
```

```shell
git checkout master
git add .
git commit -m "Fix network bug"
git branch patch-1
# `patch-1` branch is created containing the commit "Fix network bug"
git reset HEAD~1 --hard # Remove the commit from `master`
git checkout patch-1
```
