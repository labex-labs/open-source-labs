```shell
git config [--global] --add merge.ff false
```

```shell
git config --global --add merge.ff false

git checkout master
git merge my-branch
# Will never fast forward even if it's possible
```
