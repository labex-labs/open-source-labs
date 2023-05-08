# Command-line flags

## Introduction

The purpose of this challenge is to implement a command-line program that supports basic command-line flag parsing using the `flag` package in Golang.

## Problem

Implement a Golang program that parses command-line flags and outputs the parsed options and any trailing positional arguments. The program should support the following flags:

- `word`: a string flag with a default value of `"foo"`.
- `numb`: an integer flag with a default value of `42`.
- `fork`: a boolean flag with a default value of `false`.
- `svar`: a string flag that uses an existing variable declared elsewhere in the program.

## Requirements

- The program should use the `flag` package to parse command-line flags.
- The program should output the parsed options and any trailing positional arguments.
- The program should support the `word`, `numb`, `fork`, and `svar` flags as described above.

## TODO

```go
// TODO: Declare the `word`, `numb`, `fork`, and `svar` flags using the `flag` package.
// TODO: Parse the command-line flags using the `flag.Parse()` function.
// TODO: Output the parsed options and any trailing positional arguments.
```

## Example

```
$ go run main.go -word=hello -numb=123 -fork=true pos1 pos2
word: hello
numb: 123
fork: true
svar: bar
tail: [pos1 pos2]
```

## Summary

In this challenge, we learned how to use the `flag` package in Golang to parse command-line flags. We implemented a program that supports basic flag parsing and outputs the parsed options and any trailing positional arguments.
