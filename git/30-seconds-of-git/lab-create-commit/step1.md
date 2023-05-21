# Create a Git Commit

You have made some changes to your code and want to save them as a snapshot in your Git repository. However, you don't want to save all the changes you made, only the ones that are relevant to the current feature or bug fix. How can you create a commit containing only the relevant changes?

For this lab, fork the Git repository named `https://github.com/labex-labs/git-playground` into your GitHub account.To create a commit, you first need to stage the changes you want to include in the commit.Configure your github account in the environment. Let's assume you have cloned the `https://github.com/your-username/git-playground` repository and made some changes to the `README.md` file. Create a commit with the message "Update README.md", follow these steps:

1. Clone the repository and navigate it:
   ```
   git clone https://github.com/your-username/git-playground
   cd git-playground
   ```
2. Configure your github account in the environment:
   ```
   git config --global user.name "your-name"
   git config --global user.email "your-email"
   ```
3. Stage the changes using the `git add` command:
   ```
   echo "hello" > README.md
   git add README.md
   ```
4. Create the commit using the `git commit` command:
   ```
   git commit -m "Update README.md"
   ```

The `-m` option allows you to specify a commit message. Make sure the message is descriptive and explains what changes the commit contains.

This is the result of running the `git log` command:

![<result>](assets/challenge-create-commit-step1-1.png)
