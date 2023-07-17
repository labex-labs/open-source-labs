# Apply the Latest Stash

You are working on a project in your Git repository and have made some changes that are not yet ready to be committed. However, you need to switch to another branch or commit to work on a different feature. You don't want to lose your changes, so you decide to stash them. Later, when you're ready to continue working on your changes, you need to apply the latest stash to your working directory.

To apply the latest stash to your Git repository, follow these steps:

1. Clone the Git repository named `https://github.com/labex-labs/git-playground` to your local machine.
2. Navigate to the `git-playground` directory.
3. Make some changes to the `README.md` file, e.g. write "This is a new line" in the `README.md` file.
4. Run the command `git stash` to stash your changes.
5. Run the command `git stash list` to see a list of your stashes. You should see one stash in the list.
6. Run the command `git stash apply` to apply the latest stash to your working directory.
7. Check the `README.md` file to see that your changes have been applied.

```shell
git clone https://github.com/labex-labs/git-playground.git
cd git-playground
echo "This is a new line" >> README.md
git stash
git stash list
git stash apply
cat README.md
```
