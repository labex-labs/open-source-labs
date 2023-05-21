# Delete a Branch

## Problem

You have created a local branch in your Git repository, and you no longer need it. You want to delete the branch to keep your repository clean and organized.

## Example

1. Clone the `git-playground` repository using the following command:
```shell
git clone https://github.com/labex-labs/git-playground.git
```
2. Navigate to the cloned repository:
```shell
cd git-playground
```
3. Create a new branch named `feature-1` and switch to it:
```shell
git checkout -b feature-1
```
4. Verify that the branch has been deleted:
5. Switch back to the `master` branch:
```shell
git checkout master
```
6. Delete the `feature-1` branch:
```shell
git branch -d feature-1
```
7. Verify that the branch has been deleted:
```shell
git branch
```

Output:

```
* master
```
