# Number Parsing

## Introduction
The purpose of this challenge is to demonstrate how to parse numbers from strings in Go.

## Problem
Parsing numbers from strings is a common task in many programs. This challenge requires you to use the built-in `strconv` package to parse different types of numbers from strings.

## Requirements
- Use the `strconv` package to parse numbers from strings.
- Parse a float with `ParseFloat`.
- Parse an int with `ParseInt`.
- Parse a hex-formatted number with `ParseInt`.
- Parse an unsigned int with `ParseUint`.
- Parse a base-10 int with `Atoi`.
- Handle errors returned by the parse functions.

## TODO
Complete the code below by using the `strconv` package to parse numbers from strings. Use the TODO keyword to mark the code that needs to be completed.

```go
package main

import (
	"fmt"
	"strconv"
)

func main() {
	f, _ := strconv.ParseFloat("1.234", 64)
	fmt.Println(f)

	i, _ := strconv.ParseInt("123", 0, 64)
	fmt.Println(i)

	d, _ := strconv.ParseInt("0x1c8", 0, 64)
	fmt.Println(d)

	u, _ := strconv.ParseUint("789", 0, 64)
	fmt.Println(u)

	k, _ := strconv.Atoi("135")
	fmt.Println(k)

	// TODO: Parse an int from the string "wat" and handle the error.
}
```

## Example
The output of the completed code should be:
```
1.234
123
456
789
135
strconv.Atoi: parsing "wat": invalid syntax
```

## Summary
This challenge demonstrated how to parse different types of numbers from strings in Go using the `strconv` package. By completing this challenge, you should have a better understanding of how to handle number parsing in your Go programs.