# Purge a file from history

Suppose you accidentally committed a file containing sensitive information, such as API keys or passwords, to your Git repository. You realize that this file should never have been committed and want to completely remove it from the repository's history. However, simply deleting the file and committing the change will not remove it from the repository's history. The file will still be accessible in previous commits, which could pose a security risk.

To complete this lab, you will use the Git repository `git-playground` from your GitHub account, which comes from a fork of `https://github.com/labex-labs/git-playground.git`. This repository contains a file named `file1.txt` that should never have been committed. Please purge `file1.txt` from the repository's history, follow these steps:

1. Clone the repository to your local machine:

```shell
git clone https://github.com/your-username/git-playground
```

2. Use the following commands to navigate to the directory and configure the identity:

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

3. Delete the file from the repository's index.

```shell
git rm --cached --ignore-unmatch file1.txt
```

4. Commit this change with the commit message "Remove sensitive file1.txt":

```shell
git commit -m "Remove sensitive file1.txt"
```

5. Rewrite the repository's history, removing all instances of `file1.txt`:

```shell
git filter-branch --force --index-filter "git rm --cached --ignore-unmatch file1.txt" --prune-empty --tag-name-filter cat -- --all
```

6. Force push the changes to the remote repository:

```shell
git push origin --force --all
```

After completing these steps, `file1.txt` will be completely removed from the repository's history and after running `git log --remotes`, you will not see the commit on `file1.txt`.
