# Undo a Commit

## Problem

Suppose you have made a commit to your Git repository, but you realize that it contains a mistake. You want to undo the commit without rewriting the history of your repository. How can you do this?

## Example

To demonstrate how to undo a commit, let's use the repository from `https://github.com/labex-labs/git-playground`.

1. Navigate to the repository directory and configure your GitHub identity.
2. View the commit history.
3. Select a commit with the message "Added file1.txt" and copy its identifier.
4. Revert the commit and Git will open a text editor and let you enter a commit message, leaving the default message in place.
5. Save and close the text editor.
6. View the commit history again.

You should see a new commit that undoes the changes made by the original commit.

This is the result of running the `git log` command:
```
commit 0d01f357a798f8960959546750d89a7e56a04a44 (HEAD -> master)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Mon Jul 24 21:52:43 2023 +0800

    Revert "Added file1.txt"
    
    This reverts commit cf80005e40a3c661eb212fcea5fad06f8283f08f.
```
