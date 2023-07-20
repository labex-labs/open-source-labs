# Reset Local Master Branch to Match Remote

You have been working on a project and have made changes to the local `master` branch. However, you realize that the remote `master` branch has been updated with new changes that you do not have in your local branch. You need to reset the local `master` branch to match the one on the remote.

1. Clone the Git repository named `https://github.com/labex-labs/git-playground` directory:
   ```shell
   git clone https://github.com/labex-labs/git-playground
   ```
2. Retrieve the latest updates from the remote:
   ```shell
   git fetch origin
   ```
3. Switch to the `master` branch:
   ```shell
   git checkout master
   ```
4. Update the contents of file1.txt to "hello" and add it to the staging area:
   ```shell
   echo "hello" > file1.txt
   git add .
   ```
5. View current status:
   ```shell
   git status
   ```
6. Reset the local `master` branch to match the one on the remote:
   ```shell
   git reset --hard origin/master
   ```
7. Verify that the local `master` branch is now up to date with the remote `master` branch:
   ```shell
   git status
   ```

This is the finished result：

![<result>](./assets/challenge-reset-master-step1-1.png)
