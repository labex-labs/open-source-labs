# Pull Latest Changes from Remote

You are working on a project with a team of developers, and you need to ensure that your local copy of the codebase is up to date with the latest changes made by your team members. To do this, you need to pull the latest changes from the remote repository.

For this lab, we will be using the Git repository named `https://github.com/labex-labs/git-playground`. Follow the steps below to complete the challenge:

1. Clone the repository to your local machine using the following command:
```shell
git clone https://github.com/labex-labs/git-playground.git
```
2. Change into the directory of the cloned repository:
```shell
cd git-playground
```
3. Identify the commit hash with the commit message "Initial commit", and revert the repository to a version containing only that hash:
```shell
git log --oneline
git checkout b00b937
```
4. Pull the latest changes from the `master` branch of the remote repository:
```shell
git pull origin master
```

After running the `git pull` command, you should see a message indicating that your local copy of the repository is up to date with the remote repository.

This is the result after pulling:

![<result>](./assets/challenge-pull-changes-step1-1.png)
