# Automate Upstream Branch Creation

As a developer, you want to automate the process of creating upstream branches on push to avoid the hassle of manually creating the branch on the remote repository.

For this lab, you will fork the `https://github.com/labex-labs/git-playground` repository to your account, using the `git-playground` repository on your account to automatically create the upstream branch on push.

1. On the GitHub website, log in to your account and find `https://github.com/labex-labs/git-playground` to fork the repository to your account.
2. On the page for your own forked repository, click the `Code` button and copy the URL of the repository.
3. Clone the repository, navigate to the directory and configure the identity:
```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```
4. Use the following command to enable automatic upstream branch creation on push:
```shell
git config --global push.default current
```
5. Push a new branch called `new-feature`, which does not exist in the remote repository:
```shell
git checkout -b new-feature
git push --set-upstream origin new-feature
```
6. Verify that the new branch has been created on the remote repository:
```shell
git ls-remote --heads origin
```

This is the result after completing the lab:

![<result>](./assets/challenge-automatic-push-upstream-step1-1.png)
