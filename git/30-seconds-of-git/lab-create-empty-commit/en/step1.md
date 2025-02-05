# Create an Empty Commit

You need to create an empty commit in your Git repository. This can be useful in several scenarios, such as:

- Triggering a build process
- Creating a placeholder commit
- Marking a specific point in the repository's history

For this lab, let's use the repository from `https://github.com/labex-labs/git-playground`:

1. Clone the repository to your local machine using the command `git clone https://github.com/labex-labs/git-playground`.
2. Navigate to the repository's directory using the command `cd git-playground` and configure your github account in the environment using commands `git config --global user.name "your-uername"` and `git config --global user.email "your-email"`.
3. Use the command `git commit --allow-empty -m "Empty commit"` to create an empty commit with the message "Empty commit".
4. Verify that the empty commit was created by using the command `git log --name-status HEAD^..HEAD`.

This is where you run `git log --name-status HEAD^..HEAD` and the result:

![git log empty commit result](../assets/challenge-create-empty-commit-step1-1.png)
