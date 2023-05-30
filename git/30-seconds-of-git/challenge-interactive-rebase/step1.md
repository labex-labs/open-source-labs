# Perform an Interactive Rebase

## Problem

You are working on a project with a team of developers, and you have made several commits to your branch. However, you realize that some of the commits are unnecessary or need to be combined. You want to clean up your commit history and make it more organized.

## Example

To complete this challenge, you will use the Git repository named `https://github.com/labex-labs/git-playground`. Follow these steps:

1. Clone the repository to your local machine using the command `git clone https://github.com/labex-labs/git-playground`.
2. Navigate to the directory using the command `cd git-playground`.
3. Create a new branch using the command `git checkout -b my-branch`.
4. Make several commits to the branch using the command `git commit -m "commit message"`.
5. Run the command `git rebase -i HEAD~3` to perform an interactive rebase of the last 3 commits.
6. The interactive rebase file will open in your default text editor. You can modify the order of the commits and the action to perform for each one (pick, squash, drop, reword etc.).
7. Save and close the file.
8. If there are merge conflicts or you need to make changes, you can continue the rebase when ready using `git rebase --continue` or abort it using `git rebase --abort`.
9. Once the rebase is complete, push the changes to the remote repository using the command `git push -u origin my-branch`.
    