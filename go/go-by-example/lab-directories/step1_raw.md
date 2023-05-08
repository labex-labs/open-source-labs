# Directories

## Introduction
In this challenge, you will learn how to work with directories in Go. Go provides several useful functions for working with directories in the file system.

## Problem
Create a Go program that creates a new sub-directory in the current working directory, creates a hierarchy of directories, including parents, lists directory contents, changes the current working directory, and visits a directory recursively.

## Requirements
- Create a new sub-directory in the current working directory.
- When creating temporary directories, it's good practice to `defer` their removal. `os.RemoveAll` will delete a whole directory tree (similarly to `rm -rf`).
- Create a hierarchy of directories, including parents with `MkdirAll`. This is similar to the command-line `mkdir -p`.
- `ReadDir` lists directory contents, returning a slice of `os.DirEntry` objects.
- `Chdir` lets us change the current working directory, similarly to `cd`.
- Visit a directory recursively, including all its sub-directories. `Walk` accepts a callback function to handle every file or directory visited.

## TODO
```
// Create a new sub-directory in the current working
// directory.
err := os.Mkdir("subdir", 0755)
check(err)

// When creating temporary directories, it's good
// practice to `defer` their removal. `os.RemoveAll`
// will delete a whole directory tree (similarly to
// `rm -rf`).
defer os.RemoveAll("subdir")

// Helper function to create a new empty file.
createEmptyFile := func(name string) {
    d := []byte("")
    check(os.WriteFile(name, d, 0644))
}

createEmptyFile("subdir/file1")

// We can create a hierarchy of directories, including
// parents with `MkdirAll`. This is similar to the
// command-line `mkdir -p`.
err = os.MkdirAll("subdir/parent/child", 0755)
check(err)

createEmptyFile("subdir/parent/file2")
createEmptyFile("subdir/parent/file3")
createEmptyFile("subdir/parent/child/file4")

// `ReadDir` lists directory contents, returning a
// slice of `os.DirEntry` objects.
c, err := os.ReadDir("subdir/parent")
check(err)

fmt.Println("Listing subdir/parent")
for _, entry := range c {
    fmt.Println(" ", entry.Name(), entry.IsDir())
}

// `Chdir` lets us change the current working directory,
// similarly to `cd`.
err = os.Chdir("subdir/parent/child")
check(err)

// Now we'll see the contents of `subdir/parent/child`
// when listing the *current* directory.
c, err = os.ReadDir(".")
check(err)

fmt.Println("Listing subdir/parent/child")
for _, entry := range c {
    fmt.Println(" ", entry.Name(), entry.IsDir())
}

// `cd` back to where we started.
err = os.Chdir("../../..")
check(err)

// We can also visit a directory *recursively*,
// including all its sub-directories. `Walk` accepts
// a callback function to handle every file or
// directory visited.
fmt.Println("Visiting subdir")
err = filepath.Walk("subdir", visit)
}

// `visit` is called for every file or directory found
// recursively by `filepath.Walk`.
func visit(p string, info os.FileInfo, err error) error {
if err != nil {
    return err
}
fmt.Println(" ", p, info.IsDir())
return nil
}
```

## Example
```
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

## Summary
In this challenge, you learned how to work with directories in Go. You learned how to create a new sub-directory, create a hierarchy of directories, list directory contents, change the current working directory, and visit a directory recursively.