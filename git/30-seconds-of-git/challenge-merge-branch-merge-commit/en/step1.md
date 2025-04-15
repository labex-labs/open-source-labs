# Merge a Branch and Create a Merge Commit

As a developer, you may need to merge a branch into the current branch, creating a merge commit. This can be a bit tricky if you're not familiar with Git. The problem is to merge a branch into the current branch, creating a merge commit, using the Git repository named `https://github.com/labex-labs/git-playground` directory.

## Tasks

For this challenge, let's use the repository from `https://github.com/labex-labs/git-playground`.

1. Clone the repository, navigate to the directory and configure the identity.
2. Create and switch to a branch called `feature-branch`.
3. Add "This is a new line." to the `README.md` file, add it to the staging area and commit it, the commit message is "Add new line to README.md".
4. Switch to the `master` branch.
5. Merge the `feature-branch` into the `master` branch,which will create a merge commit with the message "Merge feature-branch".

This is the result of running `git log`:

```shell
ADD new line to README.md
```
