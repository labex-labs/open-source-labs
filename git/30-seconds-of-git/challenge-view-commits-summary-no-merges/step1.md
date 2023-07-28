# View a Short Summary of Commits without Merge Commits

## Problem

You have been working on a project with several other developers, and you want to see a summary of all the commits made to the repository. However, you don't want to see the merge commits, as they don't contain any actual changes to the code. How can you view a summary of all the commits excluding merge commits?

## Example

For this challenge, let's use the repository from `https://github.com/labex-labs/git-playground`.

1. Navigate to the directory and configure the identity.
2. Create and switch to a branch called `feature1`, create a file called `file.txt` and write `feature 1` into it, add it to the staging area and commit it with the message "Add feature 1".
3. Switch back to the `master` branch, merge the `feature1` branch, disable the forward merge, save and exit without changing the text.
4. View a short summary of all commits excluding merge commits.

This will output a list of all the commits made to the repository, excluding any merge commits. The output will look something like this:
```shell
430b986 (feature1) Add feature 1
d22f46b (origin/master, origin/HEAD) Added file2.txt
cf80005 Added file1.txt
b00b937 Initial commit
```
