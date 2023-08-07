# Undo the Last Commit

You have just committed changes to your Git repository, but you realize that you made a mistake. You want to undo the last commit without losing any of the changes you made. How can you do this?

For this lab, let's use the repository from `https://github.com/labex-labs/git-playground`. Follow these steps:

1. Clone the repository, navigate to the directory and configure the identity:
```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```
2. Check the commit history:
```shell
git log
```
3. Undo the last commit, creating a new commit with the inverse of the commit's changes:
```shell
git revert HEAD
```
4. Check the commit history again:
```shell
git log
```

This is the result of running the `git log --oneline` command:
```shell
532b49b (HEAD -> master) Revert "Added file2.txt"
d22f46b (origin/master, origin/HEAD) Added file2.txt
cf80005 Added file1.txt
b00b937 Initial commit
```
