# Delete a Remote Branch

Sometimes, you may need to delete a remote branch that is no longer needed. For example, if a feature branch has been merged into the main branch, you may want to delete the remote feature branch to keep the repository clean.

Suppose that a GitHub repository called `git-playground` has been cloned from your GitHub account, which comes from a fork of `https://github.com/labex-labs/git-playground.git`. You want to delete the remote branch named `feature-branch` that is no longer needed. Here are the steps to delete the remote branch:

1. Open the terminal and navigate to the local repository directory.
   ```shell
   git clone https://github.com/your-username/git-playground.git
   cd git-playground
   ```
2. Use the `git branch -r` command to list all the remote branches.
   ```shell
   git branch -r
   ```
   The output should include the `feature-branch` remote branch:
   ```
   origin/HEAD -> origin/main
   origin/master
   ```
3. Add the `feature-branch` branch to the `origin` remote repository:
   ```shell
   git checkout -b feature-branch
   git push -u origin feature-branch
   ```
3. Use the `git push -d <remote> <branch>` command to delete the specified remote `<branch>` on the given `<remote>`.
   ```shell
   git push -d origin feature-branch
   ```
   This command deletes the `feature-branch` remote branch on the `origin` remote repository.
4. Use the `git branch -r` command again to verify that the remote branch has been deleted.
   ```shell
   git branch -r
   ```
   The output should not include the `feature-branch` remote branch:
   ```
   origin/HEAD -> origin/master
   origin/master
   ```
