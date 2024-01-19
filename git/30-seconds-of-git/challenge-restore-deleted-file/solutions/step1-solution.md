# Solutions

```shell
git checkout <commit> -- <file>
```

```shell
cd git-playground
git log --oneline
# "file2.txt" was deleted in the commit `d22f46b`
git checkout d22f46b -- file2.txt
# Restores the file2.txt file
ll
```
