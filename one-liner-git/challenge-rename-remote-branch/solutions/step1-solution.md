```shell
git branch -m <old-name> <new-name>
git push origin --delete <old-name>
git checkout <new-name>
git push origin -u <new-name>
```

```shell
git checkout master
git branch -m patch-1 patch-2 # Renamed the local branch to `patch-2`
git push origin --delete patch-1
git checkout patch-2
git push origin -u patch-2 # Renames the remote branch to `patch-2`
```
