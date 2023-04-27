# Change the Remote URL

You have cloned a repository from GitHub and made some changes to it. However, you now realize that you need to change the URL of the remote repository. This could be because the original repository has been moved to a different location, or because you want to push your changes to a different remote repository. Your task is to change the remote URL of the repository using Git commands.

Assume that you have cloned the repository `https://github.com/labex-labs/git-playground` to your local machine. To change the remote URL of the repository to `https://github.com/your-username/git-playground`, follow these steps:

1. Open the terminal or command prompt and navigate to the local repository.
2. Use the following command to view the current remote URL:
   ```
   git remote -v
   ```
3. Use the following command to change the remote URL to the new URL:
   ```
   git remote set-url origin https://github.com/your-username/git-playground
   ```
4. Use the following command to verify that the remote URL has been changed:
   ```
   git remote -v
   ```
   The output should show the new URL instead of the old one.
