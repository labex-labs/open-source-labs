# Create a Fixup Commit

## Problem

Suppose you are working on a project with several other developers, and you notice a small error in a commit that was made a few days ago. You want to fix the error, but you don't want to create a new commit and disrupt the work of the other developers. This is where fixup commits come in handy. By creating a fixup commit, you can make the necessary changes without creating a new commit, and the fixup commit will be automatically merged with the original commit during the next rebase.

## Example

Your task is to write the "hello,world" string to the `hello.txt` file and add it to the most recent commits as a "fixup" commit to be automatically merged in subsequent rebase operations. The most recent commit is the one with the commit message "Added file1.txt".

To complete this challenge, you will use the Git repository `git-playground` from your GitHub account, which comes from a fork of `https://github.com/labex-labs/git-playground.git`.

1. Create a `hello.txt` file, write "hello,world" in it and add it to the staging area.
2. Create a fixup commit for the hash of the "Added file1.txt" commit message.
3. Once you have created the fixup commit, you can automatically merge the fixup commit with the original commit during the next rebase. When opening the interactive editor, you don't need to change the text and save to exit.

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
