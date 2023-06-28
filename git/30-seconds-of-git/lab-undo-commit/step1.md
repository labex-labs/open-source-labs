# Undo a Commit

Suppose you have made a commit to your Git repository, but you realize that it contains a mistake. You want to undo the commit without rewriting the history of your repository. How can you do this?

To demonstrate how to undo a commit, you will use the Git repository `git-playground` from your GitHub account, which comes from a fork of `https://github.com/labex-labs/git-playground.git`. Follow these steps:

1. Clone the repository to your local machine:
   ```
   git clone https://github.com/your-username/git-playground.git
   ```
2. Change into the repository directory:
   ```
   cd git-playground
   ```
3. View the commit history:
   ```
   git log
   ```
   You should see a list of commits, each with a unique identifier (a long string of letters and        numbers).
4. Select a commit with the message "Added file1.txt" and copy its identifier.
5. Revert the commit using the `git revert` command:
   ```
   git revert <commit>
   ```
   Replace `<commit>` with the identifier of the commit you want to revert.
6. Git will open a text editor and let you enter a commit message, leaving the default message in place.
7. Save and close the text editor.
8. View the commit history again:
   ```
   git log
   ```
   You should see a new commit that undoes the changes made by the original commit.

This is the result of running the `ll` command:
```shell
total 8.0K
-rw-r--r-- 1 labex labex 15 Jun 24 16:02 file2.txt
-rw-r--r-- 1 labex labex 32 Jun 24 16:02 README.md
```
