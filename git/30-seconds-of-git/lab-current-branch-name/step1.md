# Get the Current Branch Name

Write a command that prints the name of the current branch in a Git repository.

Suppose you're working on a project stored in the `https://github.com/labex-labs/git-playground` repository. You've made some changes to the `README.md` file and want to commit them to the current branch. However, before doing so, you want to make sure you're on the correct branch.

To check the current branch, you can use the following command:

```shell
git rev-parse --abbrev-ref HEAD
```

This will print the name of the current branch to the console. For example, if you're currently on the `master` branch, the output will be:

```shell
master
```

If you switch to a different branch, such as `feature-branch`, the output will change accordingly:

```shell
git checkout -b feature-branch
git rev-parse --abbrev-ref HEAD
```

This will output:

```shell
feature-branch
```
