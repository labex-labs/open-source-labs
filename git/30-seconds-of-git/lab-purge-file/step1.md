# Purge a file from history

Suppose you accidentally committed a file containing sensitive information, such as API keys or passwords, to your Git repository. You realize that this file should never have been committed and want to completely remove it from the repository's history. However, simply deleting the file and committing the change will not remove it from the repository's history. The file will still be accessible in previous commits, which could pose a security risk.

To complete this lab, you will use the Git repository `git-playground` from your GitHub account, which comes from a fork of `https://github.com/labex-labs/git-playground.git`. This repository contains a file named `file1.txt` that should never have been committed. Please purge `file1.txt` from the repository's history,follow these steps:

1. Clone the repository to your local machine using the command `git clone https://github.com/your-username/git-playground`.
2. Navigate to the repository's directory using the command `cd git-playground`.
3. Use the command `git rm --cached --ignore-unmatch file1.txt` to delete the file from the repository's index.
4. Use the command `git filter-branch --force --index-filter "git rm --cached --ignore-unmatch file1.txt" --prune-empty --tag-name-filter cat -- --all` to rewrite the repository's history, removing all instances of `file1.txt`.
5. Use the command `git push origin --force --all` to force push the changes to the remote repository.

After completing these steps, `file1.txt` will be completely removed from the repository's history and after running `git log -r`, you will not see the commit on `file1.txt`.
