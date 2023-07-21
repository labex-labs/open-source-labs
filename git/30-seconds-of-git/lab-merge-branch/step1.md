# Merge a Branch

Your task is to merge a branch into the current branch using Git. You will need to switch to the target branch and then merge the source branch into it. This can be useful when you want to combine changes from a `feature-branch-A` into the `master` branch of your project.

For this lab, let's use the repository from `https://github.com/labex-labs/git-playground`. Follow these steps to merge the `feature-branch-A` into the `master` branch:

1. Clone the repository, navigate to the directory and configure the identity:
```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```
2. Create a `feature-branch-A` branch. Switch to it:
```shell
git checkout -b feature-branch-A
```
3. Add "hello,world" to the `file2.txt` file, add it to the staging area and commit it with the message "fix file2.txt":
```shell
echo "hello,world" >> file2.txt
git add .
git commit -m "fix file2.txt"
```
4. Switch to the `master` branch:
```shell
git checkout master
```
5. Merge the `feature-branch-A` into the `master` branch:
```shell
git merge feature-branch-A
```
6. Resolve any conflicts that may arise during the merge process.

This is the result of running `git log`:
```shell
commit e2b80358ae6e4c3b8439cf111a4672a188739290 (HEAD -> master, feature-branch-A)
Author: xiaoshengyunan <xiaoshengyunan@users.noreply.github.com>
Date:   Fri Jul 21 18:51:00 2023 +0800

    fix file2.txt
```