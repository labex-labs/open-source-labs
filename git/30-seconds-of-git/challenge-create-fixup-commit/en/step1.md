# Create a Fixup Commit

Suppose you are working on a project with several other developers, and you notice a small error in a commit that was made a few days ago. You want to fix the error, but you don't want to create a new commit and disrupt the work of the other developers. This is where fixup commits come in handy. By creating a fixup commit, you can make the necessary changes without creating a new commit, and the fixup commit will be automatically merged with the original commit during the next rebase.

## Tasks

Your task is to write the string "hello,world" to the `hello.txt` file and add it as a "fixup" commit to the commit with the message "Added file1.txt", so that it can be automatically merged in a subsequent rebase operation.

For this challenge, let's use the repository from `https://github.com/labex-labs/git-playground`.

1. Navigate to the directory and configure the identity.
2. Create a `hello.txt` file, write "hello,world" in it and add it to the staging area.
3. Create a fixup commit for the hash of the "Added file1.txt" commit message.
4. Once you have created the fixup commit, you can automatically merge the fixup commit with the original commit during the next rebase. When opening the interactive editor, you don't need to change the text and save to exit.

This is the result of running the `git show HEAD~1` command:

```shell
[object Object]
```
