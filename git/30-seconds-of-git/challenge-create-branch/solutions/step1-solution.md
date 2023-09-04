```shell
git checkout -b < branch > [-t < remote > / < branch > ]

git checkout -b feature-1
# Local branch, without a remote tracking branch
git push -u origin feature-1

git checkout -b feature-1 -t origin/feature-1
# Local branch and remote tracking branch with the same name
```

```shell
# Fork from https://github.com/labex-labs/git-playground.git
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
git branch
git checkout -b feature-1
git branch
git push -u origin feature-1
```
