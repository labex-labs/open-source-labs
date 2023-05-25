# Fetch Latest Changes from Remote

Suppose you are working on a project with a team of developers, and the project is stored in a remote repository. You want to get the latest changes from the remote repository without applying them to your local repository. This is where the `git fetch` command comes in handy.

The `git fetch` command downloads the latest changes from the remote repository to your local repository, but it does not apply them to your working directory. This means that you can review the changes before merging them into your local repository.

To demonstrate how to fetch the latest changes from a remote repository, we will use the `git-playground` repository hosted on GitHub. Follow the steps below:

1. Clone the `git-playground` repository to your local machine using the following command:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Change your working directory to the `git-playground` directory:

```shell
cd git-playground
```

3. Fetch the latest changes from the remote repository:

```shell
git fetch
```

4. Verify that the latest changes have been fetched by running the following command:

```shell
git log origin/master
```

This will show you the latest commits on the `origin/master` branch.This is the result of running `git log origin/master`:

![<result>](assets/challenge-fetch-changes-step1-1.png)
