# Sort Git Branches by Date

You have a Git repository with multiple branches, and you want to sort them by date. This will allow you to see which branches have been updated recently and which ones have not. Sorting branches by date can also help you identify branches that may need attention or merging.

For this lab, we will be using the Git repository named `https://github.com/labex-labs/git-playground`. 

1. Clone the repository to your local machine using the following command:
```shell
git clone https://github.com/labex-labs/git-playground.git
```
2. Once you have cloned the repository, navigate to the directory using the following command:
```shell
cd git-playground
```
3. To switch a remote branch to a local branch, use the command `git checkout -b feature-branch origin/feature-branch` to switch the remote `origin/feature-branch` branch to the local branch:
```shell
git fetch origin
git checkout -b feature-branch origin/feature-branch
```
4. View the commit history and sort the branches by date.
```shell
git log
```
5. Now, to sort the branches by date, use the following command:
```shell
git branch --sort=-committerdate
```

This will display a list of all local branches and sort them based on the date of their last commit. You can use the arrow keys to navigate the list, and press <kbd>Q</kbd> to exit.

This is the finished result:

```shell
* feature-branch
  master
```
