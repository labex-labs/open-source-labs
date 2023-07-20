# Embed Directive

## Problem

Your task is to modify the given code to embed files and folders into the Go binary and print their contents.

## Requirements

- You must use the `embed` package to embed files and folders.
- You must use the `string` and `[]byte` types to store the contents of the embedded files.
- You must use the `embed.FS` type to embed multiple files or folders with wildcards.
- You must print the contents of the embedded files.

## Example

```sh
# Use these commands to run the example.
# (Note: due to limitation on go playground,
# this example can only be run on your local machine.)
$ mkdir -p folder
$ echo "hello go" > folder/single_file.txt
$ echo "123" > folder/file1.hash
$ echo "456" > folder/file2.hash

$ go run embed-directive.go
hello go
hello go
123
456
```
