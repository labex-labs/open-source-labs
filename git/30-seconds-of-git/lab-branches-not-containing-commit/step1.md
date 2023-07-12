# Find Branches Not Containing a Commit

You are working on a project with multiple branches, and you need to find all the branches that do not contain a specific commit. This can be useful if you want to make sure that a certain change has been applied to all branches, or if you want to know which branches are outdated and need to be updated.

For this lab, we will be using the Git repository named `https://github.com/your-username/git-playground`. 

1. Clone this repository to your local machine using the following command:
```shell
git clone https://github.com/your-username/git-playground.git
```
2. After cloning the repository, use the following commands to navigate to the directory and configure the identity:
```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```
3. Create and switch to a `new-branch` branch and make some code changes on that branch and then commit it, the commit message is "Create a new-branch branch":
```shell
git checkout -b new-branch
echo "hello,world" > file1.txt
git commit -am "Create a new-branch branch"
```
4. Check the hash of the commit message "Create a new-branch branch":
```shell
git log
```
5. Finds all branches that do not contain a hash with the commit message "Create a new-branch branch". To do this, we can use the following command:
```shell
git branch --no-contains 31c5ac20129151af1
```

This will output a list of all the branches that do not contain the specified commit. In this case, the output will be:
```shell
master
```

This means that the `master` branch do not contain the commit with the hash `31c5ac20129151af1`.
