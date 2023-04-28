# View a Short Summary of Commits

## Problem

As a developer, you are working on a project with multiple contributors. You need to view a summary of all the commits made to the project to understand the changes that have been made and to identify any potential issues. However, you don't want to spend a lot of time sifting through all the commit messages to find the information you need.

## Example

To view a short summary of all the commits made to a Git repository, you can use the `git log --oneline` command. For example, let's say you are working on a project hosted on GitHub called `git-playground`. You can clone the repository to your local machine using the following command:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

Once you have cloned the repository, navigate to the project directory and run the following command to view a short summary of all the commits:

```shell
git log --oneline
```

This will output a list of all the commits made to the repository, along with a short summary of each commit message. For example:

```shell
d540ba1ab Merge network bug fix
3050fc0de Fix network bug
c191f90c7 Initial commit
```
