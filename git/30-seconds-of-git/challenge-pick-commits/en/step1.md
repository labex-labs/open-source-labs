# Git Cherry-Pick

As a developer, you are working on a project with multiple branches. You have identified a specific change that was made in a previous commit that you would like to apply to your current branch. However, you do not want to merge the entire branch as it contains other changes that you do not need.

## Tasks

For this challenge, let's use the repository from `https://github.com/labex-labs/git-playground`.

1. Navigate to the directory and configure the identity.
2. Create and switch to a branch called `one-branch`, create a file called `hello.txt`, write "hello,world" in it, add it to the staging area and commit it with the message "add hello.txt".
3. Identify the hash of the commit created in the previous step to apply to the `master` branch.
4. Checkout the `master` branch and apply the change to the `master` branch.
5. Verify that the change has been applied to the `master` branch.

This is the result of running `git log` on the `master` branch:

```shell
ADD hello.txt
```
