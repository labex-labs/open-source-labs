# Copy a File from Another Branch

## Problem

You are working on a project in a Git repository named `https://github.com/labex-labs/git-playground.git`. You have two branches named `feature-1` and `feature-2`. You need to copy the file `hello.txt` from `feature-1` branch to `feature-2` branch.

## Example

1. Navigate to the directory and configure the identity.
2. Create and switch to `feature-1` branch and create a text file named `hello.txt` and write the string "hello,world" to it and commit the file with the message "add hello.txt".
3. Create and switch to `feature-2` branch after switching to `master` branch.
4. Copy the `hello.txt` file from the `feature-1` branch to the `feature-2` branch and commit it with the commit message "copy hello.txt".
5. Verify that the `hello.txt` file has been copied to `feature-2` branch.

You should see the `hello.txt` file in the list of files in the `feature-2` branch:
```
-rw-r--r-- 1 labex labex 15 Jul 12 22:43 file1.txt
-rw-r--r-- 1 labex labex 15 Jul 12 22:43 file2.txt
-rw-r--r-- 1 labex labex 12 Jul 12 22:50 hello.txt
-rw-r--r-- 1 labex labex 32 Jul 12 22:43 README.md
```
