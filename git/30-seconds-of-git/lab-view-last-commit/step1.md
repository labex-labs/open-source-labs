# View Last Commit

## Problem

You are working on a project with a team of developers, and you need to view the last commit made to the project's Git repository. You want to see the details of the commit, including the commit message, author, and date.

## Example

To view the last commit made to a Git repository, follow these steps:

1. Open the terminal on your computer.
2. Navigate to the directory where the Git repository is located:
```shell
cd git-playground
```
3. View the last commit:
```shell
git log -l
```

The output will show you the details of the last commit, including the commit message, author, and date:
```shell
commit d22f46ba8c2d4e07d773c5126e9c803933eb5898 (HEAD -> master, origin/master, origin/feature-branch, origin/HEAD)
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt
```
