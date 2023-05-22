# Change the Last Commit's Author

You have just made a commit to your Git repository, but you realized that the author's name and email address are incorrect. You want to update the author's information without changing the contents of the commit. How can you achieve this using Git?

To change the last commit's author, you can use the `git commit --amend` command. This command allows you to modify the last commit in your Git repository. Here's an example of how you can change the author's name and email address:

1. Clone the Git repository named `https://github.com/labex-labs/git-playground` to your local machine:
```shell
git clone https://github.com/labex-labs/git-playground.git
```
2. Configure Git's identity information using your GitHub account and make some changes to the files in the repository:
```shell
cd git-playground
git config user.email "your email"
git config user.name "your username"
echo "Hello, World" > hello.txt
git add hello.txt
git commit -m "Initial commit"
```
3. Use the `git commit --amend` command to modify the last commit's author and save the contents:
```shell
git commit --amend --author="Duck Quackers <cool.duck@qua.ck>"
```
4. Verify that the author's information has been updated:
```shell
git log
```

You should see that the last commit's author is now `Duck Quackers`:

![<result>](assets/challenge-commit-amend-author-step1-1.png)
