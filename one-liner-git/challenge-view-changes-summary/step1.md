# Git Challenge: View Changes Between Commits

## Problem

As a developer, you have been working on a project hosted on the `https://github.com/labex-labs/git-playground` repository. You have made several commits to the repository, and you want to view a summary of the changes between two specific commits. However, you are not sure how to do this using Git.

## Example

To view a summary of changes between two commits, you can use the `git shortlog` command. For example, let's say you want to view the changes between the `HEAD` commit and the commit with the hash `3050fc0de`. Here's how you can do it:

1. Open a terminal window and navigate to the directory where the `git-playground` repository is located.
2. Run the following command: `git shortlog 3050fc0de..HEAD`
3. Git will display a summary of the changes between the two commits. You can use the arrow keys to navigate through the summary, and press `Q` to exit.

Here's an example of what the output might look like:

```shell
git shortlog 3050fc0de..HEAD
# Duck Quacking (2):
#      Fix network bug
#      Update documentation
```

In this example, Git is showing that there were two commits between the `3050fc0de` commit and the `HEAD` commit. The first commit fixed a network bug, and the second commit updated the documentation.
