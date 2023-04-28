# Git Challenge: Rewind to a Specific Commit

As a developer, you may need to undo changes made to your codebase. For example, you may have made a mistake and need to go back to an earlier version of your code. In this challenge, you will use Git to rewind back to a specific commit in a repository.

For this challenge, you will use the Git repository named `https://github.com/labex-labs/git-playground`. Follow these steps to complete the challenge:

1. Clone the repository to your local machine using the command `git clone https://github.com/labex-labs/git-playground`.
2. Navigate to the repository using the command `cd git-playground`.
3. Use the command `git log` to view the commit history of the repository.
4. Identify the commit hash that you want to rewind back to.
5. Use the command `git reset <commit>` to rewind back to the specified commit. For example, if you want to rewind back to the commit with hash `3050fc0d3`, use the command `git reset 3050fc0d3`.
6. Use the command `git status` to view the changes made to your codebase.
7. If you want to delete the changes and revert to the earlier version of your code, use the command `git reset --hard <commit>`. For example, if you want to delete the changes and revert to the commit with hash `c0d30f305`, use the command `git reset --hard c0d30f305`.
