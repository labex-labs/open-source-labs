---
title: Remove files from the staging area
---

Removes files from the staging area.

- Use `git restore --staged <pathspec>` to remove files from the staging area.
- `<pathspec>` can be a filename or a fileglob.

```shell
git restore --staged <pathspec>
```

```shell
git restore --staged "labex.txt"
# Remove the file `labex.txt` from the staging area

git restore --staged src/*.json
# Remove all files with a `.json` extension in the `src` directory

git restore --staged .
# Remove all changes from the staging area
```
