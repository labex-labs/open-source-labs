# Return to Previous Branch

As a developer, you are working on a project and have switched to a different branch to work on a new feature. After making some changes, you realize that you need to switch back to the previous branch to fix a bug. How do you switch back to the previous branch without losing your changes?

To demonstrate how to switch back to the previous branch, we will use the Git repository named `https://github.com/labex-labs/git-playground`. Follow the steps below:

1. Clone the repository using the following command:
   ```
   git clone https://github.com/labex-labs/git-playground.git
   ```
2. Change to the repository directory:
   ```
   cd git-playground
   ```
3. Create a new branch named `new-feature`:
   ```
   git checkout -b new-feature
   ```
4. Make some changes to the codebase:
   ```
   echo "New feature added" >> README.md
   ```
5. Commit the changes:
   ```
   git add README.md
   git commit -m "Added new feature"
   ```
6. Switch to the master branch:
   ```
   git checkout master
   ```
7. Make some changes to the codebase:
   ```
   echo "Bug fixed" >> README.md
   ```
8. Commit the changes:
   ```
   git add README.md
   git commit -m "Fixed bug"
   ```
9. Switch back to the previous branch:
   ```
   git checkout -
   ```
   This will switch back to the `new-feature` branch, and your changes will still be there.
