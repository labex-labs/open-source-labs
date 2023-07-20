# View the Remote URL

As a developer, you may need to view the URL of a remote repository for various reasons, such as troubleshooting issues with your Git configuration or verifying that you are working with the correct repository. However, if you are not familiar with Git commands, it can be challenging to know how to view the remote URL.

For this lab, we will be using the Git repository named `https://github.com/labex-labs/git-playground`. To view the remote URL of this repository, follow these steps:

1. Open your terminal or command prompt.
2. Navigate to the directory where you have cloned the `git-playground` repository:
```shell
cd git-playground
```
3. Run the following command to view the remote URL:
```shell
git config --get remote.origin.url
```

The output should display the URL of the remote repository, which in this case is `https://github.com/labex-labs/git-playground.git`.
