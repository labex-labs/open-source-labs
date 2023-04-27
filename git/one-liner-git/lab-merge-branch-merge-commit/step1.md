# Merge a Branch and Create a Merge Commit

As a developer, you may need to merge a branch into the current branch, creating a merge commit. This can be a bit tricky if you're not familiar with Git. The problem is to merge a branch into the current branch, creating a merge commit, using the Git repository named `https://github.com/labex-labs/git-playground` directory.

Suppose you are working on a project with a team of developers, and you need to merge a branch named `feature-branch` into the `master` branch. Here are the steps you would take:

1. First, you need to switch to the `master` branch using the following command:

```
git checkout master
```

2. Next, you need to merge the `feature-branch` into the `master` branch using the following command:

```
git merge --no-ff -m "Merge feature-branch" feature-branch
```

This will merge the `feature-branch` into the `master` branch, creating a merge commit with the message "Merge feature-branch".
