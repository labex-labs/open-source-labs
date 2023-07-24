# Add a Commit Message Template

Without a commit message template, developers may be tempted to write vague or uninformative commit messages, such as "fixed bug" or "updated code". This makes it difficult for others to understand the purpose of the change and can lead to confusion or mistakes down the line. By setting up a commit message template, developers are encouraged to provide more detailed and informative commit messages, which can improve collaboration and productivity.

For this lab, fork the Git repository named `https://github.com/labex-labs/git-playground` into your GitHub account. Follow these steps to set up a commit message template for this repository:

1. Clone the repository to your local machine using the command `git clone https://github.com/your-username/git-playground`.
2. Configure your GitHub account using the commands `git config --global user.name "your-username"` and `git config --global user.email "your-email"` and navigate to the repository directory using the command `cd git-playground`.
3. Create a new file named `commit-template` in the repository directory using the command `touch commit-template`.
4. Open the `commit-template` file in a text editor and add the following lines:

```
# <type>: <subject>

# <body>

# <footer>

#This creates a template with three sections, where "<type>" indicates the type of submission, such as "feat" or "fix", "<subject>" is a short #summary describing the content of the submission, "<body>" is a more detailed description, and "<footer>" can contain other metadata, such as the #associated issue number or other comments.
```

5. Save and close the `commit-template` file.
6. Use the command `git config commit.template commit-template` to set the `commit-template` file as the commit message template for the repository.
7. Make a change to the codebase using the command `echo "test" >> README.md`.
8. Use the command `git add README.md` to stage the change.
9. Use the command `git commit` to open the commit message editor.
10. Please note that the submission message editor now includes the submission message template you created in step 4. Fill in the template with a description of the type, subject, body and footer of your changes, e.g:

```
feat: Add test to README.md

Add a new line to the README.md file with the text "test", to test the Git commit message template.

# This change is not expected to affect any existing functionality.

# Related issue(s): none
```

11. Save and close the commit message editor.
12. Give your account permissions to the environment.
13. Use the command `git push` to push your changes to the remote repository.

Check with `git log --oneline origin/master` gives the following results:

![<result>](./assets/challenge-commit-template-step1-1.png)
