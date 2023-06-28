```shell
# Edit or add files
echo "New content" >> README.md
git commit --amend --no-edit
# The last commit includes the edited/added files
```

```shell
# Fork from https://github.com/labex-labs/git-playground.git
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
echo "New content" >> README.md
git add .
git commit --amend --no-edit
```
