```shell
git push -f
```

```shell
git checkout patch-1
git pull
git rebase master
# Local `patch-1` branch has been rebased onto `master`, thus diverging
# from the remote `patch-1` branch

git push -f # Force update the remote `patch-1` branch
```
