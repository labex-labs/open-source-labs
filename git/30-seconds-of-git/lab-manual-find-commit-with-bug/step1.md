# Manually Find the Commit that Introduced a Bug

Your task is to manually find the commit that introduced a bug in the `git-playground` repository. The repository can be found at `https://github.com/labex-labs/git-playground`. The bug is that the `file2.txt` file should print "This is file2.txt." instead of "This is file2.".

To complete this lab, you will need to use the `git bisect` command to perform a binary search through the commit history of the repository. You will need to mark commits as either "good" (bug-free) or "bad" (buggy) until you have narrowed down the commit that introduced the bug.

1. Change into the repository directory:

```
cd git-playground
```

2. Start the `git bisect` process:

```
git bisect start
```

3. Mark the current commit as "bad":

```
git bisect bad HEAD
```

4. Mark a commit with the message "Initial commit" as "good". Git will automatically checkout a new commit for you to test:

```
git bisect good 3050fc0de
```

Git will automatically checkout a new commit for you to test. 5. If the contents of the checked `file2.txt` file do not match the bug, mark it as "good":

```
cat file2.txt
git bisect good
```

6. If the contents of the checked `file2.txt` file match the bug, mark it as "bad":

```
git bisect bad
```

7. Once you have found the buggy commit, reset the `git bisect` process:

```
git bisect reset
```

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
