# Create a Git Commit

You have made some changes to your code and want to save them as a snapshot in your Git repository. However, you don't want to save all the changes you made, only the ones that are relevant to the current feature or bug fix. How can you create a commit containing only the relevant changes?

For this lab, let's use the repository from `https://github.com/labex-labs/git-playground`, follow these steps:

1. Clone the repository and navigate it:
   ```
   git clone https://github.com/labex-labs/git-playground
   cd git-playground
   ```
2. Configure your github account in the environment:
   ```
   git config --global user.name "your-name"
   git config --global user.email "your-email"
   ```
3. Add "hello,labex" to the `README.md` file, add it to the staging area and commit it with the message "Updating README.md":
   ```
   echo "hello,labex" >> README.md
   git add .
   git commit -m "Update README.md"
   ```
   The `-m` option allows you to specify a commit message. Make sure the message is descriptive and explains what changes the commit contains.

This is the result of running the `git log` command:

![<result>](./assets/challenge-create-commit-step1-1.png)
