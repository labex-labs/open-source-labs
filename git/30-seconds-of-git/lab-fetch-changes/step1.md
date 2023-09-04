# Fetch Latest Changes from Remote

Suppose you are working on a project with a team of developers, and the project is stored in a remote repository. You want to get the latest changes from the remote repository without applying them to your local repository. This is where the `git fetch` command comes in handy.

The `git fetch` command downloads the latest changes from the remote repository to your local repository, but it does not apply them to your working directory. This means that you can review the changes before merging them into your local repository.

To demonstrate how to fetch the latest changes from a remote repository, we will use the Git repository `git-playground` from your GitHub account, which comes from a fork of `https://github.com/labex-labs/git-playground.git`. Follow the steps below:

1. Clone the repository, navigate to the directory:

```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
```

2. Find the `git-playground` repository in your account on the Github website, create and switch to a branch called `fetch-branch`, create a file called `hello.txt`, add "hello, world" and commit with the message "Create hello.txt".
3. View branches in remote repositories:

```shell
git branch -r
```

4. Fetch the latest changes from the remote repository:

```shell
git fetch
```

5. View branches in remote repositories again and verify that the latest changes have been fetched:

```shell
git branch -r
git log origin/fetch-branch
```

This will show you the latest commits on the `origin/fetch-branch` branch.This is the result of running `git log origin/fetch-branch`:

```shell
commit f3125b4c99e0ef2ce58bc0b1287c966c9e68c577 (origin/fetch-branch)
Author: xiaoshengyunan <131872312+xiaoshengyunan@users.noreply.github.com>
Date:   Thu Jul 20 20:17:23 2023 +0800

    Create hello.txt
```
