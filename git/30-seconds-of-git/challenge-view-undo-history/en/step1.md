# View "Undo" History

As a developer, you may need to undo changes that you've made to your codebase. Git provides several ways to undo changes, such as using the `git reset` or `git revert` commands. However, it can be difficult to keep track of all the actions you've taken, especially if you've used more advanced commands like `git rebase`.

## Tasks

Let's say you've made some changes to a repository and want to undo them.

1. Navigate to the repository.
2. Now, you realize that you made a mistake and want to undo the last commit.
3. You may realize that you've made another mistake and want to undo the reset. View the reference log and find the commit hash of the previous commit.
4. You can see that the previous commit hash is `d22f46b` and use this hash to reset the repository back to the previous commit.
5. View historical commit records to verify results.

Here is the result of step 3. This will display a list of all the actions you've taken in the repository, including the reset:

```shell
cf80005 (HEAD -> master) HEAD@{0}: reset: moving to HEAD~1
d22f46b (origin/master, origin/feature-branch, origin/HEAD) HEAD@{1}: clone: from https://github.com/labex-labs/git-playground.git
```
