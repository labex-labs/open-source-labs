# Rewind Commits

As a developer, you have been working on a project and have made several commits. However, you realize that the last few commits contain errors and you need to go back to a previous version of your code. You need to use Git to rewind your commits and get back to the previous version of your code.

To complete this lab, you will use the Git repository `git-playground` from your GitHub account, which comes from a fork of `https://github.com/labex-labs/git-playground.git`. Follow these steps:

1. Clone the repository to your local machine:
```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
```
2. Create a new branch called `rewind-commits`:
```shell
git checkout -b rewind-commits
```
3. View the commit history of the repository and realize that the last commit contain errors and you need to go back to the previous version of your code:
```shell
git log
```
4. Use Git to rewind your commits by 1:
```shell
git reset HEAD~1 --hard
```
5. Verify that you have successfully rewound your commits:
```shell
git log
```
6. Push your changes to the `rewind-commits` branch:
```shell
git push --force origin rewind-commits
```

This is the final result:
```shell
cf80005 (HEAD -> rewind-commits, origin/rewind-commits) Added file1.txt
b00b937 Initial commit
```
