# Set Default Push Branch Name

## Problem

When pushing changes to a remote repository, Git will use the name of the current local branch as the default name for the remote branch. However, sometimes you may want to push your changes to a different branch. In this case, you would need to specify the name of the remote branch explicitly every time you push your changes. This can be tedious and error-prone, especially if you are working with multiple branches.

## Example

To complete this challenge, you will use the Git repository `git-playground` from your GitHub account, which comes from a fork of `https://github.com/labex-labs/git-playground.git`. Follow the steps below to set the default push branch name:

1. Clone the repository from `https://github.com/your-username/git-playground.git.
2. Change to the repository directory.
3. Set the default push branch name to the name of the current local branch.
4. Create a new branch named `my-branch` and switch to it.
5. Create a new file called `hello.txt` and write the string "Hello, World" into it. Add the newly created file `hello.txt` to the Git staging area and commit it, using the commit message "Add hello.txt" to describe the changes made in this commit.
6. Push your changes to the remote repository. Git will push your changes to a branch named `my-branch` on the remote repository.

This is the result of running `git log -r`:

![<result>](./assets/challenge-set-default-push-branch-step1-1.png)

1. Clone the repository using the following command:
   ```
   git clone https://github.com/labex-labs/git-playground.git
   ```
2. Change to the repository directory:
   ```
   cd git-playground
   ```
3. Set the default push branch name to the name of the current local branch:
   ```
   git config push.default current
   ```
4. Create a new branch and switch to it:
   ```
   git checkout -b my-branch
   ```
5. Make some changes to the repository and commit them:
   ```
   echo "Hello, World" > hello.txt
   git add hello.txt
   git commit -m "Add hello.txt"
   ```
6. Push your changes to the remote repository:
   ```
   git push -u
   ```
   Git will push your changes to a branch named `my-branch` on the remote repository.