# Git Challenge: Change the Last Commit's Message

Imagine you have just committed some changes to your Git repository, but you realize that you made a typo in the commit message. You want to correct the mistake without changing the actual changes you made. How can you do this?

To demonstrate how to change the last commit's message, we will use the Git repository named `https://github.com/labex-labs/git-playground`. Follow these steps:

1. Clone the repository to your local machine:
   ```
   git clone https://github.com/labex-labs/git-playground.git
   ```
2. Navigate to the repository directory:
   ```
   cd git-playground
   ```
3. Make some changes to the codebase:
   ```
   echo "print('Hello, World!')" >> hello.py
   ```
4. Stage the changes:
   ```
   git add .
   ```
5. Commit the changes with a typo in the message:
   ```
   git commit -m "Add a new line to the helo.py file"
   ```
6. Correct the typo in the commit message using `git commit --amend -m <message>`:
   ```
   git commit --amend -m "Add a new line to the hello.py file"
   ```
   This will open your default text editor where you can modify the commit message. Save and close the editor to complete the process.
7. Verify that the commit message has been changed:
   ```
   git log
   ```
   You should see the updated commit message in the log.
