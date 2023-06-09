```shell
git stash save [-u] [ < message > ]
```

```shell
git stash save
# Creates a new stash

git stash save -u
# Creates a new stash, including untracked files

git stash save "My changes"
# Creates a new stash with the message "My changes"
git stash apply
```
