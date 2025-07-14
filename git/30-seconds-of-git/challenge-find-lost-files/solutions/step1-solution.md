# Step 1 Solution

To solve this challenge, you need to first create a "lost" commit and then use `git fsck` to find it. Here are the detailed steps:

1.  First, navigate to the `git-playground` repository and configure your Git identity.

    ```shell
    cd /home/labex/project/git-playground
    git config --global user.name "labex"
    git config --global user.email "labex@labex.io"
    ```

2.  Create a new branch `one-branch`, and switch to it.

    ```shell
    git checkout -b one-branch
    ```

3.  On the new branch, delete the `file2.txt` and commit this change. This creates a new commit object.

    ```shell
    git rm file2.txt
    git commit -m "Remove file2"
    ```

4.  Switch back to the `master` branch.

    ```shell
    git checkout master
    ```

5.  Now, delete the `one-branch` branch. Because this was the only branch pointing to the commit where `file2.txt` was deleted, that commit is now "lost" or "dangling".

    ```shell
    git branch -D one-branch
    ```

6.  Run `git fsck --lost-found`. This command will search for any dangling objects (like our lost commit) and restore them into the `.git/lost-found` directory.

    ```shell
    git fsck --lost-found
    ```

7.  Finally, list the contents of the `.git/lost-found` directory to verify that the lost commit has been found. You should see a `commit` object.

    ```shell
    ls .git/lost-found
    ```
