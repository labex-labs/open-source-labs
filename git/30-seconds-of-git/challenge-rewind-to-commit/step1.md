# Git Challenge: Rewind to a Specific Commit

## Problem

As a developer, you may need to undo changes made to your codebase. For example, you may have made a mistake and need to go back to an earlier version of your code. In this challenge, you will use Git to rewind back to a specific commit in a repository.

## Example

To complete this experiment, you will use the Git repository `git-playground` from your GitHub account, which comes from a fork of `https://github.com/labex-labs/git-playground.git`.

1. Clone the repository to your local machine from `https://github.com/your-username/git-playground`.
2. Navigate to the repository using the command `cd git-playground`.
3. Create a new file called `hello.txt` with the text "Hello, World" and add it to the Git staging area. Then commit the changes with the message "Add hello.txt file".
4. Update the contents of the file `hello.txt` to "Hello, Git" and add the changes to the Git staging area. Then use the "Update hello.txt file" message to commit the changes.
5. Update the contents of the file `hello.txt` to "Hello, Labex" and add the changes to the Git staging area. Then use the "Update hello.txt file again" message to commit the changes again.
6. View the commit history of the repository.
7. Make sure that the commit message you want to rewind to is the "Add hello.txt file" commit hash.
8. Rewind back to the commit hash.
9. View the changes made to your codebase.

This is the result of running `cat hello.txt`:
```shell
Hello, World
```

To complete this experiment, you will use the Git repository `git-playground` from your GitHub account, which comes from a fork of `https://github.com/labex-labs/git-playground.git`.Follow these steps:

1. Clone the repository to your local machine:
```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
```
2. Create a new branch called `rewind-commits-hash`:
```shell
git checkout -b rewind-commits-hash
```
3. Create a new file called hello.py with the text "Hello, World" and add it to the Git staging area. Then commit the changes with the message "Add hello.py file":
```shell
echo "Hello, World" > hello.py
git add hello.py
git commit -m "Add hello.py file"
```
4. Update the contents of the file hello.py to "Hello, Git" and add the changes to the Git staging area. Then use the "Update hello.py file" message to commit the changes:
```shell
echo "Hello, Git" > hello.py
git add hello.py
git commit -m "Update hello.py file"
```