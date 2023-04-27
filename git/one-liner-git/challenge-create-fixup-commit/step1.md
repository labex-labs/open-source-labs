# Create a Fixup Commit

## Problem

Suppose you are working on a project with several other developers, and you notice a small error in a commit that was made a few days ago. You want to fix the error, but you don't want to create a new commit and disrupt the work of the other developers. This is where fixup commits come in handy. By creating a fixup commit, you can make the necessary changes without creating a new commit, and the fixup commit will be automatically merged with the original commit during the next rebase.

## Example

To create a fixup commit, you can use the `git commit --fixup <commit>` command. For example, suppose you want to create a fixup commit for the commit with the hash `3050fc0de`. Here's how you would do it:

```shell
git add .
git commit --fixup 3050fc0de
```

This will create a fixup commit for the specified commit. Note that you must stage your changes before creating the fixup commit.

Once you have created the fixup commit, you can use the `git rebase --autosquash` command to automatically merge the fixup commit with the original commit during the next rebase. For example:

```shell
git rebase HEAD~5 --autosquash
```

This will perform a rebase on the last 5 commits, and automatically merge any fixup commits with their corresponding original commits.
