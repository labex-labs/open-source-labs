# Move Commits to a New Branch

For this lab, let's use the repository from `https://github.com/labex-labs/git-playground`. You have been working on a project in the `master` branch. You realize that some of the changes you made should have been made on a separate branch. You want to move these changes to a new branch called `feature`.

1. Clone the repository, navigate to the directory and configure the identity:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Checkout the `master` branch:

```shell
git checkout master
```

3. Create a file called `hello.txt`, add "hello, world" to it, add it to the staging area and submit it with the message "Added hello.txt":

```shell
echo "hello,world" >> hello.txt
git add .
git commit -m "Added hello.txt"
```

4. Create a new branch called `feature` without switching to it. When you create a new branch on the `master` branch, the state of the new branch is the same as the `master` branch, i.e., the files in the new branch are the same as the files in the `master` branch, with the same content and version history:

```shell
git branch feature
```

5. Undo the last commit on `master`:

```shell
git reset HEAD~1 --hard
```

6. Check the commit history on the `master` branch and the commit history on the `feature` branch to verify the results:

```shell
git log
git checkout feature
git log
```

This is the result of running `git log`:

```shell
commit 7969ab5d6606e2a40c9fd826c732206b835976e9 (HEAD -> feature)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 20:19:22 2023 +0800

    Added hello.txt
```
