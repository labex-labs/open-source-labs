# Delete a Branch

You have created a local branch in your Git repository, and you no longer need it. You want to delete the branch to keep your repository clean and organized.

1. Navigate to the cloned repository:
```shell
cd git-playground
```
2. View current branches:
```shell
git branch
```
3. Delete the `feature-1` branch:
```shell
git branch -d feature-1
```
4. Verify that the branch has been deleted:
```shell
git branch
```

This is the result of running the `git branch` command:
```
* master
```
