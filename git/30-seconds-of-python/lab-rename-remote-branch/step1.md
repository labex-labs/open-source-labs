# Rename Remote Branch

You have a Git repository named `https://github.com/labex-labs/git-playground`. You have created a branch named `feature-1` and pushed it to the remote. Now you want to rename the branch to `new-feature-1` both locally and on the remote.

1. Open the terminal and clone the Git repository:
   ```
   git clone https://github.com/labex-labs/git-playground.git
   ```
2. Change to the repository directory:
   ```
   cd git-playground
   ```
3. Create a new branch named `feature-1` and switch to it:
   ```
   git checkout -b feature-1
   ```
4. Push the branch to the remote:
   ```
   git push -u origin feature-1
   ```
5. Rename the branch both locally and on the remote:
   ```
   git branch -m feature-1 new-feature-1
   git push origin --delete feature-1
   git push -u origin new-feature-1
   ```
6. Verify that the branch has been renamed:
   ```
   git branch -a
   ```
