# Create a New Branch

For this lab, fork the Git repository named `https://github.com/labex-labs/git-playground` into your GitHub account.You are working on a project in a Git repository named `https://github.com/your-username/git-playground`. You need to create a new branch named `feature-1` to work on a new feature.

1. Clone the repository:

```shell
git clone https://github.com/your-username/git-playground.git
```

2. Navigate to the repository directory:

```shell
cd git-playground
```

3. Check the current branch:

```shell
git branch
```

4. Create a new branch named `feature-1`:

```shell
git checkout -b feature-1
```

5. Verify that you are now on the `feature-1` branch:

```shell
git branch
```

6. Push the changes to the remote repository:

```shell
git push -u origin feature-1
```

This is what happens when you run the `git branch -r` command:

![<result>](assets/challenge-create-branch-step1-1.png)

