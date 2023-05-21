```shell
git commit --fixup <commit>
```

```shell
git add .  
git commit --fixup 3050fc0de
# Created a fixup commit for `3050fc0de`
git rebase HEAD~5 --autosquash
# Now the fixup commit has been squashed
```
