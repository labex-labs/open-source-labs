# Find Branches Containing a Commit

## Problem

You have been given a Git repository named `https://github.com/labex-labs/git-playground`. Your task is to find all the branches that contain the commit with the hash `3050fc0d3`.

## Example

1. Clone the repository using the following command:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Change into the repository directory:

```shell
cd git-playground
```

3. Use the `git branch --contains` command to find all the branches containing the commit with the hash `3050fc0d3`:

```shell
git branch --contains 3050fc0d3
```

4. The output should be:

```shell
patch-1
patch-2
```
