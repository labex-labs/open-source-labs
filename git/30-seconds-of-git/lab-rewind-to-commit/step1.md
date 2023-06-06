# Git Challenge: Rewind to a Specific Commit

As a developer, you may need to undo changes made to your codebase. For example, you may have made a mistake and need to go back to an earlier version of your code. In this challenge, you will use Git to rewind back to a specific commit in a repository.

To complete this experiment, you will use the Git repository `git-playground` from your GitHub account, which comes from a fork of `https://github.com/labex-labs/git-playground.git`.Follow these steps to complete the challenge:

1. Clone the repository to your local machine:
```shell
git clone https://github.com/your-username/git-playground
```
2. Navigate to the repository:
```shell
cd git-playground
```
3. Create a new file called `hello.txt` with the text "Hello, World" and add it to the Git staging area. Then commit the changes with the message "Add hello.txt file":
```shell
echo "Hello, World" > hello.txt
git add hello.txt
git commit -m "Add hello.txt file"
```
4. Update the contents of the file `hello.txt` to "Hello, Git" and add the changes to the Git staging area. Then use the "Update hello.txt file" message to commit the changes:
```shell
echo "Hello, Git" > hello.txt
git add hello.txt
git commit -m "Update hello.txt file"
```
5. Update the contents of the file `hello.txt` to "Hello, Labex" and add the changes to the Git staging area. Then use the "Update hello.txt file again" message to commit the changes again:
```shell
echo "Hello, Labex" > hello.txt
git add hello.txt
git commit -m "Update hello.txt file again"
```
6. View the commit history of the repository:
```shell
git log --oneline
```
7. Make sure that the commit message you want to rewind to is the "Add hello.txt file" commit hash.
8. Use the command `git reset <commit>` to rewind back to the specified commit. For example, if you want to rewind back to the commit with hash `3050fc0d3`:
```shell
git reset 3050fc0d3
```
9. View the changes made to your codebase:
```shell
git status 
```
10. If you want to delete the changes and revert to the earlier version of your code, use the command `git reset --hard <commit>`. For example, if you want to delete the changes and revert to the commit with hash `c0d30f305`,
```shell
git reset --hard c0d30f305
```

This is the result of running `cat hello.txt`:
```shell
Hello, World
```
