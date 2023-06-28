```shell
git revert <commit>
```

```shell
# Fork from https://github.com/labex-labs/git-playground.git
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
git log
git revert 3050fc0d3
# a commit with the message "Added file1.txt"
# Reverts the commit `3050fc0d3`
```
