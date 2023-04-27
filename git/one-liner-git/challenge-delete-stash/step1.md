# Delete a Git Stash

## Problem

You have a Git repository named `https://github.com/labex-labs/git-playground`. You have created a stash using the command `git stash save "my stash"`. Now, you want to delete this stash because you no longer need it.

## Example

1. Clone the Git repository using the command `git clone https://github.com/labex-labs/git-playground`.
2. Change to the repository directory using the command `cd git-playground`.
3. Create a new file named `test.txt` and add some content to it.
4. Save the changes to a stash using the command `git stash save "my stash"`.
5. List all stashes using the command `git stash list`. You should see the stash you just created.
6. Delete the stash using the command `git stash drop stash@{0}`.
7. List all stashes again using the command `git stash list`. The stash you just deleted should no longer be there.
