# Move Commits to a New Branch

## Problem

For this challenge, let's use the repository from `https://github.com/labex-labs/git-playground`. You have been working on a project in the `master` branch. You realize that some of the changes you made should have been made on a separate branch. You want to move these changes to a new branch called `feature-branch`.

## Example

1. Navigate to the repository directory and configure your GitHub identity.
2. Checkout the `master` branch.
3. Create a file called `hello.txt`, add "hello, world" to it, add it to the staging area and submit it with the message "Added hello.txt".
4. Create a new branch called `feature-branch` without switching to it .
5. Undo the last commit on `master`.
6. Check the commit history on the `master` branch and the commit history on the `feature-branch` branch to verify the results.

This is the result of running `git log`:
```shell
commit 7969ab5d6606e2a40c9fd826c732206b835976e9 (HEAD -> feature-branch)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 20:19:22 2023 +0800

    Added hello.txt
```
