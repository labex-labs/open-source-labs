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
3. Create branches named `one-branch`, `two-branch` and `three-branch` in that order:
```shell
git branch one-branch
git branch two-branch
git branch three-branch
```
4. Now, to sort the branches by date, use the following command:
```shell
git branch --sort=-committerdate
```

This will display a list of all local branches and sort them based on the date of their last commit. You can use the arrow keys to navigate the list, and press <kbd>Q</kbd> to exit.

This is the finished result:

![<result>](./assets/challenge-sort-branches-by-date.png)