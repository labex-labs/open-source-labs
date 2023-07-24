# Find Commits that Manipulated a Specific String

As a developer, you may need to find all the commits that modified a specific string in your codebase. For example, you may want to find all the commits that added or removed a specific function name or variable. This can be useful when debugging issues or tracking down the source of a bug.

Suppose you are working on a project hosted on GitHub called `git-playground`. You want to find all the commits that modified the string "Git Playground" in the `README.md` file. Here's how you can do it:

1. Navigate to the repository directory:
```shell
cd git-playground
```
2. Use the `git log -S` command to find all the commits that modified the string "Git Playground" in the `README.md` file and use the arrow keys to navigate through the list of commits. Press <kbd>Q</kbd> to exit the log:
```shell
git log -S"Git Playground" README.md
```

Git will output a list of all the commits that modified the string "Git Playground" in the `README.md` file:
```shell
commit b00b9374a7c549d1af111aa777fdcc868d8a2a01
Author: Hang <huhuhang@gmail.com>
Date:   Wed Apr 26 14:16:00 2023 +0800

    Initial commit
```
