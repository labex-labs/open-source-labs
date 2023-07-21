# Change the Last Commit's Author

You have just made a commit to your Git repository, but you realized that the author's name and email address are incorrect. You want to update the author's information without changing the contents of the commit. How can you achieve this using Git?

To change the last commit's author, you can use the `git commit --amend` command. This command allows you to modify the last commit in your Git repository. Here's an example of how you can change the author's name and email address:

1. Clone the Git repository named `https://github.com/labex-labs/git-playground` to your local machine:
```shell
git clone https://github.com/labex-labs/git-playground.git
```
2. Configure Git's identity information using your GitHub account:
```shell
cd git-playground
git config user.email "your email"
git config user.name "your username"
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
```shell
commit d5a385cc354f3528472a215b66cbb7c628ba47d5
Author: Duck Quackers <cool.duck@qua.ck>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt
```
