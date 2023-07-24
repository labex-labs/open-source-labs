# {{ exit }}

## Introduction

The {{ exit }} lab is designed to test your ability to use the `os.Exit` function in Go to immediately exit with a given status.

The problem to be solved in this lab is to exit a Go program with a specific status code using the `os.Exit` function.

To complete this lab, you will need to have a basic understanding of Go programming and the `os` package.

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

```
$ go run main.go
$ echo $?
3
```

## Summary

In this lab, you learned how to use the `os.Exit` function to immediately exit a Go program with a specific status code. Remember that unlike other programming languages, Go does not use an integer return value from `main` to indicate exit status.
