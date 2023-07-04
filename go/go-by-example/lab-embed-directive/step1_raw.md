# Embed Directive

## Introduction

This lab aims to test your understanding of the `embed` package in Golang. The `embed` package allows programs to include arbitrary files and folders in the Go binary at build time.

Your task is to modify the given code to embed files and folders into the Go binary and print their contents.

- You must use the `embed` package to embed files and folders.
- You must use the `string` and `[]byte` types to store the contents of the embedded files.
- You must use the `embed.FS` type to embed multiple files or folders with wildcards.
- You must print the contents of the embedded files.

## TODO

```go
// TODO: Embed the contents of the folder into a variable of type `embed.FS`.
// Hint: Use the `//go:embed` directive with wildcards.
// TODO: Print the contents of `single_file.txt`.
// TODO: Print the contents of `single_file.txt` as a byte slice.
// TODO: Retrieve the contents of `file1.hash` from the embedded folder and print it.
// TODO: Retrieve the contents of `file2.hash` from the embedded folder and print it.
```

```
This is the content of single_file.txt
This is the content of single_file.txt
This is the content of file1.hash
This is the content of file2.hash
```

## Summary

In this lab, you learned how to use the `embed` package to embed files and folders into the Go binary at build time. You also learned how to use the `string` and `[]byte` types to store the contents of the embedded files, and how to use the `embed.FS` type to embed multiple files or folders with wildcards.
