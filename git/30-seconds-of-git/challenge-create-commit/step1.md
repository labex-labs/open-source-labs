# Create a Git Commit

## Problem

You have made some changes to your code and want to save them as a snapshot in your Git repository. However, you don't want to save all the changes you made, only the ones that are relevant to the current feature or bug fix. How can you create a commit containing only the relevant changes?

## Example

To create a commit, you first need to stage the changes you want to include in the commit. Let's assume you have cloned the `https://github.com/labex-labs/git-playground` repository and made some changes to the `README.md` file. To create a commit with the message "Update README.md", follow these steps:

1. Add "hello" to the `README`.md file and stage the changes using the `git add` command:

   ```
   git add README.md
   ```

2. Create the commit using the `git commit` command:
   ```
   git commit -m "Update README.md"
   ```

The `-m` option allows you to specify a commit message. Make sure the message is descriptive and explains what changes the commit contains.
