# Delete Detached Branches

You have a Git repository with several detached branches that you no longer need. These branches are cluttering your repository and making it difficult to manage. You want to delete all detached branches to clean up your repository.

To complete this lab, you will use the Git repository `git-playground` from your GitHub account, which comes from a fork of `https://github.com/labex-labs/git-playground.git`. Do not check "Copy the master branch only".

1. Clone the repository, navigate to the directory and configure the identity:

```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Since there is a `feature-branch` branch in the remote repository, switch to `feature-branch`, which will cause the local `feature-branch` to track the `feature-branch` branch of the remote repository and delete the `feature-branch` branch in the remote repository: 

```shell
git checkout feature-branch
git push origin --delete feature-branch
```

3. View the trace relationship between local branches and the remote branches they track:

```shell
git branch -vv
```

4. Switch back to the `master` branch:

```shell
git checkout master
```

5. Remove all detached branches from your local repository:

```shell
git branch -vv | grep ': gone]' | awk '{print $1}' | xargs git branch -D
```

6. Verify that the detached branches have been deleted:

```shell
git branch
```

The output should only show the branches that are associated with a specific branch:

```shell
* master d22f46b [origin/master] Added file2.txt
```
