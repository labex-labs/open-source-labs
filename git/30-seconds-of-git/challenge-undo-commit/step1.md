# Undo a Commit

## Problem

Suppose you have made a commit to your Git repository, but you realize that it contains a mistake. You want to undo the commit without rewriting the history of your repository. How can you do this?

## Example

To demonstrate how to undo a commit, you will use the Git repository `git-playground` from your GitHub account, which comes from a fork of `https://github.com/labex-labs/git-playground.git`.

1. View the commit history.
2. Select a commit with the message "Added file1.txt" and copy its identifier.
3. Revert the commit and Git will open a text editor and let you enter a commit message, leaving the default message in place.
4. Save and close the text editor.
5. View the commit history again.

You should see a new commit that undoes the changes made by the original commit.

This is the result of running the `ll` command:
```shell
total 8.0K
-rw-r--r-- 1 labex labex 15 Jun 24 16:02 file2.txt
-rw-r--r-- 1 labex labex 32 Jun 24 16:02 README.md
```
