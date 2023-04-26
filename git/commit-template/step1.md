# Add a Commit Message Template

## Problem

Without a commit message template, developers may be tempted to write vague or uninformative commit messages, such as "fixed bug" or "updated code". This makes it difficult for others to understand the purpose of the change and can lead to confusion or mistakes down the line. By setting up a commit message template, developers are encouraged to provide more detailed and informative commit messages, which can improve collaboration and productivity.

## Example

For this challenge, we will be using the Git repository named `https://github.com/labex-labs/git-playground`. Follow these steps to set up a commit message template for this repository:

1. Clone the repository to your local machine using the command `git clone https://github.com/labex-labs/git-playground`.
2. Navigate to the repository directory using the command `cd git-playground`.
3. Create a new file named `commit-template` in the repository directory using the command `touch commit-template`.
4. Open the `commit-template` file in a text editor and add the following lines:

```
# <type>: <subject>

# <body>

# <footer>
```

5. Save and close the `commit-template` file.
6. Use the command `git config commit.template commit-template` to set the `commit-template` file as the commit message template for the repository.
7. Make a change to the codebase using the command `echo "test" >> README.md`.
8. Use the command `git add README.md` to stage the change.
9. Use the command `git commit` to open the commit message editor.
10. Notice that the commit message editor now includes the commit message template you created in step 4. Fill in the template with a type, subject, body, and footer that describe your change.
11. Save and close the commit message editor.
12. Use the command `git push` to push your changes to the remote repository.
