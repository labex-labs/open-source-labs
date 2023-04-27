# Delete All Stashes

You have been working on a project in a Git repository and have created multiple stashes to save your changes. Now, you want to delete all stashes to start fresh. However, you are not sure how to do it.

To complete this challenge, you will use the Git repository named `https://github.com/labex-labs/git-playground`. Follow the steps below:

1. Clone the repository to your local machine using the command `git clone https://github.com/labex-labs/git-playground`.
2. Navigate to the repository directory using the command `cd git-playground`.
3. Create a new file in the repository directory using the command `touch newfile.txt`.
4. Add the new file to the staging area using the command `git add newfile.txt`.
5. Create a stash using the command `git stash save "new file added"`.
6. Repeat steps 3-5 to create multiple stashes.
7. Delete all stashes using the command `git stash clear`.
8. Verify that all stashes have been deleted using the command `git stash list`.
