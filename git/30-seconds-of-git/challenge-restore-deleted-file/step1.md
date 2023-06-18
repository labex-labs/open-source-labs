# Restore a Deleted File

## Problem

You are working on a project using Git and accidentally deleted a file that you need. Fortunately, you know the commit where the file was deleted. Your task is to restore the deleted file using Git.

## Example

To complete this experiment, you will use the Git repository `git-playground` from `https://github.com/labex-labs/git-playground.git`.

1. Identifies a commit where a file was deleted with the message "Added file2.txt".
2. Restore the deleted file by checking out the commit before the deletion.

This will restore the `file2.txt` file to your local repository.

This is the result of running the `ll` command:
```shell
total 12K
-rw-r--r-- 1 labex labex 15 Jun 18 18:05 file1.txt
-rw-r--r-- 1 labex labex 15 Jun 18 18:13 file2.txt
-rw-r--r-- 1 labex labex 32 Jun 18 18:05 README.md
```
