# File Paths

## Introduction
The `filepath` package in Golang provides functions to parse and construct file paths in a way that is portable between operating systems.

## Problem
In this challenge, you need to use the `filepath` package to perform various operations on file paths, such as constructing paths in a portable way, splitting a path into directory and file components, checking whether a path is absolute, finding the extension of a file, and finding a relative path between two paths.

## Requirements
- Use `Join` to construct paths in a portable way.
- Use `Dir` and `Base` to split a path into directory and file components.
- Use `IsAbs` to check whether a path is absolute.
- Use `Ext` to find the extension of a file.
- Use `TrimSuffix` to remove the extension from a file name.
- Use `Rel` to find a relative path between two paths.

## TODO
```go
// TODO: Use Join to construct a path from the given directory and file name.
path := filepath.Join("dir", "file")

// TODO: Use Dir and Base to split the path into directory and file components.
dir := filepath.Dir(path)
file := filepath.Base(path)

// TODO: Use IsAbs to check whether the path is absolute.
isAbs := filepath.IsAbs(path)

// TODO: Use Ext to find the extension of the file.
ext := filepath.Ext(path)

// TODO: Use TrimSuffix to remove the extension from the file name.
name := strings.TrimSuffix(file, ext)

// TODO: Use Rel to find a relative path between the two paths.
rel, err := filepath.Rel("a/b", "a/b/t/file")
if err != nil {
    panic(err)
}
```

## Example
```
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

## Summary
The `filepath` package in Golang provides functions to work with file paths in a portable way. By using these functions, you can construct paths, split them into directory and file components, check whether they are absolute, find the extension of a file, and find a relative path between two paths.