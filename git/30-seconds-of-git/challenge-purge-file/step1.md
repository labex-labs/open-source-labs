# Purge a file from history

## Problem

Suppose you accidentally committed a file containing sensitive information, such as API keys or passwords, to your Git repository. You realize that this file should never have been committed and want to completely remove it from the repository's history. However, simply deleting the file and committing the change will not remove it from the repository's history. The file will still be accessible in previous commits, which could pose a security risk.

## Example

To complete this experiment, you will use the Git repository `git-playground` from your GitHub account, which comes from a fork of `https://github.com/labex-labs/git-playground.git`.This repository contains a file named `file1.txt` that should never have been committed.Please purge `file1.txt` from the repository's history.

1. Clone the repository to your local machine from `https://github.com/your-username/git-playground`.
2. Navigate to the repository's directory.
3. Delete the file from the repository's index.
4. Rewrite the repository's history, removing all instances of `file1.txt`.
5. Force push the changes to the remote repository.

After completing these steps, `file1.txt` will be completely removed from the repository's history and after running `git log -r`, you will not see the commit on `file1.txt`.
