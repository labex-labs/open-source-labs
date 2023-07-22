# Rebase onto Another Branch

As a developer, you are working on a project with multiple branches. You have made changes to your branch and want to incorporate those changes into another branch. However, you don't want to merge the branches because you want to maintain a clean and linear history. In this case, you can use the `git rebase` command to rebase your branch onto another branch.

For this lab, let's use the repository from `https://github.com/labex-labs/git-playground`. Follow the steps below to complete the challenge:

1. Clone the repository, navigate to the directory and configure the identity:
```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```
2. Create and switch to a branch called `one-branch`:
```shell
git checkout -b one-branch
```
3. Add "hello,world" to the `README.md` file, add it to the staging area and commit it with the message "Added some changes to README.md":
```shell
echo "hello,world" >> README.md
git add .
git commit -am "Added some changes to README.md"
```
4. Switch to the `master` branch:
```shell
git checkout master
``` 
5. Ensure that your local `master` branch is up to date with the remote repository:
```shell
git pull
```
6. Rebase the `one-branch` onto the `master` branch:
```shell
git rebase one-branch
```
7. Resolve any conflicts that arise during the rebase process.

This is the result of running `git log`:
```shell
commit eccff423dd6bf5335f76f2f364fa3b95130ff805 (HEAD -> master, one-branch)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Sat Jul 22 23:10:04 2023 +0800

    Added some changes to README.md
```
