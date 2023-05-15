# Automate Upstream Branch Creation

## Problem

As a developer, you want to automate the process of creating upstream branches on push to avoid the hassle of manually creating the branch on the remote repository.

## Example

In this challenge, you will use the git repository named `https://github.com/labex-labs/git-playground` directory to enable automatic upstream branch creation on push.


1. On the GitHub website, log in to your account and find the page for the repository you want to fork.

2. Click the "Fork" button in the top right corner of the repository page to fork the repository into your own account.

3. On the page for your own forked repository, click the "Code" button and copy the URL of the repository.

4. Clone the repository to your local machine using the following command:

```shell
git clone https://github.com/your-username/git-playground.git
```

5. Navigate to the repository directory:

```shell
cd git-playground
```

6. Use a command to enable automatic upstream branch creation on push.

7. Push your changes to a new branch that does not exist on the remote repository.

8. Verify that the new branch has been created on the remote repository:

```shell
git ls-remote --heads origin
```
