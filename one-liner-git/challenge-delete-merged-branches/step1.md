# Delete Merged Branches

## Problem

Your task is to delete all local branches that have been merged into the `master` branch of the `https://github.com/labex-labs/git-playground` repository.

## Example

1. Clone the `https://github.com/labex-labs/git-playground` repository:
   ```shell
   git clone https://github.com/labex-labs/git-playground.git
   ```
2. Change to the repository directory:
   ```shell
   cd git-playground
   ```
3. List all branches:
   ```shell
   git branch
   ```
   Output:
   ```
   * master
     feature-1
     feature-2
     feature-3
   ```
4. Merge the `feature-1` branch into `master`:
   ```shell
   git checkout master
   git merge feature-1
   ```
5. Delete all merged branches:
   ```shell
   git branch --merged master | grep -v "(^\*|master)" | xargs git branch -d
   ```
6. List all branches again:
   ```shell
   git branch
   ```
   Output:
   ```
   * master
   ```
