# Undo the Last Commit

You have just committed changes to your Git repository, but you realize that you made a mistake. You want to undo the last commit without losing any of the changes you made. How can you do this?

To complete this lab, you will use the Git repository `git-playground` from your GitHub account, which comes from a fork of `https://github.com/labex-labs/git-playground.git`. Follow these steps:

1. Clone the repository to your local machine using the command `git clone https://github.com/your-username/git-playground`.
2. Navigate to the repository directory using the command `cd git-playground`.
3. Check the commit history using the command `git log`.
4. Use `git revert HEAD` to undo the last commit, creating a new commit with the inverse of the commit's changes.
5. Check the commit history again using the command `git log`.

This is the result of running the `git log --oneline` command:
```
532b49b (HEAD -> master) Revert "Added file2.txt"
d22f46b (origin/master, origin/HEAD) Added file2.txt
cf80005 Added file1.txt
b00b937 Initial commit
```
