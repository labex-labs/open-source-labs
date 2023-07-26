# Sort Git Branches by Date

You have a Git repository with multiple branches, and you want to sort them by date. This will allow you to see which branches have been updated recently and which ones have not. Sorting branches by date can also help you identify branches that may need attention or merging.

For this lab, we will be using the Git repository named `https://github.com/labex-labs/git-playground`.

1. Clone the repository to your local machine:
```shell
git clone https://github.com/labex-labs/git-playground
```
2. Navigate to the repository directory and configure your GitHub identity:
```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
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

This will display a list of all local branches and sort them based on the date of their last commit. You can use the arrow keys to navigate the list, and press Q to exit.