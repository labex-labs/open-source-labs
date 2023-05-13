# Apply a stash

## Problem

You are working on a feature branch in the `git-playground` repository and you need to switch to another branch to work on a bug fix. However, you have some changes that are not ready to be committed yet. You want to save these changes and switch to the other branch. Once you are done with the bug fix, you want to apply the stash and continue working on your feature branch.

## Example

1. Clone the `git-playground` repository from the link https://github.com/git-tutorial/git-tutorial.git.
2. Change to the `git-playground` directory.
3. Create a new branch called `feature-branch`.
4. Make some changes to the files in the repository, add "some changes" to the README.md file. 
5. Save the changes to a stash.
6. Switch to the `master` branch.
7. Make some changes to the files in the repository,add "some bug fixes" to the README.md file. 
8. Switch back to the `feature-branch`.
9. Apply the stash.
10. Check the status of the repository.

This is the result after completing the challenge:


You should see that the changes you made before stashing are now applied.
