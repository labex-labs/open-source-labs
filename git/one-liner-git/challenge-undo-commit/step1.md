# Undo a Commit

## Problem

Suppose you have made a commit to your Git repository, but you realize that it contains a mistake. You want to undo the commit without rewriting the history of your repository. How can you do this?

## Example

To demonstrate how to undo a commit, we will use the Git repository named `https://github.com/labex-labs/git-playground`. Follow these steps:

1. Clone the repository to your local machine:
   ```
   git clone https://github.com/labex-labs/git-playground.git
   ```
2. Change into the repository directory:
   ```
   cd git-playground
   ```
3. View the commit history:
   ```
   git log
   ```
   You should see a list of commits, each with a unique identifier (a long string of letters and numbers).
4. Choose a commit that you want to undo and copy its identifier.
5. Revert the commit using the `git revert` command:
   ```
   git revert <commit>
   ```
   Replace `<commit>` with the identifier of the commit you want to revert.
6. Git will open a text editor for you to enter a commit message. You can leave the default message or enter your own.
7. Save and close the text editor.
8. View the commit history again:
   ```
   git log
   ```
   You should see a new commit that undoes the changes made by the original commit.
