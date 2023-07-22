# Remove a File from the Last Commit

You have added a file to the last commit that you didn't intend to include. You want to remove the file from the last commit without changing its message.

For this lab, let's use the repository from `https://github.com/labex-labs/git-playground`. Suppose you have a Git repository named `git-playground` with a file named `file2.txt` that you accidentally added to the last commit. Here are the steps to remove the file from the last commit:

1. Clone the repository, navigate to the directory and configure the identity:
```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```
2. Use `git rm --cached <file>` to remove the specified `<file>` from the index:
```shell
git rm --cached file2.txt
```
3. Use `git commit --amend` to update the contents of the last commit, without changing its message:
```shell
git commit --amend --allow-empty
```
If the commit is an empty commit after deleting the file, use `--allow-empty`, otherwise you can leave it out.

After running these commands, the file `file2.txt` will be removed from the last commit without changing its message.

This is what happens when you remove `file2.txt` from Git version control:
```shell
On branch master

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        deleted:    file2.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        file2.txt
```