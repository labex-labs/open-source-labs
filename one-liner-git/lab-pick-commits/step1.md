# Git Cherry-Pick

As a developer, you are working on a project with multiple branches. You have identified a specific change that was made in a previous commit that you would like to apply to your current branch. However, you do not want to merge the entire branch as it contains other changes that you do not need. In this scenario, you can use the `git cherry-pick` command to apply the specific change to your current branch.

For this challenge, we will be using the `https://github.com/labex-labs/git-playground` repository. Follow the steps below to complete the challenge:

1. Clone the repository to your local machine using the command `git clone https://github.com/labex-labs/git-playground`.
2. Checkout the `master` branch using the command `git checkout master`.
3. Use the `git log` command to view the commit history.
4. Identify the commit that contains the change you want to apply to the `master` branch.
5. Use the `git cherry-pick` command to apply the change to the `master` branch. For example, if the commit hash is `3050fc0de`, use the command `git cherry-pick 3050fc0de`.
6. Use the `git log` command again to verify that the change has been applied to the `master` branch.
7. Commit the changes using the command `git commit -m "Applied cherry-pick from <commit-hash>"`.
8. Push the changes to the remote repository using the command `git push origin master`.
