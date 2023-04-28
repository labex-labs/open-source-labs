# Restore a Deleted File

## Problem

You are working on a project using Git and accidentally deleted a file that you need. Fortunately, you know the commit where the file was deleted. Your task is to restore the deleted file using Git.

## Example

To complete this challenge, you will use the `git-playground` repository located at `https://github.com/labex-labs/git-playground`. Follow the steps below:

1. Clone the repository to your local machine using the command `git clone https://github.com/labex-labs/git-playground`.
2. Navigate to the repository directory using the command `cd git-playground`.
3. Run the command `git log --oneline` to view the commit history.
4. Identify the commit where the file was deleted.
5. Run the command `git checkout <commit>^ -- <file>` to restore the specified `<file>` deleted in the specified `<commit>`. Replace `<commit>` with the commit hash and `<file>` with the name of the deleted file.

For example, if the file `example.txt` was deleted in the commit `3050fc0de`, you would run the following command:

```shell
git checkout 3050fc0de^ -- example.txt
```

This will restore the `example.txt` file to your local repository.
