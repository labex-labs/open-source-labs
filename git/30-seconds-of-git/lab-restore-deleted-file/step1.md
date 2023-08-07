# Restore a Deleted File

You are working on a project using Git and accidentally deleted a file named `file2.txt` that you need. Fortunately, you know the commit where the file was deleted. Your task is to restore the deleted file using Git.

To complete this lab, you will use the Git repository `git-playground` from `https://github.com/labex-labs/git-playground.git`. Follow the steps below:

1. Navigate to the repository directory using the command `cd git-playground`.
2. Run the command `git log --oneline` to view the commit history.
3. Identifies a commit where a file was deleted with the message "Added file2.txt".
4. Run the command `git checkout <commit> -- <file>` to restore the specified `<file>` deleted in the specified `<commit>`. Replace `<commit>` with the commit hash and `<file>` with the name of the deleted file.

For example, if the file `file2.txt` was deleted in the commit `d22f46b`, you would run the following command:
```shell
git checkout d22f46b -- file2.txt
```
This will restore the `file2.txt` file to your local repository.

This is the result of running the `ll` command:
```shell
total 12K
-rw-r--r-- 1 labex labex 15 Jun 18 18:05 file1.txt
-rw-r--r-- 1 labex labex 15 Jun 18 18:13 file2.txt
-rw-r--r-- 1 labex labex 32 Jun 18 18:05 README.md
```
