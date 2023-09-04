# Find Branches Not Containing a Commit

## Problem

You are working on a project with multiple branches, and you need to find all the branches that do not contain a specific commit. This can be useful if you want to make sure that a certain change has been applied to all branches, or if you want to know which branches are outdated and need to be updated.

## Example

For this challenge, we will be using the Git repository named `https://github.com/your-username/git-playground`.

1. Clone this repository to your local machine.
2. Once you have cloned the repository, navigate to the directory.
3. Create and switch to a `new-branch` branch and make some code changes on that branch and then commit it, the commit message is "Create a new-branch branch".
4. Check the hash of the commit message "Create a new-branch branch".
5. Finds all branches that do not contain a hash with the commit message "Create a new-branch branch".

This will output a list of all the branches that do not contain the specified commit. In this case, the output will be:

```shell
master
```

This means that the `master` branch do not contain the commit with the hash `31c5ac20129151af1`.
