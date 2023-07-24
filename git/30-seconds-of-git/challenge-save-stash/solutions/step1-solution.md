```shell
git stash save [-u] [ < message > ]

git stash save
# Creates a new stash

git stash save -u
# Creates a new stash, including untracked files

git stash save "My changes"
# Creates a new stash with the message "My changes"
git stash apply
```

```shell
cd git-playground
git checkout -b feature
echo "Some changes" >> README.md
git stash save "My changes"
git checkout master
git checkout feature
git stash apply
```
