```shell
git branch -m <old-name> <new-name>
git push origin --delete <old-name>
git checkout <new-name>
git push origin -u <new-name>
```

```shell
git checkout master
git branch -m feature-1 new-feature-1 # Renamed the local branch to `new-feature-1`
git push origin --delete feature-1
git checkout new-feature-1
git push origin -u new-feature-1 # Renames the remote branch to `new-feature-1`
```
