# Fetch Latest Changes from Remote

Suppose you are working on a project with a team of developers, and the project is stored in a remote repository. You want to get the latest changes from the remote repository without applying them to your local repository.

## Example

To demonstrate how to fetch the latest changes from a remote repository, we will use the Git repository `git-playground` from your GitHub account, which comes from a fork of `https://github.com/labex-labs/git-playground.git`.

1. Clone the repository, navigate to the directory.
2. Find the `git-playground` repository in your account on the Github website, create and switch to a branch called `fetch-branch`, create a file called `hello.txt`, add "hello, world" and commit with the message "Create hello.txt".
3. View branches in remote repositories.
4. Fetch the latest changes from the remote repository.
5. View branches in remote repositories again and verify that the latest changes have been fetched.

This is the result of running `git log origin/fetch-branch`:

```shell
commit f3125b4c99e0ef2ce58bc0b1287c966c9e68c577 (origin/fetch-branch)
Author: xiaoshengyunan <131872312+xiaoshengyunan@users.noreply.github.com>
Date:   Thu Jul 20 20:17:23 2023 +0800

    Create hello.txt
```
