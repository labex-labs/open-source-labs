# Line Filters

## Introduction

The Line Filters lab is a common type of program that reads input on stdin, processes it, and then prints some derived result to stdout. The purpose of this lab is to write a Go program that reads input text and modifies it according to specific requirements.

The problem to be solved in this lab is to write a Go program that reads input text from stdin, capitalizes all the letters in the text, and then prints the modified text to stdout.

- The program must read input text from stdin.
- The program must capitalize all the letters in the input text.
- The program must print the modified text to stdout.

## TODO

```go
package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	for scanner.Scan() {
		ucl := strings.ToUpper(scanner.Text())

		// TODO: Modify the code to print the modified text to stdout.
	}

	if err := scanner.Err(); err != nil {
		fmt.Fprintln(os.Stderr, "error:", err)
		os.Exit(1)
	}
}
```

Input:

```
hello world
```

Output:

```
HELLO WORLD
```

## Summary

The Line Filters lab requires writing a Go program that reads input text from stdin, capitalizes all the letters in the text, and then prints the modified text to stdout. This lab is a great way to practice writing Go programs that read and modify input text.
