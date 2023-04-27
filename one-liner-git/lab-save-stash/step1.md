# Create a Git Stash

As a developer, you may find yourself in a situation where you need to switch to a different branch or work on a different feature, but you're not ready to commit your changes yet. You don't want to lose your progress, but you also don't want to commit incomplete or buggy code. This is where a stash comes in handy.

A stash allows you to save your changes without committing them, so you can switch to a different branch or work on a different feature. You can then apply your stash later when you're ready to continue working on your changes.

To create a stash, you can use the `git stash save` command. Let's say you're working on a feature branch in the `git-playground` repository and you want to save your changes before switching to a different branch:

1. First, navigate to the `git-playground` directory:

```shell
cd git-playground
```

2. Make some changes to the files in the directory:

```shell
echo "Some changes" >> README.md
```

3. Save your changes to a stash:

```shell
git stash save "My changes"
```

4. Switch to a different branch:

```shell
git checkout master
```

5. Apply your stash:

```shell
git stash apply
```
