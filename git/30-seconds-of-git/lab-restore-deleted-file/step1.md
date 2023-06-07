# Restore a Deleted File

You are working on a project using Git and accidentally deleted a file that you need. Fortunately, you know the commit where the file was deleted. Your task is to restore the deleted file using Git.

To complete this lab, you will use the Git repository `git-playground` from your GitHub account, which comes from a fork of `https://github.com/labex-labs/git-playground.git`. Follow the steps below:

1. Clone the repository to your local machine using the command `git clone https://github.com/your-username/git-playground`.
2. Navigate to the repository directory using the command `cd git-playground`.
3. Create a new file called `example.txt` using the command `echo "This is an example file" > example.txt`.
4. Add and commit the file to the repository using the commands `git add example.txt` and `git commit -m "Add example.txt file"`.
5. Delete the example.txt file using the command `rm example.txt`.
6. Run the command `git log --oneline` to view the commit history.
7. Identify the commit where the file was deleted.
8. Run the command `git checkout <commit>^ -- <file>` to restore the specified `<file>` deleted in the specified `<commit>`. Replace `<commit>` with the commit hash and `<file>` with the name of the deleted file.

For example, if the file `example.txt` was deleted in the commit `3050fc0de`, you would run the following command:

```shell
git checkout 3050fc0de^ -- example.txt
```

This will restore the `example.txt` file to your local repository.

This is the result of running `git status`:

![<result>](./assets/challenge-restore-deleted-file-step1-1.png)
