# Solutions

```shell
git rm —-cached <file>
git commit —-amend
```

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
git rm --cached "file2.txt"
git status
git commit --amend --allow-empty
# Removes `file2.txt` from the last commit
```
