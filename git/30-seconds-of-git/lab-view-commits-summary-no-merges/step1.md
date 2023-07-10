# View a Short Summary of Commits without Merge Commits

You have been working on a project with several other developers, and you want to see a summary of all the commits made to the repository. However, you don't want to see the merge commits, as they don't contain any actual changes to the code. How can you view a summary of all the commits excluding merge commits?

To complete this challenge, you will need to use the Git repository named `https://github.com/labex-labs/git-playground`.

1. Clone the repository to your local machine using the following command:
```shell
git clone https://github.com/labex-labs/git-playground.git
```
2. Once you have cloned the repository, navigate to the directory using the following command:
```shell
cd git-playground
```
3. Now, to view a short summary of all commits excluding merge commits, use the following command:
```shell
git log --oneline --no-merges
```

This will output a list of all the commits made to the repository, excluding any merge commits. The output will look something like this:

```shell
d22f46b (HEAD -> master, origin/master, origin/feature-branch, origin/HEAD) Added file2.txt
cf80005 Added file1.txt
b00b937 Initial commit
```
