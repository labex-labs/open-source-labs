# Git Cherry-Pick

## Problem

As a developer, you are working on a project with multiple branches. You have identified a specific change that was made in a previous commit that you would like to apply to your current branch. However, you do not want to merge the entire branch as it contains other changes that you do not need.

## Example

To complete this challenge, you will use the Git repository `git-playground` from your GitHub account, which comes from a fork of `https://github.com/labex-labs/git-playground.git`.

1. Clone the repository, navigate to the directory and configure the identity.
2. Create and switch to a branch called `one-branch`, create a file called `hello.txt`, write "hello,world" in it, add it to the staging area and commit it with the message "add hello.txt".
3. Identify the hash of the commit created in the previous step to apply to the `master` branch.
4. Checkout the `master` branch and apply the change to the `master` branch.
5. Verify that the change has been applied to the `master` branch.

This is the result of running `git log` on the `master` branch:
```shell
commit e2f3c6af9570f4eac2580dea93ca8133f1547d53 (HEAD -> master)
Author: xiaoshengyunan <1797063828@qq.com>
Date:   Sat Jul 15 14:30:31 2023 +0800

    add hello.txt

commit d22f46ba8c2d4e07d773c5126e9c803933eb5898 (origin/master, origin/HEAD)
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

