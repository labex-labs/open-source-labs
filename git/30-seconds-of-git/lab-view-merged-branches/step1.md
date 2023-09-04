# View Merged Branches

Your task is to print a list of all merged local branches in the Git repository named `https://github.com/labex-labs/git-playground`. You will need to use the command `git branch -a --merged` to display the list of merged branches. Once you have the list, you should be able to navigate through it using the arrow keys and exit by pressing <kbd>Q</kbd>.

1. Navigate to the repository directory:

```shell
cd git-playground
```

2. View the list of merged branches:

```shell
git branch -a --merged
```

This is the final result:

```
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/feature-branch
  remotes/origin/master
```
