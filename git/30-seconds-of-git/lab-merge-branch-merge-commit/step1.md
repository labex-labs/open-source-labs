# Merge a Branch and Create a Merge Commit

As a developer, you may need to merge a branch into the current branch, creating a merge commit. This can be a bit tricky if you're not familiar with Git. The problem is to merge a branch into the current branch, creating a merge commit, using the Git repository named `https://github.com/labex-labs/git-playground` directory.

Suppose you are working on a project with a team of developers, and you need to merge a branch named `feature-branch` into the `master` branch. Here are the steps you would take:

1. Clone a repository from `https://github.com/labex-labs/git-playground.git`:
```shell
git clone https://github.com/labex-labs/git-playground.git
```
2. Navigate to the directory and configure the identity: 
```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```
3. Create an empty branch `feature-branch` and modify the `README.md` file:
```shell
git checkout -b feature-branch
echo "This is a new line." >> README.md
git add .
```
4. Commit all modified files to the local repository:
```shell
git commit -am "Add new line to README.md"
```
5. Switch to the `master` branch:
```shell
git checkout master
```
6. Merge the `feature-branch` into the `master` branch,which will create a merge commit with the message "Merge feature-branch":
```shell
git merge --no-ff -m "Merge feature-branch" feature-branch
```

This is the result of running `git log`:
```shell
commit 45b7e0fa8656d0aa751c7ca3cee29422e3d6cf05 (HEAD -> master)
Merge: d22f46b 1f19499
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 19:26:57 2023 +0800

    Merge feature-branch

commit 1f1949955387a154ff1bb5286d3d0a2b993f87e0 (feature-branch)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 19:26:57 2023 +0800

    Add new line to README.md
```
