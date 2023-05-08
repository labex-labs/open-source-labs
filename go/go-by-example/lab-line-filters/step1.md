# Line Filters

## Problem

The problem to be solved in this challenge is to write a Go program that reads input text from stdin, capitalizes all the letters in the text, and then prints the modified text to stdout.

## Requirements

- The program must read input text from stdin.
- The program must capitalize all the letters in the input text.
- The program must print the modified text to stdout.

## Example

```sh
# To try out our line filter, first make a file with a few
# lowercase lines.
$ echo 'hello' > /tmp/lines
$ echo 'filter' >> /tmp/lines

# Then use the line filter to get uppercase lines.
$ cat /tmp/lines | go run line-filters.go
HELLO
FILTER
```

## Solution

```go
// A _line filter_ is a common type of program that reads
// input on stdin, processes it, and then prints some
// derived result to stdout. `grep` and `sed` are common
// line filters.

// Here's an example line filter in Go that writes a
// capitalized version of all input text. You can use this
// pattern to write your own Go line filters.
package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {

	// Wrapping the unbuffered `os.Stdin` with a buffered
	// scanner gives us a convenient `Scan` method that
	// advances the scanner to the next token; which is
	// the next line in the default scanner.
	scanner := bufio.NewScanner(os.Stdin)

	for scanner.Scan() {
		// `Text` returns the current token, here the next line,
		// from the input.
		ucl := strings.ToUpper(scanner.Text())

		// Write out the uppercased line.
		fmt.Println(ucl)
	}

	// Check for errors during `Scan`. End of file is
	// expected and not reported by `Scan` as an error.
	if err := scanner.Err(); err != nil {
		fmt.Fprintln(os.Stderr, "error:", err)
		os.Exit(1)
	}
}

```
