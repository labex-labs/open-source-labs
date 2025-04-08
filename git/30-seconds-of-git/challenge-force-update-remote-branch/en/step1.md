# Update Remote Branch After Rewriting History

When you rewrite history locally, you create a new commit with a different SHA-1 hash. This means that the commit history on your local branch is different from the commit history on the remote branch. If you try to push your changes to the remote branch, Git will reject the push because it will see the commit history as diverged. To solve this problem, you need to force an update of the remote branch.

## Tasks

To complete this challenge, you will use the Git repository `git-playground` from your GitHub account, which comes from a fork of `https://github.com/labex-labs/git-playground.git`.

1. Clone the `git-playground` repository to your local machine.
2. Update a commit with the message "Added file2.txt" to a commit with the message "Update file2.txt".
3. Push changes from local branch to remote repository.
4. If you can't push it successfully, please force push it.

This is the final result:

```shell

```
