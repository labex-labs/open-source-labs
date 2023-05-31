# Move Commits to a New Branch

To complete this experiment, you will use the Git repository `git-playground` from your GitHub account, which comes from a fork of `https://github.com/labex-labs/git-playground.git`.You have been working on a project in the `master` branch of the `https://github.com/your-username/git-playground` repository. You realize that some of the changes you made should have been made on a separate branch. You want to move these changes to a new branch called `feature-branch`.

1. Clone the `https://github.com/your-username/git-playground` repository to your local machine.
2. Checkout the `master` branch using `git checkout master`.
3. Make some changes to the codebase, add and commit them using `git add .` and `git commit -m "Add new feature to master branch"`.
4. Create a new branch called `feature-branch` using `git branch feature-branch`.
5. Move the last commit from `master` to `feature-branch` using `git checkout feature-branch` and `git cherry-pick master`.
6. Verify that the changes are now in the `feature-branch` using `git log`.

```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
git checkout master
# Make some changes to the codebase
git add .
git commit -m "Add new feature to master branch"
git branch feature-branch
git checkout feature-branch
git cherry-pick master
git log # Verify that the changes are now in `feature-branch`
```
