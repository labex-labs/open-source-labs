# View Merged Branches

Your task is to print a list of all merged local branches in the Git repository named `https://github.com/labex-labs/git-playground`. You will need to use the command `git branch -a --merged` to display the list of merged branches. Once you have the list, you should be able to navigate through it using the arrow keys and exit by pressing <kbd>Q</kbd>.

1. Clone the `git-playground` repository:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Navigate to the repository directory:

```shell
cd git-playground
```

3. Create a new branch and make some changes:

```shell
git checkout -b my-branch
touch new-file.txt
git add new-file.txt
git commit -m "Add new-file.txt"
```

4. Merge the branch into the main branch:

```shell
git checkout main
git merge my-branch
```

5. View the list of merged branches:

```shell
git branch -a --merged
```

6. Use the arrow keys to navigate through the list and press <kbd>Q</kbd> to exit.
