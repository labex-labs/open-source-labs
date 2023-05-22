# Multiple Return Values

## Problem

Complete the `swap` function to return two input parameters in reverse order.

## Requirements

- The `swap` function should take two integers as input parameters.
- The `swap` function should return two integers in reverse order.

## Example

```sh
$ go run multiple-return-values.go
3
7
7

# Accepting a variable number of arguments is another nice
# feature of Go functions; we'll look at this next.
```

## Solution

```go
// Go has built-in support for _multiple return values_.
// This feature is used often in idiomatic Go, for example
// to return both result and error values from a function.

package main

import "fmt"

// The `(int, int)` in this function signature shows that
// the function returns 2 `int`s.
func vals() (int, int) {
	return 3, 7
}

func main() {

	// Here we use the 2 different return values from the
	// call with _multiple assignment_.
	a, b := vals()
	fmt.Println(a)
	fmt.Println(b)

	// If you only want a subset of the returned values,
	// use the blank identifier `_`.
	_, c := vals()
	fmt.Println(c)
}

```
