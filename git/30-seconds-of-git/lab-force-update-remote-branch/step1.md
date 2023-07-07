# Update Remote Branch After Rewriting History

When you rewrite history locally, you create a new commit with a different SHA-1 hash. This means that the commit history on your local branch is different from the commit history on the remote branch. If you try to push your changes to the remote branch, Git will reject the push because it will see the commit history as diverged. To solve this problem, you need to force an update of the remote branch.

To complete this challenge, you will use the Git repository `git-playground` from your GitHub account, which comes from a fork of `https://github.com/labex-labs/git-playground.git`.

1. Clone the `git-playground` repository to your local machine:
```shell
git clone https://github.com/your-username/git-playground.git
```
2. Update the previous commit message to "Update file2.txt":
```shell
git commit --amend
```
3. Push changes from local branch to remote repository:
```shell
git push
```
4. If you can't push it successfully, please force push it:
```shell
git push -f origin master
```
The `-f` flag forces Git to update the remote branch with your changes, even though the commit history has diverged.

This is the final result:
```shell
commit 7d87e34194c7530f97a11f74c7d90e2eb71d315f (HEAD -> master, origin/master, origin/HEAD)
Author: xiaoshengyunan <1797063828@qq.com>
Date:   Mon Jul 3 15:31:29 2023 +0800

    Update file2.txt

commit cf80005e40a3c661eb212fcea5fad06f8283f08f (origin/rewind-commits)
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file1.txt

commit b00b9374a7c549d1af111aa777fdcc868d8a2a01
Author: Hang <huhuhang@gmail.com>
Date:   Wed Apr 26 14:16:00 2023 +0800

    Initial commit
```

