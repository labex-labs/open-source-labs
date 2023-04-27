# Delete Detached Branches

## Problem

You have a Git repository with several detached branches that you no longer need. These branches are cluttering your repository and making it difficult to manage. You want to delete all detached branches to clean up your repository.

## Example

Assuming you have a Git repository named `https://github.com/labex-labs/git-playground`, follow these steps to delete all detached branches:

1. Open your terminal and navigate to the local directory of the Git repository.
2. Run the command `git fetch --all --prune` to garbage collect any detached branches.
3. This command will remove all detached branches from your local repository.
4. To verify that the detached branches have been deleted, run the command `git branch`.
5. The output should only show the branches that are associated with a specific branch, such as `master` or `develop`.

```shell
$ git clone https://github.com/labex-labs/git-playground.git
$ cd git-playground
$ git fetch --all --prune
$ git branch
* master
```
