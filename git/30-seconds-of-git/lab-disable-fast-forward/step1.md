# Disable Fast Forward Merging

By default, Git uses fast forward merging to merge branches that have no divergent commits. This means that if you have a branch with no new commits, Git will simply move the pointer of the branch you are merging into to the latest commit of the branch you are merging from. While this can be useful in some cases, it can also cause issues, especially when working on larger projects with multiple contributors. For example, if two developers are working on the same branch and both make changes, fast forward merging can cause conflicts that are difficult to resolve.

To disable fast forward merging, let's use the repository from `https://github.com/labex-labs/git-playground`.

1. Clone the repository, navigate to the directory and configure the identity:
```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```
2. Create and switch to a branch called `my-branch`, create a `hello.txt` file and add "hello,world" to it, add it to the staging area and commit it with the message "Added hello.txt":
```shell
git checkout -b my-branch
echo "hello,world" > hello.txt
git add .
git commit -m "Added hello.txt"
```
3. Run the following command to disable fast forward merging:
```shell
git config --add merge.ff false
```
This will disable fast forward merging for all branches, even if it is possible. You can use the `--global` flag to configure this option globally:
```shell
git config --global --add merge.ff false
```
4. Switch back to the `mater` branch and merge the `my-branch` branch, save and exit without changing the text:
```shell
git checkout master
git merge my-branch
```

Now, Git will always create a merge commit, even if it is possible to fast forward:
```shell
commit 6e17a776ab51a89ace069614b0caf1c07915a92c (HEAD -> master)
Merge: ec5ea6d 6d7de91
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Mon Jul 17 13:30:44 2023 +0800

    Merge branch 'my-branch'
```
