# Delete a Git Stash

You have a Git repository named `https://github.com/labex-labs/git-playground`. You have created a stash using the command `git stash save "my stash"`. Now, you want to delete this stash because you no longer need it.

1. Change to the repository directory using the command `cd git-playground`.
2. List all stashes using the command `git stash list`. You should see the stash you just created.
3. Delete the stash using the command `git stash drop stash@{0}`.
4. List all stashes again using the command `git stash list`.

The stash you just deleted should no longer be there.
