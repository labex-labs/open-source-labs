# View "Undo" History

As a developer, you may need to undo changes that you've made to your codebase. Git provides several ways to undo changes, such as using the `git reset` or `git revert` commands. However, it can be difficult to keep track of all the actions you've taken, especially if you've used more advanced commands like `git rebase`. This is where the `git reflog` command comes in handy.

The `git reflog` command displays the Git reference log, which is a record of all the actions you've taken in your repository. This includes not only commits, but also other actions like branch merges, rebases, and resets. By viewing the reference log, you can see a complete history of all the changes you've made to your repository, even if they don't show up in the commit history.

To view the "undo" history in Git, you can use the `git reflog` command. Let's say you've made some changes to a repository and want to undo them.

1. Navigate to the repository using the command line:

```shell
cd git-playground
```

2. Now, let's say you realize that you made a mistake and want to undo the last commit. You can use the `git reset` command to do this:

```shell
git reset HEAD~1
```

3. After running this command, you may realize that you've made another mistake and want to undo the reset. This is where the `git reflog` command comes in handy. You can use it to view the reference log and find the commit hash of the previous commit:

```shell
git reflog
```

This will display a list of all the actions you've taken in the repository, including the reset:

```shell
cf80005 (HEAD -> master) HEAD@{0}: reset: moving to HEAD~1
d22f46b (origin/master, origin/feature-branch, origin/HEAD) HEAD@{1}: clone: from https://github.com/labex-labs/git-playground.git
```

4. From this output, you can see that the previous commit hash is `d22f46b`. You can use this hash to reset the repository back to the previous commit:

```shell
git reset d22f46b
```

5. View historical commit records to verify results:

```shell
git log
```
