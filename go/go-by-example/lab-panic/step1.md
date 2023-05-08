# Panic

## Problem

The challenge requires you to use the `panic` function to fail fast on errors that shouldn't occur during normal operation or that you aren't prepared to handle gracefully.

## Requirements

- Basic knowledge of Golang programming language.
- Familiarity with error handling in Golang.
- Understanding of the `panic` function in Golang.

## Example

```sh
# Running this program will cause it to panic, print
# an error message and goroutine traces, and exit with
# a non-zero status.

# When first panic in `main` fires, the program exits
# without reaching the rest of the code. If you'd like
# to see the program try to create a temp file, comment
# the first panic out.
$ go run panic.go
panic: a problem

goroutine 1 [running]:
main.main()
	/.../panic.go:12 +0x47
...
exit status 2

# Note that unlike some languages which use exceptions
# for handling of many errors, in Go it is idiomatic
# to use error-indicating return values wherever possible.

```

## Solution

```go
// A `panic` typically means something went unexpectedly
// wrong. Mostly we use it to fail fast on errors that
// shouldn't occur during normal operation, or that we
// aren't prepared to handle gracefully.

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