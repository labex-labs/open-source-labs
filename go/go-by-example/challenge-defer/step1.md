# Defer

## Problem

In this challenge, you need to use `defer` to create a file, write to it, and then close it when you're done.

## Requirements

- The `createFile` function should create a file with the given path and return a pointer to the file.
- The `writeFile` function should write the string "data" to the file.
- The `closeFile` function should close the file and check for errors.

## Example

```sh
# Running the program confirms that the file is closed
# after being written.
$ go run defer.go
creating
writing
closing
```
