```shell
git config commit.template <file>
```

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
vim commit-template
git add commit-template
git config commit.template "commit-template"
# Sets "commit-template" as the commit message template
git commit
```
