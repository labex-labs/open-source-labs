# Edit the Last Commit

You have just committed some changes to your Git repository, but you realize that you forgot to include a file or make a small change. You don't want to create a new commit just for this small change, but you also don't want to change the commit message. How can you edit the last commit without changing its message?

To demonstrate how to edit the last commit, let's use the repository from `https://github.com/labex-labs/git-playground`.

1. Clone the repository, navigate to the directory and configure the identity:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
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
![Updated commit contents display](./assets/challenge-update-commit-contents.png)
