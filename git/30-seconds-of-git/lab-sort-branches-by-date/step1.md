# Sort Git Branches by Date

You have a Git repository with multiple branches, and you want to sort them by date. This will allow you to see which branches have been updated recently and which ones have not. Sorting branches by date can also help you identify branches that may need attention or merging.

To complete this lab, you will use the Git repository `git-playground` from your GitHub account, which comes from a fork of `https://github.com/labex-labs/git-playground.git`. 

1. Clone the repository to your local machine using the following command:
```shell
git clone https://github.com/your-username/git-playground.git
```
2. Once you have cloned the repository, navigate to the directory using the following command:
```shell
cd git-playground
```
3. Create a branch called `one`, modify the code and commit it：
```shell
git checkout -b one
touch hello.txt
git add .
git commit -m "hello.txt"
```
4. Switch to the branch named `master` and create a branch named `two`：
```shell
git checkout master
git checkout -b two
```
5. Now, to sort the branches by date, use the following command:
```shell
git branch --sort=-committerdate
```
6. View the commit history and sort the branches by date.
```shell
git log
```

This will display a list of all local branches and sort them based on the date of their last commit. You can use the arrow keys to navigate the list, and press <kbd>Q</kbd> to exit.

This is the finished result:

![<result>](./assets/challenge-sort-branches-by-date.png)
