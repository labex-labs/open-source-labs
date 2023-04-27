# Rebase onto Another Branch

As a developer, you are working on a project with multiple branches. You have made changes to your branch and want to incorporate those changes into another branch. However, you don't want to merge the branches because you want to maintain a clean and linear history. In this case, you can use the `git rebase` command to rebase your branch onto another branch.

For this challenge, we will be using the `https://github.com/labex-labs/git-playground` repository. Follow the steps below to complete the challenge:

1. Clone the repository to your local machine using the command `git clone https://github.com/labex-labs/git-playground`.
2. Switch to the `feature-branch` branch using the command `git checkout feature-branch`.
3. Make some changes to the `README.md` file and commit your changes using the command `git commit -am "Added some changes to README.md"`.
4. Switch to the `master` branch using the command `git checkout master`.
5. Use the command `git pull` to ensure that your local `master` branch is up to date with the remote repository.
6. Use the command `git rebase feature-branch` to rebase the `feature-branch` onto the `master` branch.
7. Resolve any conflicts that arise during the rebase process.
8. Push your changes to the remote repository using the command `git push origin master`.
