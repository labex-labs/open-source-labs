# Find Lost Files

You have been working on a project in the `git-playground` repository. However, you have noticed that some files are missing and you are not sure when they were deleted or how to recover them. Your task is to use Git to find any lost files and commits in the repository.

1. Clone the `git-playground` repository:
```shell
git clone https://github.com/labex-labs/git-playground.git
```
2. Navigate to the repository directory:
```shell
cd git-playground
```
3. Run the `git fsck --lost-found` command to find any lost files and commits:
```shell
git fsck --lost-found
```
4. Check the `.git/lost-found` directory to see if any lost files were recovered:
```shell
ls .git/lost-found
```
5. If any lost files were found, review them to determine if they are the missing files.
