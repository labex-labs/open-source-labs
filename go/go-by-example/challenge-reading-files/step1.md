# Reading Files

## Problem

You need to read files in your Go program and perform different operations on the data in the file.

## Requirements

- You should be familiar with basic Go programming concepts.
- You should have Go installed on your computer.

## Example

```sh
$ echo "hello" > /tmp/dat
$ echo "go" >> /tmp/dat
$ go run reading-files.go
hello
go
5 bytes: hello
2 bytes @ 6: go
2 bytes @ 6: go
5 bytes: hello

# Next we'll look at writing files.
```
