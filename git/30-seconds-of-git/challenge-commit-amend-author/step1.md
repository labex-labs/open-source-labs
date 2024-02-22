# Change the Last Commit's Author

You have just made a commit to your Git repository, but you realized that the author's name and email address are incorrect. You want to update the author's information without changing the contents of the commit. How can you achieve this using Git?

## Tasks

To change the last commit's author, you can use a command. This command allows you to modify the last commit in your Git repository.

1. Navigate to the repository and configure Git's identity information using your GitHub account.
2. Change the author of the last commit to `Duck Quackers`, whose email address is `cool.duck@qua.ck` and save the contents.
3. Verify that the author's information has been updated.

You should see that the last commit's author is now `Duck Quackers`:

```shell
commit d5a385cc354f3528472a215b66cbb7c628ba47d5
Author: Duck Quackers <cool.duck@qua.ck>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt
```
