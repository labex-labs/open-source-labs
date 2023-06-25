# Edit the Last Commit

You have just committed some changes to your Git repository, but you realize that you forgot to include a file or make a small change. You don't want to create a new commit just for this small change, but you also don't want to change the commit message. How can you edit the last commit without changing its message?

To demonstrate how to edit the last commit, you will use the Git repository `git-playground` from your GitHub account, which comes from a fork of `https://github.com/labex-labs/git-playground.git`.

1. Clone the repository to your local machine:
```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
```
2. Realize that you forgot to include a file or make a small change. Add the text "New content" to the end of the `README.md` file. Add any staged changes to the last commit, without changing its message:
```shell
echo "New content" >> README.md
git add README.md
git commit --amend --no-edit
```
3. Verify that the last commit now includes the changes you made:
```shell
git show HEAD
```

This is the content of the late commit:
![result](./assets/challenge-update-commit-contents.png)
