# {{ exit }}

## Introduction

The {{ exit }} challenge is designed to test your ability to use the `os.Exit` function in Go to immediately exit with a given status.

## Problem

The problem to be solved in this challenge is to exit a Go program with a specific status code using the `os.Exit` function.

## Requirements

To complete this challenge, you will need to have a basic understanding of Go programming and the `os` package.

## TODO

Complete the `main` function to exit the program with a status code of `3` using the `os.Exit` function.

```go
package main

import (
	"fmt"
	"os"
)

func main() {
	// TODO: Exit with status 3 using os.Exit
}
```

## Example

```
$ go run main.go
$ echo $?
3
```

## Summary

In this challenge, you learned how to use the `os.Exit` function to immediately exit a Go program with a specific status code. Remember that unlike other programming languages, Go does not use an integer return value from `main` to indicate exit status.
