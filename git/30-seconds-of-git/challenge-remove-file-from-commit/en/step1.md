# Remove a File from the Last Commit

You have added a file to the last commit that you didn't intend to include. You want to remove the file from the last commit without changing its message.

## Tasks

For this challenge, let's use the repository from `https://github.com/labex-labs/git-playground`. Suppose you have a Git repository named `git-playground` with a file named `file2.txt` that you accidentally added to the last commit.

1. Navigate to the repository directory and configure your GitHub identity .
2. Remove the specified `file2.txt` from the index.
3. Update the contents of the last commit, without changing its message.

After running these commands, the file `file2.txt` will be removed from the last commit without changing its message.

This is what happens when you remove `file2.txt` from Git version control:

```shell
On branch master

Changes to be committed:
(use "git restore --staged <file>..." to unstage)
deleted: file2.txt

Untracked files:
(use "git add <file>..." to include in what will be committed)
file2.txt
```
