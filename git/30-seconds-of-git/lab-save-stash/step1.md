# Create a Git Stash

As a developer, you may find yourself in a situation where you need to switch to a different branch or work on a different feature, but you're not ready to commit your changes yet. You don't want to lose your progress, but you also don't want to commit incomplete or buggy code. This is where a stash comes in handy.

A stash allows you to save your changes without committing them, so you can switch to a different branch or work on a different feature. You can then apply your stash later when you're ready to continue working on your changes.

To create a stash, you can use the `git stash save` command. Let's say you're working on a branch named `feature` in the `git-playground` repository and you want to save your changes before switching to a different branch:

1. First, navigate to the `git-playground` directory:
```shell
cd git-playground
```
2. Switch to a branch named `feature`:
```shell
git checkout -b feature
```
3. Make some changes to the files in the directory:
```shell
echo "Some changes" >> README.md
```
4. Save your changes to a stash:
```shell
git stash save "My changes"
```
5. Switch to a different branch:
```shell
git checkout master
```
6. When done making changes on the other branch, switch back to the `feature` branch and apply your stash:
```shell
git stash apply
```

This is the finished result:
```shell
stash@{0}: On feature: My changes
```

