# Number Parsing

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

## Example

```sh
$ go run number-parsing.go 
1.234
123
456
789
135
strconv.ParseInt: parsing "wat": invalid syntax

# Next we'll look at another common parsing task: URLs.

```

## Solution

```go
// Parsing numbers from strings is a basic but common task
// in many programs; here's how to do it in Go.

package main

// The built-in package `strconv` provides the number
// parsing.
import (
	"fmt"
	"strconv"
)

func main() {

	// With `ParseFloat`, this `64` tells how many bits of
	// precision to parse.
	f, _ := strconv.ParseFloat("1.234", 64)
	fmt.Println(f)

	// For `ParseInt`, the `0` means infer the base from
	// the string. `64` requires that the result fit in 64
	// bits.
	i, _ := strconv.ParseInt("123", 0, 64)
	fmt.Println(i)

	// `ParseInt` will recognize hex-formatted numbers.
	d, _ := strconv.ParseInt("0x1c8", 0, 64)
	fmt.Println(d)

	// A `ParseUint` is also available.
	u, _ := strconv.ParseUint("789", 0, 64)
	fmt.Println(u)

	// `Atoi` is a convenience function for basic base-10
	// `int` parsing.
	k, _ := strconv.Atoi("135")
	fmt.Println(k)

	// Parse functions return an error on bad input.
	_, e := strconv.Atoi("wat")
	fmt.Println(e)
}

```