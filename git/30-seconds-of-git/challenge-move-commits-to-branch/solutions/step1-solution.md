```shell
git branch <branch>
git reset HEAD~<n> --hard
git checkout <branch>
```

```shell
git checkout master
echo "hello" > file1.txt
git add .
git commit -m "Add new feature to master branch"
git branch feature-branch
# `feature-branch` branch is created containing the commit "Add new feature to master branch"
git reset HEAD~1 --hard # Remove the commit from `master`
git checkout feature-branch
git cherry-pick master
git log # Verify that the changes are now in `feature-branch`
```