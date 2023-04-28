# Update Remote Branch After Rewriting History

When you rewrite history locally, you create a new commit with a different SHA-1 hash. This means that the commit history on your local branch is different from the commit history on the remote branch. If you try to push your changes to the remote branch, Git will reject the push because it will see the commit history as diverged. To solve this problem, you need to force an update of the remote branch.

To demonstrate how to update a remote branch after rewriting history, we will use the `git-playground` repository. This repository contains a simple Python script that prints "Hello, World!" to the console.

1. Clone the `git-playground` repository to your local machine:
   ```
   git clone https://github.com/labex-labs/git-playground.git
   ```
2. Create a new branch called `feature` and switch to it:
   ```
   git checkout -b feature
   ```
3. Modify the Python script to print "Hello, Git!" instead of "Hello, World!":
   ```
   sed -i 's/World/Git/g' hello.py
   ```
4. Commit the changes:
   ```
   git commit -am "Update greeting"
   ```
5. Push the changes to the remote repository:
   ```
   git push origin feature
   ```
   This should succeed because you are the only one working on the `feature` branch.
6. Switch to the `master` branch:
   ```
   git checkout master
   ```
7. Modify the Python script to print "Hello, Labex!" instead of "Hello, World!":
   ```
   sed -i 's/World/Labex/g' hello.py
   ```
8. Commit the changes:
   ```
   git commit -am "Update greeting"
   ```
9. Pull the changes from the remote repository:
   ```
   git pull origin master
   ```
10. Switch back to the `feature` branch:
    ```
    git checkout feature
    ```
11. Rebase the `feature` branch onto the `master` branch:
    ```
    git rebase master
    ```
12. Push the changes to the remote repository:
    ```
    git push -f origin feature
    ```
    The `-f` flag forces Git to update the remote branch with your changes, even though the commit history has diverged.
