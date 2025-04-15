# Git Cherry-Pick

As a developer, you are working on a project with multiple branches. You have identified a specific change that was made in a previous commit that you would like to apply to your current branch. However, you do not want to merge the entire branch as it contains other changes that you do not need. In this scenario, you can use the `git cherry-pick` command to apply the specific change to your current branch.

For this lab, let's use the repository from `https://github.com/labex-labs/git-playground`. Follow the steps below to complete the challenge:

1. Clone the repository, navigate to the directory and configure the identity:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Create and switch to a branch called `one-branch`, create a file called `hello.txt`, write "hello,world" in it, add it to the staging area and commit it with the message "add hello.txt":

```shell
git checkout -b one-branch
echo "hello,world" > hello.txt
git add .
git commit -m "add hello.txt"
```

3. Identify the hash of the commit created in the previous step to apply to the `master` branch:

```shell
git log
```

4. Checkout the `master` branch and apply the change to the `master` branch:

```shell
git checkout master
git cherry-pick 1609c283ec86ee4
```

5. Verify that the change has been applied to the `master` branch:

```shell
git log
```

This is the result of running `git log` on the `master` branch:

```shell
ADD hello.txt
```
