# Create an Empty Commit

## Problem

You need to create an empty commit in your Git repository. This can be useful in several scenarios, such as:

- Triggering a build process  
- Creating a placeholder commit
- Marking a specific point in the repository's history

## Example

For this challenge, fork the Git repository named `https://github.com/labex-labs/git-playground` into your GitHub account.Configure your github account in the environment.You will use the Git repository named `https://github.com/your-username/git-playground` directory. 

1. Clone the repository to your local machine.
2. Navigate to the repository's directory and configure your github account in the environment.
3. Use a command to create an empty commit with the message "Empty commit".
4. Verify that the empty commit was created.

This is where you run `git log --name-status HEAD^. .HEAD` and the result:

![<result>](assets/challenge-create-empty-commit-step1-1.png)
