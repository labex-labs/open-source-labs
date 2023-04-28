# Git Challenge: View Difference Between Two Branches

You have been working on a project with your team, and you have created a branch named `feature-1` to work on a new feature. Your colleague has also created a branch named `feature-2` to work on a different feature. You want to compare the changes between the two branches to see what has been added, modified, or deleted. How can you view the difference between the two branches?

To complete this challenge, you will use the Git repository named `https://github.com/labex-labs/git-playground`. Follow the steps below:

1. Clone the repository to your local machine using the command `git clone https://github.com/labex-labs/git-playground`.
2. Change to the repository's directory using the command `cd git-playground`.
3. Create a new branch named `feature-1` using the command `git checkout -b feature-1`.
4. Make some changes to the `README.md` file using your favorite text editor.
5. Commit the changes using the command `git commit -am "Add new content to README.md"`.
6. Create a new branch named `feature-2` using the command `git checkout -b feature-2`.
7. Make some changes to the `index.html` file using your favorite text editor.
8. Commit the changes using the command `git commit -am "Update index.html file"`.
9. View the difference between the two branches using the command `git diff feature-1..feature-2`.

The output should display the difference between the `feature-1` and `feature-2` branches.
