# Return to Previous Branch

As a developer, you are working on a project and have switched to a different branch to work on a new feature. After making some changes, you realize that you need to switch back to the previous branch to fix a bug. You can commit your changes in a new branch and use a command to quickly switch to the previous branch.

To demonstrate how to switch back to the previous branch, we will use the Git repository named `https://github.com/labex-labs/git-playground`. Follow the steps below:

1. Clone the repository using the following command:
   ```
   git clone https://github.com/labex-labs/git-playground.git
   ```
2. Change to the repository directory:
   ```
   cd git-playground
   ```
3. Create a new branch named `feature-branch`:
   ```
   git checkout -b feature-branch
   ```
4. Check the current branch and switch to the previous branch quickly. The name of your new branch is `feature-branch` and the name of the previous branch you want to switch back to is `master`:
   ```
   git checkout -
   ```
   This will switch back to the `master` branch, and your changes will still be there.
