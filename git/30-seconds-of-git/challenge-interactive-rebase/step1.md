# Perform an Interactive Rebase

## Problem

You are working on a project with a team of developers, and you have made several commits to your branch. However, you realize that some of the commits are unnecessary or need to be combined. You want to clean up your commit history and make it more organized.

## Example

To complete this challenge,you will fork `https://github.com/labex-labs/git-playground` to your GitHub account and use the Git repository named `https://github.com/your-username/git-playground` in your environment.

1. Clone the repository to your local machine.
2. Navigate to the directory.
3. Create a new branch named `my-branch`.
4. Make several commits to the branch.
5. Perform an interactive rebase of the last 3 commits.
6. The interactive rebase file will open in your default text editor. You can modify the order of the commits and the action to perform for each one (pick, squash, drop, reword etc.).
7. Save and close the file.
8. Once the rebase is complete, push the changes to the remote repository.

Running `git log origin/my-branch` will give you a result that looks like this:

![<result>](./assets/challenge-interactive-rebase-step1-1.png)
