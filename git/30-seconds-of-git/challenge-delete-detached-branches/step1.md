# Delete Detached Branches

## Problem

You have a Git repository with several detached branches that you no longer need. These branches are cluttering your repository and making it difficult to manage. You want to delete all detached branches to clean up your repository.

## Example

To complete this challenge, you will use the Git repository `git-playground` from your GitHub account, which comes from a fork of `https://github.com/labex-labs/git-playground.git`. Do not check "Copy the master branch only".

1. Clone the repository, navigate to the directory and configure the identity.
2. Since there is a `feature-branch` branch in the remote repository, switch to `feature-branch`, which will cause the local `feature-branch` to track the `feature-branch` branch of the remote repository and delete the `feature-branch` branch in the remote repository.
3. View the trace relationship between local branches and the remote branches they track.
4. Switch back to the `master` branch.
5. Remove all detached branches from your local repository.
6. Verify that the detached branches have been deleted.

The output should only show the branches that are associated with a specific branch:
```shell
* master d22f46b [origin/master] Added file2.txt
```
