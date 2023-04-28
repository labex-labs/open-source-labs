# Automate Upstream Branch Creation

As a developer, you want to automate the process of creating upstream branches on push to avoid the hassle of manually creating the branch on the remote repository.

In this challenge, you will use the git repository named `https://github.com/labex-labs/git-playground` directory to enable automatic upstream branch creation on push.

1. Clone the repository to your local machine using the following command:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Navigate to the repository directory:

```shell
cd git-playground
```

3. Use the following command to enable automatic upstream branch creation on push:

```shell
git config --add --bool remote.origin.pushdefault true
```

4. Push your changes to a new branch that does not exist on the remote repository:

```shell
git checkout -b new-feature
git push
```

5. Verify that the new branch has been created on the remote repository:

```shell
git ls-remote --heads origin
```
