# Update Remote Branch After Rewriting History

When you rewrite history locally, you create a new commit with a different SHA-1 hash. This means that the commit history on your local branch is different from the commit history on the remote branch. If you try to push your changes to the remote branch, Git will reject the push because it will see the commit history as diverged. To solve this problem, you need to force an update of the remote branch.

To complete this lab, you will use the Git repository `git-playground` from your GitHub account, which comes from a fork of `https://github.com/labex-labs/git-playground.git`.

1. Clone the `git-playground` repository to your local machine:

```shell
git clone https://github.com/your-username/git-playground.git
```

2. Update a commit with the message "Added file2.txt" to a commit with the message "Update file2.txt":

```shell
git commit --amend
```

3. Push changes from local branch to remote repository:

```shell
git push
```

4. If you can't push it successfully, please force push it:

```shell
git push -f origin master
```

The `-f` flag forces Git to update the remote branch with your changes, even though the commit history has diverged.

This is the final result:

```shell

```
