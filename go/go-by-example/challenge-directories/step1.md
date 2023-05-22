# Directories

## Problem

Create a Go program that creates a new sub-directory in the current working directory, creates a hierarchy of directories, including parents, lists directory contents, changes the current working directory, and visits a directory recursively.

## Requirements

- Create a new sub-directory in the current working directory.
- When creating temporary directories, it's good practice to `defer` their removal. `os.RemoveAll` will delete a whole directory tree (similarly to `rm -rf`).
- Create a hierarchy of directories, including parents with `MkdirAll`. This is similar to the command-line `mkdir -p`.
- `ReadDir` lists directory contents, returning a slice of `os.DirEntry` objects.
- `Chdir` lets us change the current working directory, similarly to `cd`.
- Visit a directory recursively, including all its sub-directories. `Walk` accepts a callback function to handle every file or directory visited.

## Example

```sh
$ go run directories.go
Listing subdir/parent
child true
file2 false
file3 false
Listing subdir/parent/child
file4 false
Visiting subdir
subdir true
subdir/file1 false
subdir/parent true
subdir/parent/child true
subdir/parent/child/file4 false
subdir/parent/file2 false
subdir/parent/file3 false
```
