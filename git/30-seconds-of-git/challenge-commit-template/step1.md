# Add a Commit Message Template

## Problem

Without a commit message template, developers may be tempted to write vague or uninformative commit messages, such as "fixed bug" or "updated code". This makes it difficult for others to understand the purpose of the change and can lead to confusion or mistakes down the line. By setting up a commit message template, developers are encouraged to provide more detailed and informative commit messages, which can improve collaboration and productivity.

## Example

For this challenge, let's use the repository from `https://github.com/labex-labs/git-playground`.

1. Navigate to the repository directory and configure your GitHub identity.
2. Create a new file called `commit-template` in the current directory of the repository.
3. Open the `commit-template` file in a text editor and add the following lines:
```shell
# <type>: <subject>

# <body>

# <footer>

# This creates a template with three sections:
# "<type>" indicates the type of submission, such as "feat" or "fix"
# "<subject>" is a short #summary describing the content of the submission
# "<body>" is a more detailed description
# "<footer>" can contain other metadata, such as the #associated issue number or other comments.
```
4. Press <kbd>Esc</kbd> and enter the <kbd>:wq</kbd> command, then press <kbd>Enter</kbd> to save your changes and exit the `commit-template` file editor.
5. Set the `commit-template` file as the commit message template for the repository.
6. Open the commit message editor and notice that the commit message editor now contains the commit message template you created in step 3.
7. Press <kbd>Esc</kbd> and enter the <kbd>:q</kbd> command, then press <kbd>Enter</kbd> to exit the commit message editor.

This is the final result:

![<result>](./assets/challenge-commit-template-step1-1.png)
