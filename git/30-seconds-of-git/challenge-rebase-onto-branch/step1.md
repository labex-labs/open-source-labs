# Rebase onto Another Branch

## Problem

As a developer, you are working on a project with multiple branches. You have made changes to your branch and want to incorporate those changes into another branch. However, you don't want to merge the branches because you want to maintain a clean and linear history.

## Example

To complete this challenge, you will use the Git repository `git-playground` from your GitHub account, which comes from a fork of `https://github.com/labex-labs/git-playground.git`.

1. Clone the repository to your local machine from `https://github.com/your-username/git-playground`.
2. Switch to the `feature-branch` branch.
3. Make some changes to the `README.md` file and commit the changes with the message "Added some changes to README.md".
4. Switch to the `master` branch.
5. Ensure that your local `master` branch is up to date with the remote repository.
6. Rebase the `feature-branch` onto the `master` branch.
7. Resolve any conflicts that arise during the rebase process.
8. Push your changes to the remote repository.

This is the result of running `git log -r`:

![<result>](./assets/challenge-rebase-onto-branch-step1-1.png)
