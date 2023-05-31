# Merge a Branch and Create a Merge Commit

As a developer, you may need to merge a branch into the current branch, creating a merge commit. This can be a bit tricky if you're not familiar with Git. The problem is to merge a branch into the current branch, creating a merge commit, using the Git repository named `https://github.com/labex-labs/git-playground` directory.

To complete this experiment, you will use the Git repository `git-playground` from your GitHub account, which comes from a fork of `https://github.com/labex-labs/git-playground.git`.
Suppose you are working on a project with a team of developers, and you need to merge a branch named `feature-branch` into the `master` branch. Here are the steps you would take:
1. Clone a repository from `https://github.com/your-username/git-playground.git`.
```
git clone https://github.com/your-username/git-playground.git
```
2. Navigate into the repository and create an empty branch `feature-branch` and modify the `README.md` file.
```
cd git-playground
echo "This is a new line." >> README.md
git add .
```
3. Commit all modified files to the local repository.
```
git commit -am "Add new line to README.md"
```
4. Switch to the `master` branch.
```
git checkout master
```
5. Merge the `feature-branch` into the `master` branch,which will create a merge commit with the message "Merge feature-branch".
```
git merge --no-ff -m "Merge feature-branch" feature-branch
```

This is the result of running `git log`.

![<result>](assets/challenge-merge-branch-merge-commit-step1-1.png)
