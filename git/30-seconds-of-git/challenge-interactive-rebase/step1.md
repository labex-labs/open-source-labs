# Perform an Interactive Rebase

## Problem

You are working on a project with a team of developers, and you have made several commits to your branch. However, you realize that some of the commits are unnecessary or need to be combined. You want to clean up your commit history and make it more organized.

## Example

For this challenge, let's use the repository from `https://github.com/labex-labs/git-playground`.

1. Navigate to the directory.
2. Perform an interactive rebase of the last 2 commits.
3. Change "pick" to "squash" in the commit message "Added file2.txt", press <kbd>Esc</kbd> and enter the <kbd>:wq</kbd> command, then press <kbd>Enter</kbd> to save your changes and exit the editor, change the commit message to "Added file1.txt and file2.txt" in the same way and exit.

Running `git log` will give you a result that looks like this:
```shell
commit 7575ded485555c28ecb09487c68e90639bebbe9d (HEAD -> master)
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file1.txt and file2.txt

commit b00b9374a7c549d1af111aa777fdcc868d8a2a01
Author: Hang <huhuhang@gmail.com>
Date:   Wed Apr 26 14:16:00 2023 +0800

    Initial commit
```
    