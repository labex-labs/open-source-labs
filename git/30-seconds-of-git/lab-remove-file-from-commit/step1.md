# Git Challenge: Remove a File from the Last Commit

You have added a file to the last commit that you didn't intend to include. You want to remove the file from the last commit without changing its message.

Suppose you have a Git repository named `git-playground` with a file named `file.txt` that you accidentally added to the last commit. Here are the steps to remove the file from the last commit:

1. Use `git rm --cached <file>` to remove the specified `<file>` from the index.

```shell
git rm --cached file.txt
```

2. Use `git commit --amend` to update the contents of the last commit, without changing its message.

```shell
git commit --amend
```

After running these commands, the file `file.txt` will be removed from the last commit without changing its message.
