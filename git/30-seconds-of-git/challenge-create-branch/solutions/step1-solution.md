```shell
git checkout -b < branch > [-t < remote > / < branch > ]  
```

```shell
git checkout -b feature-1
# Local branch, without a remote tracking branch
git push -u origin feature-1

git checkout -b patch-2 -t origin/patch-2
# Local branch and remote tracking branch with the same name
```
