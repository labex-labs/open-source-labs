# Find Branches Not Containing a Commit

## Problem

You are working on a project with multiple branches, and you need to find all the branches that do not contain a specific commit. This can be useful if you want to make sure that a certain change has been applied to all branches, or if you want to know which branches are outdated and need to be updated.

## Example

For this challenge, we will be using the Git repository named `https://github.com/labex-labs/git-playground`. Clone this repository to your local machine using the following command:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

Once you have cloned the repository, navigate to the directory using the following command:

```shell
cd git-playground
```

Now, let's say that we want to find all the branches that do not contain the commit with the hash `3050fc0d3`. To do this, we can use the following command:

```shell
git branch --no-contains 3050fc0d3
```

This will output a list of all the branches that do not contain the specified commit. In this case, the output will be:

```shell
patch-3
patch-4
```

This means that the `patch-3` and `patch-4` branches do not contain the commit with the hash `3050fc0d3`.
