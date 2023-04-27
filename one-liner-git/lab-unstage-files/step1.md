# Remove Files from the Staging Area

You are working on a project in the `git-playground` repository. You have made some changes to the files and added them to the staging area using the `git add` command. However, you realize that you accidentally added a file that you don't want to commit. You need to remove this file from the staging area.

1. Clone the `git-playground` repository using the following command:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Navigate to the repository directory:

```shell
cd git-playground
```

3. Create a new file and add it to the staging area:

```shell
touch newfile.txt
git add newfile.txt
```

4. Remove the file from the staging area using the `git restore --staged` command:

```shell
git restore --staged newfile.txt
```

5. Verify that the file has been removed from the staging area using the `git status` command:

```shell
git status
```

Output:

```
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
```
