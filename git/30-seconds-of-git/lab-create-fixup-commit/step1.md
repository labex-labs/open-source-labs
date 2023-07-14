# Create a Fixup Commit

Suppose you are working on a project with several other developers, and you notice a small error in a commit that was made a few days ago. You want to fix the error, but you don't want to create a new commit and disrupt the work of the other developers. This is where fixup commits come in handy. By creating a fixup commit, you can make the necessary changes without creating a new commit, and the fixup commit will be automatically merged with the original commit during the next rebase.

For example, your task is to write the string "hello,world" to the `hello.txt` file and add it as a "fixup" commit to one of the previous commits, so that it can be automatically merged in a subsequent rebase operation. This previous commit is the commit with the message "Added file1.txt".

To complete this lab, you will use the Git repository `git-playground` from your GitHub account, which comes from a fork of `https://github.com/labex-labs/git-playground.git`.

1. Clone the repository, navigate to the directory and configure the identity:
```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```
2. Create a `hello.txt` file, write "hello,world" in it and add it to the staging area:
```shell
echo "hello,world" > hello.txt
git add .
```
3. To create a fixup commit, you can use the `git commit --fixup <commit>` command:
```shell
git commit --fixup cf80005
# This is the hash of the commit message "Added file1.txt".
```
This will create a fixup commit for the specified commit. Note that you must stage your changes before creating the fixup commit.
4. Once you have created the fixup commit, you can use the `git rebase --interactive --autosquash` command to automatically merge the fixup commit with the original commit during the next rebase. For example:
```shell
git rebase --interactive --autosquash HEAD~3
```
When opening the interactive editor, you don't need to change the text and save to exit. This will perform a rebase on the last 3 commits, and automatically merge any fixup commits with their corresponding original commits.

This is the result of running the `git show HEAD~1` command:
```shell
commit 6f0b8bbfac939af197a44ecd287ef84153817e9d
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file1.txt

diff --git a/file1.txt b/file1.txt
new file mode 100644
index 0000000..bfccc4a
--- /dev/null
+++ b/file1.txt
@@ -0,0 +1 @@
+This is file1.
diff --git a/hello.txt b/hello.txt
new file mode 100644
index 0000000..2d832d9
--- /dev/null
+++ b/hello.txt
@@ -0,0 +1 @@
+hello,world
```
