# Reset Local Master Branch to Match Remote

You have been working on a project and have made changes to the local `master` branch. However, you realize that the remote `master` branch has been updated with new changes that you do not have in your local branch. You need to reset the local `master` branch to match the one on the remote.

1. Switch to the `master` branch:
   ```shell
   git checkout master
   ```
2. Retrieve the latest updates from the remote:
   ```shell
   git fetch origin
   ```
3. View the commit history of the current branch:
   ```shell
   git log
   ```
4. Reset the local `master` branch to match the one on the remote:
   ```shell
   git reset --hard origin/master
   ```
5. Verify that the local `master` branch is now up to date with the remote `master` branch:
   ```shell
   git log
   ```

This is the finished result:

```shell
[object Object]
```
