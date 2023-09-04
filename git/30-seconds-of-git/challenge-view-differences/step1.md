# View Differences in Changes

## Problem

As a developer, you may want to view the differences between your staged or unstaged changes and the last commit. This is useful when you want to review your changes before committing them or when you want to see what changes you have made since the last commit.

## Example

To demonstrate how to view differences in changes, we will use the `git-playground` repository. Suppose you have made some changes to the `README.md` file and want to view the differences between your changes and the last commit.

1. Open your terminal and navigate to the `git-playground` directory.
2. View the differences between your unstaged changes and the last commit.
3. View the differences between your staged changes and the last commit.

This is the result of completing step 2：

```
diff --git a/file1.txt b/file1.txt
index bfccc4a..ee23125 100644
--- a/file1.txt
+++ b/file1.txt
@@ -1 +1,2 @@
 This is file1.
+hello,labex
```

This is the result of completing step 3：

```
diff --git a/README.md b/README.md
index 0164284..f47591b 100644
--- a/README.md
+++ b/README.md
@@ -1,2 +1,3 @@
 # git-playground
 Git Playground
+hello,world
```
