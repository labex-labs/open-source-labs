# Remove a File from the Last Commit

You have added a file to the last commit that you didn't intend to include. You want to remove the file from the last commit without changing its message.

To complete this lab, you will use the Git repository `git-playground` from your GitHub account, which comes from a fork of `https://github.com/labex-labs/git-playground.git`. Suppose you have a Git repository named `git-playground` with a file named `file1.txt` that you accidentally added to the last commit. Here are the steps to remove the file from the last commit:

1. Clone the repository and navigate the directory:
```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
```
2. Create the `git-playground.txt` file and modify the `file1.txt` file and add them to the staging area at the same time, committing them with the message "add git-playground.txt":
```shell
echo "hello" > file1.txt
echo "world" > git-playground.txt
git add .
git commit -m "add git-playground.txt"
```
3. Use `git rm --cached <file>` to remove the specified `<file>` from the index:
```shell
git rm --cached file1.txt
```
4. Use `git commit --amend` to update the contents of the last commit, without changing its message:
```shell
git commit --amend
```

After running these commands, the file `file1.txt` will be removed from the last commit without changing its message.

This is what happens when you remove `file1.txt` from Git version control:

![<result>](./assets/challenge-remove-file-from-commit-step1-1.png)
