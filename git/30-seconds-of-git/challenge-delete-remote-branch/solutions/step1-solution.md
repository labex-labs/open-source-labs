```shell
git push -d <remote> <branch>
```

```shell
# Fork from https://github.com/labex-labs/git-playground.git
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
git checkout -b feature-branch
git push -u origin feature-branch
git branch -r
git push -d origin feature-branch # Deletes the `feature-branch` remote branch
git branch -r
```
