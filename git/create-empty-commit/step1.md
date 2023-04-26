# Create an Empty Commit

## Problem

You need to create an empty commit in your Git repository. This can be useful in several scenarios, such as:

- Triggering a build process
- Creating a placeholder commit
- Marking a specific point in the repository's history

## Example

For this challenge, we will use the Git repository named `https://github.com/labex-labs/git-playground` directory. Follow these steps to create an empty commit:

1. Clone the repository to your local machine using the command `git clone https://github.com/labex-labs/git-playground`.
2. Navigate to the repository's directory using the command `cd git-playground`.
3. Use the command `git commit --allow-empty -m "Empty commit"` to create an empty commit with the message "Empty commit".
4. Verify that the empty commit was created by using the command `git log`.

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git commit --allow-empty -m "Empty commit"
git log
```
