# Find Branches Containing a Commit

You have been given a Git repository named `https://github.com/labex-labs/git-playground`. Your task is to find all branches that contain a hash with the commit message "Added file2.txt".

1. Change into the repository directory:
```shell
cd git-playground
```
2. Use the `git branch --contains` command to find all branches that contain a hash with the commit message "Added file2.txt":
```shell
git branch --contains d22f46b
```

The output should be:
```shell
* master
  new-branch
  new-branch-1
  new-branch-2
```
