# Discard Uncommitted Changes

You have made some changes to your local Git repository, but you have not yet committed them. However, you have decided that you no longer want to keep these changes and want to discard them. The problem is to find a way to discard all uncommitted changes to the current branch.

To complete this challenge, you will use the Git repository named `https://github.com/labex-labs/git-playground` directory. Follow the steps below:

1. Clone the repository to your local machine using the command `git clone https://github.com/labex-labs/git-playground.git`.
2. Navigate to the cloned repository using the command `cd git-playground`.
3. Make some changes to the files in the repository, but do not commit them using the commands `echo "hello,world" > hello.txt` and `git add .`.
4. Use the command `git status` to see the changes you have made.
5. Discard all uncommitted changes using the command `git reset --hard HEAD`.
6. Use the command `git status` again to confirm that all changes have been discarded.

This is the result of running `git status`:
```shell
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```
