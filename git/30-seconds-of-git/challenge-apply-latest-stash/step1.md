# Apply the Latest Stash

## Problem

You are working on a project in your Git repository and have made some changes that are not yet ready to be committed. However, you need to switch to another branch or commit to work on a different feature. You don't want to lose your changes, so you decide to stash them. Later, when you're ready to continue working on your changes, you need to apply the latest stash to your working directory.

## Example

To apply the latest stash to your Git repository, follow these steps:

1. List of your stashes. You should see one stash in the list.
2. Apply the latest stash to your working directory.
3. Check the `README.md` file to see that your changes have been applied.

This is the result of running the `cat README.md` command:

![<an-example-result>](./assets/challenge-apply-latest-stash-step1-1.png)

This command reapplies the changes from the lastest saved save to the current working directory, and adds the new line "This is a new line" to the `README.md` file.

