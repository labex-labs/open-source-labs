# Undo the Last Commit

You have just committed changes to your Git repository, but you realize that you made a mistake. You want to undo the last commit without losing any of the changes you made. How can you do this?

To complete this challenge, you will need to use the Git repository named `https://github.com/labex-labs/git-playground` directory. Follow these steps:

1. Clone the repository to your local machine using the command `git clone https://github.com/labex-labs/git-playground`.
2. Navigate to the repository directory using the command `cd git-playground`.
3. Make some changes to the repository files using your preferred text editor.
4. Add the changes to the staging area using the command `git add .`.
5. Commit the changes using the command `git commit -m "Commit message"`.
6. Check the commit history using the command `git log`.
7. Use `git revert HEAD` to undo the last commit, creating a new commit with the inverse of the commit's changes.
8. Check the commit history again using the command `git log`.
