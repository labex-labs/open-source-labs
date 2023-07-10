# Delete Merged Branches

Your task is to delete all local branches that have been merged into the `master` branch of the `https://github.com/labex-labs/git-playground` repository.

1. Change to the repository directory:
```shell
cd git-playground
```
2. List all local branches that have been merged into `master`:
```shell
git branch --merged
```
Output:
```
* master
  new-branch
  new-branch-1
  new-branch-2
  new-branch-3
```
3. Delete all merged branches:
```shell
git branch --merged master | awk '!/^[ *]*$/ && !/master/ {print $1}' | xargs git branch -d
```
4. List all branches again:
```shell
git branch
```

This is the final result:
```
* master
```
