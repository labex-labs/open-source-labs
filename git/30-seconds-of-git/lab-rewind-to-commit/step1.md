# Rewind to a Specific Commit

As a developer, you may need to undo changes made to your codebase. For example, you may have made a mistake and need to go back to an earlier version of your code. In this challenge, you will use Git to rewind back to a specific commit in a repository.

To complete this lab, you will use the Git repository `git-playground` from `https://github.com/labex-labs/git-playground.git`. Follow these steps to complete the challenge:

1. Clone the repository to your local machine:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Navigate to the repository:

```shell
cd git-playground
```

3. View the commit history of the repository:

```shell
git log --oneline
```

4. Make sure that the commit message you want to rewind to is the "Initial commit" commit hash.
5. Use the command `git reset <commit>` to rewind back to the specified commit. For example, you want to rewind back to the commit with hash `3050fc0d3`:

```shell
git reset 3050fc0d3
```

6. View the commit history of the repository again:

```shell
git log --oneline
```

7. If you want to delete the changes and revert to the earlier version of your code, use the command `git reset --hard <commit>`. For example, you want to delete the changes and revert to the commit with hash `c0d30f305`:

```shell
git reset --hard c0d30f305
```

This is the result of running `git log --oneline`:

```shell
c0d30f305 (HEAD -> master) Initial commit
```
