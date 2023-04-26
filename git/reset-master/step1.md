# Reset Local Master Branch to Match Remote

## Problem

You have been working on a project and have made changes to the local `master` branch. However, you realize that the remote `master` branch has been updated with new changes that you do not have in your local branch. You need to reset the local `master` branch to match the one on the remote.

## Example

1. Clone the Git repository named `https://github.com/labex-labs/git-playground` directory.
2. Use `git fetch origin` to retrieve the latest updates from the remote.
   ```shell
   git fetch origin
   ```
3. Use `git checkout master` to switch to the `master` branch.
   ```shell
   git checkout master
   ```
4. Use `git reset --hard origin/master` to reset the local `master` branch to match the one on the remote.
   ```shell
   git reset --hard origin/master
   ```
5. Verify that the local `master` branch is now up to date with the remote `master` branch.
   ```shell
   git status
   ```
