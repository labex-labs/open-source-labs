# Rename Remote Branch

To complete this lab, you will use the Git repository `git-playground` from your GitHub account, which comes from a fork of `https://github.com/labex-labs/git-playground.git`. Please uncheck "Copy master branch only" when forking. 

You have a Git repository named `https://github.com/your-username/git-playground`. You have created a branch named `feature-branch` and pushed it to the remote. Now you want to rename the branch to `new-feature-1` both locally and on the remote.

1. Clone the repository, navigate to the directory and configure the identity:
   ```shell
   git clone https://github.com/your-username/git-playground.git
   cd git-playground
   git config --global user.name "your-username"
   git config --global user.email "your-email"
   ```
2. Switch to the named `feature-branch` branch:
   ```shell
   git checkout feature-branch
   ```
3. Rename the branch both locally and on the remote:
   ```shell
   git branch -m feature-branch new-feature-1
   git push origin --delete feature-branch
   git push -u origin new-feature-1
   ```
4. Verify that the branch has been renamed:
   ```shell
   git branch -a
   ```

This is the result of running `git branch -a`:
   ```shell
   * master
     new-feature-1
     remotes/origin/HEAD -> origin/master
     remotes/origin/master
     remotes/origin/new-feature-1
   ```
