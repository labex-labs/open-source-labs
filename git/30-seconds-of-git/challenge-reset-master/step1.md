# Reset Local Master Branch to Match Remote

## Problem

You have been working on a project and have made changes to the local `master` branch. However, you realize that the remote `master` branch has been updated with new changes that you do not have in your local branch. You need to reset the local `master` branch to match the one on the remote.

## Example

1. Switch to the `master` branch.
2. Retrieve the latest updates from the remote.
3. View the commit history of the current branch.
4. Reset the local `master` branch to match the one on the remote.
5. Verify that the local `master` branch is now up to date with the remote `master` branch.

This is the finished result: 

```shell
commit d22f46ba8c2d4e07d773c5126e9c803933eb5898 (HEAD -> master, origin/master, origin/feature-branch, origin/HEAD)
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt

commit cf80005e40a3c661eb212fcea5fad06f8283f08f
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file1.txt

commit b00b9374a7c549d1af111aa777fdcc868d8a2a01
Author: Hang <huhuhang@gmail.com>
Date:   Wed Apr 26 14:16:00 2023 +0800

    Initial commit
```
