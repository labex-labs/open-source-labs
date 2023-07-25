# Change the Last Commit's Message

Imagine you have just committed some changes to your Git repository, but you realize that you made a typo in the commit message. You want to correct the mistake without changing the actual changes you made. How can you do this?

To demonstrate how to change the last commit's message, let's use the repository from `https://github.com/labex-labs/git-playground`. Follow these steps:

1. Clone the repository, navigate to the directory and configure the identity:
   ```
   git clone https://github.com/labex-labs/git-playground
   cd git-playground
   git config --global user.name "your-username"
   git config --global user.email "your-email"
   ```
2. Correct the commit message of the last commit to read "Fix the network bug":
   ```
   git commit --amend -m "Fix the network bug"
   ```
   This will open your default text editor where you can modify the commit message. Save and       close the editor to complete the process.
3. Verify that the commit message has been changed:
   ```
   git log --oneline
   ```

You should see the updated commit message in the log:
```
54b830b (HEAD -> master) Fix the network bug
cf80005 Added file1.txt
b00b937 Initial commit
```
