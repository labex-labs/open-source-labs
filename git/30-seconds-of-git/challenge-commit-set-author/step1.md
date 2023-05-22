# Create a commit by a different author

## Problem

Suppose you are working on a project with a team of developers, and one of your team members has made some changes to the code. However, they are not available to commit the changes themselves, and you need to create a commit on their behalf. In this scenario, you can use the `--author` option to change the name and email of the commit's author. This option is useful when you need to attribute a commit to a different person, such as when you are committing code on behalf of a colleague who is on vacation or sick leave.

## Example

Let's say you are working on a project hosted on the `https://github.com/labex-labs/git-playground` repository. You have made some changes to the code, e.g. "Fix the bug" is added to the `README`.md file in your GitHub account, and you need to make a commit on behalf of your colleague John Doe, who cannot commit these changes himself.

This command will create a new commit with the message "Fix the bug" and attribute it to John Doe:

![<result>](assets/challenge-commit-set-author-step1-1.png)
