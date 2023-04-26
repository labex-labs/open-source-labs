```shell
git branch --merged <branch> | grep -v "(^\*|<branch>)" | xargs git branch -d
```

```shell
git checkout master
git branch
# master
# patch-1
# patch-2

# Assuming `patch-1` is merged into master
git branch --merged master | grep -v "(^\*|master)" | xargs git branch -d

git branch
# master
# patch-2
```
