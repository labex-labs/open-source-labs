# File Paths

## Problem

In this challenge, you need to use the `filepath` package to perform various operations on file paths, such as constructing paths in a portable way, splitting a path into directory and file components, checking whether a path is absolute, finding the extension of a file, and finding a relative path between two paths.

## Requirements

- Use `Join` to construct paths in a portable way.
- Use `Dir` and `Base` to split a path into directory and file components.
- Use `IsAbs` to check whether a path is absolute.
- Use `Ext` to find the extension of a file.
- Use `TrimSuffix` to remove the extension from a file name.
- Use `Rel` to find a relative path between two paths.

## Example

```sh
$ go run file-paths.go
p: dir1/dir2/filename
dir1/filename
dir1/filename
Dir(p): dir1/dir2
Base(p): filename
false
true
.json
config
t/file
../c/t/file

```
