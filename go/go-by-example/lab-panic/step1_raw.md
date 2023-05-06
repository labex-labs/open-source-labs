# {{ panic }}

## Introduction
The `panic` challenge is designed to test your ability to handle unexpected errors in Golang.

## Problem
The challenge requires you to use the `panic` function to fail fast on errors that shouldn't occur during normal operation or that you aren't prepared to handle gracefully.

## Requirements
- Basic knowledge of Golang programming language.
- Familiarity with error handling in Golang.
- Understanding of the `panic` function in Golang.

## TODO
```go
package main

import "os"

func main() {

	// We'll use panic throughout this site to check for
	// unexpected errors. This is the only program on the
	// site designed to panic.
	panic("a problem")

	// A common use of panic is to abort if a function
	// returns an error value that we don't know how to
	// (or want to) handle. Here's an example of
	// `panic`king if we get an unexpected error when creating a new file.
	_, err := os.Create("/tmp/file")
	if err != nil {
		panic(err)
	}
}
```

## Example
```
panic: a problem

goroutine 1 [running]:
main.main()
	/tmp/sandbox188531485/prog.go:8 +0x39
```

## Summary
In this challenge, you learned how to use the `panic` function to handle unexpected errors in Golang. Remember to use `panic` only when necessary and to handle errors gracefully whenever possible.