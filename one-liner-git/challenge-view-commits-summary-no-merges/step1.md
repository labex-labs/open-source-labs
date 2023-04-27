# View a Short Summary of Commits without Merge Commits

## Problem

You have been working on a project with several other developers, and you want to see a summary of all the commits made to the repository. However, you don't want to see the merge commits, as they don't contain any actual changes to the code. How can you view a summary of all the commits excluding merge commits?

## Example

To complete this challenge, you will need to use the Git repository named `https://github.com/labex-labs/git-playground`. Clone the repository to your local machine using the following command:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

Once you have cloned the repository, navigate to the directory using the following command:

```shell
cd git-playground
```

Now, to view a short summary of all commits excluding merge commits, use the following command:

```shell
git log --oneline --no-merges
```

This will output a list of all the commits made to the repository, excluding any merge commits. The output will look something like this:

```shell
3050fc0de Fix network bug
c191f90c7 Initial commit
```
