# Commit without Running Git Hooks

## Problem

You have made some changes to your code and want to commit them, but your pre-commit hook is preventing you from doing so. This could be because the hook is checking for syntax errors, code style violations, or other issues that need to be fixed before committing. However, you may need to bypass the hook and commit your changes anyway, perhaps because you are in a hurry or because you disagree with the hook's requirements.

## Example

Suppose you have cloned the `git-playground` repository from GitHub and made some changes to the `README.md` file. You have also added a pre-commit hook that checks for spelling errors in the file. However, you intentionally introduced a spelling mistake to test the hook. When you try to commit your changes, the hook prevents you from doing so:

```shell
$ git add README.md
$ git commit -m "Fix typo"
Spell check failed: README.md:3: misspelling: "comit" = > "commit"
```

To bypass the hook and commit your changes anyway, you can use the `--no-verify` option:

```shell
$ git commit --no-verify -m "Fix typo"
[master 1234567] Fix typo
 1 file changed, 1 insertion(+), 1 deletion(-)
```

This creates a new commit with the message "Fix typo" without running the pre-commit hook.
