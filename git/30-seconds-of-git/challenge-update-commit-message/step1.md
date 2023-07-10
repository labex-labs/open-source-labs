# Change the Last Commit's Message

## Problem

Imagine you have just committed some changes to your Git repository, but you realize that you made a typo in the commit message. You want to correct the mistake without changing the actual changes you made. How can you do this?

## Example

To demonstrate how to change the last commit's message, you will use the Git repository `git-playground` from your GitHub account, which comes from a fork of `https://github.com/labex-labs/git-playground.git`.

1. Clone the repository to your local machine.
2. Navigate to the repository directory.
3. Correct the commit message of the last commit to read "Fix the network bug".
4. Verify that the commit message has been changed.

You should see the updated commit message in the log:
```
54b830b (HEAD -> master) Fix the network bug
cf80005 Added file1.txt
b00b937 Initial commit
```
