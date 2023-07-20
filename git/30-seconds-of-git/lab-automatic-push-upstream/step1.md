# Automate Upstream Branch Creation

As a developer, you want to automate the process of creating upstream branches on push to avoid the hassle of manually creating the branch on the remote repository.

For this lab, you will fork the https://github.com/labex-labs/git-playground repository to your account, using the `git-playground` repository on your account to automatically create the upstream branch on push.

1. On the GitHub website, log in to your account and find https://github.com/labex-labs/git-playground to fork the repository to your account.

2. On the page for your own forked repository, click the `Code` button and copy the URL of the repository.

3. Clone the repository to your local machine using the following command:

```shell
git clone https://github.com/your-username/git-playground.git
```

4. Navigate to the repository directory:

```shell
cd git-playground
```

5. Use the following command to enable automatic upstream branch creation on push:

```shell
git config --add --bool remote.origin.pushdefault true
```

6. Push your changes to a new branch that does not exist on the remote repository:

```shell
git checkout -b new-feature
git push --set-upstream origin new-feature
```

7. Verify that the new branch has been created on the remote repository:

```shell
git ls-remote --heads origin
```

This is the result after completing the lab:

![<result>](./assets/challenge-automatic-push-upstream-step1-1.png)
