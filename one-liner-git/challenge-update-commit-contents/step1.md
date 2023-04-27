# Git Challenge: Edit the Last Commit

## Problem

You have just committed some changes to your Git repository, but you realize that you forgot to include a file or make a small change. You don't want to create a new commit just for this small change, but you also don't want to change the commit message. How can you edit the last commit without changing its message?

## Example

To demonstrate how to edit the last commit, we will use the Git repository named `https://github.com/labex-labs/git-playground`.

1. Clone the repository to your local machine:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Make some changes to a file in the repository:

```shell
cd git-playground
echo "New content" >> README.md
git add README.md
git commit -m "Initial commit"
```

3. Realize that you forgot to include a file or make a small change. Use the following command to add any staged changes to the last commit, without changing its message:

```shell
git commit --amend --no-edit
```

4. Verify that the last commit now includes the changes you made:

```shell
git log --oneline
```
