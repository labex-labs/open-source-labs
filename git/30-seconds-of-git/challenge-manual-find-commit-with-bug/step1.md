# Manually Find the Commit that Introduced a Bug

## Problem

Your task is to manually find the commit that introduced a bug in the `git-playground` repository. The repository can be found at `https://github.com/labex-labs/git-playground`.

To complete this challenge, you will need to perform a binary search through the commit history of the repository. You will need to mark commits as either "good" (bug-free) or "bad" (buggy) until you have narrowed down the commit that introduced the bug.

## Example

The error message is that the `file2.txt` file should print "This is file2.txt." instead of "This is file2.".

1. Change into the repository directory.
2. Start a binary search.
3. Mark the current commit as "bad".
4. Mark a commit with the message "Initial commit" as "good". Git will automatically checkout a new commit for you to test.
5. If the contents of the checked `file2.txt` file do not match the bug, mark it as "good".
6. If the contents of the checked `file2.txt` file match the bug, mark it as "bad".
7. Once you have found the buggy commit, exit the binary search.

You can now examine the code changes in the buggy commit to find the source of the bug.

This is the result of the test:

```
d22f46ba8c2d4e07d773c5126e9c803933eb5898 is the first bad commit
commit d22f46ba8c2d4e07d773c5126e9c803933eb5898
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt

 file2.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 file2.txt
```
