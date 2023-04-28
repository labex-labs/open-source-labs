# Find Commits that Manipulated a Specific String

As a developer, you may need to find all the commits that modified a specific string in your codebase. For example, you may want to find all the commits that added or removed a specific function name or variable. This can be useful when debugging issues or tracking down the source of a bug.

Suppose you are working on a project hosted on GitHub called `git-playground`. You want to find all the commits that modified the string "hello world" in the `README.md` file. Here's how you can do it:

1. Clone the `git-playground` repository to your local machine:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Navigate to the repository directory:

```shell
cd git-playground
```

3. Use the `git log -S` command to find all the commits that modified the string "hello world" in the `README.md` file:

```shell
git log -S"hello world" README.md
```

4. Git will output a list of all the commits that modified the string "hello world" in the `README.md` file:

```shell
commit 2a6d3c6c3e6c8d6d7c6d8d6c8d6c8d6c8d6c8d6c
Author: labex
Date: Tue Apr 26 10:10:08 2023 +0300

Update README.md

commit 1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0
Author: john.doe
Date: Mon Apr 25 09:09:07 2023 +0300

Add hello world example to README.md
```

5. Use the arrow keys to navigate through the list of commits. Press <kbd>Q</kbd> to exit the log.
