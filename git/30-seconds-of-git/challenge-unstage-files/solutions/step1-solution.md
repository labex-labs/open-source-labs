```shell
git restore --staged <pathspec>
```

```shell
git restore --staged "newfile.txt"
# Remove the file `newfile.txt` from the staging area

git restore --staged src/*.json
# Remove all files with a `.json` extension in the `src` directory

git restore --staged .
# Remove all changes from the staging area
```
