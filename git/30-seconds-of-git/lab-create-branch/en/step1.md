# Create a New Branch

For this lab, fork the Git repository named `https://github.com/labex-labs/git-playground` into your GitHub account.You are working on a project in a Git repository named `https://github.com/your-username/git-playground`. You need to create a new branch named `feature-1` to work on a new feature.

1. Clone the repository, navigate to the directory and configure the identity:

```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Check the current branch:

```shell
git branch
```

3. Create a new branch named `feature-1`:

```shell
git checkout -b feature-1
```

4. Verify that you are now on the `feature-1` branch:

```shell
git branch
```

5. Push the changes to the remote repository:

```shell
git push -u origin feature-1
```

This is what happens when you run the `git branch -r` command:

![git branch remote output](../assets/challenge-create-branch-step1-1.png)
