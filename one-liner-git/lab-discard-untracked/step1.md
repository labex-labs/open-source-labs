# Discard Untracked Changes

You are working on a project using Git and have made some changes to your working directory. However, you realize that you don't need these changes and want to discard them. You want to discard all untracked changes to the current branch.

To complete this challenge, you will use the Git repository named `https://github.com/labex-labs/git-playground`. Follow these steps:

1. Clone the repository to your local machine:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Navigate to the repository directory:

```shell
cd git-playground
```

3. Create a new file in the repository directory:

```shell
touch new-file.txt
```

4. Check the status of your working directory:

```shell
git status
```

You should see the following output:

```shell
On branch main
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        new-file.txt

nothing added to commit but untracked files present (use "git add" to track)
```

5. Discard all untracked changes to the current branch:

```shell
git clean -f -d
```

6. Check the status of your working directory again:

```shell
git status
```

You should see the following output:

```shell
On branch main
nothing to commit, working tree clean
```

The `git clean -f -d` command has discarded all untracked changes to the current branch.
