```shell
git config commit.template <file>
```

```shell
git clone https://github.com/your-username/git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
cd git-playground
touch commit-template
git config commit.template "commit-template"
# Sets "commit-template" as the commit message template
echo "test" >> README.md
git commit
git push
```
