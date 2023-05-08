# Functions

## Problem

In the given code, we have two functions `plus` and `plusPlus`. The `plus` function takes two integers as arguments and returns their sum. The `plusPlus` function takes three integers as arguments and returns their sum. Your task is to complete the `plusPlus` function by adding the third integer to the sum of the first two integers.

## Requirements

- The `plus` function should take two integers as arguments and return their sum as an integer.
- The `plusPlus` function should take three integers as arguments and return their sum as an integer.
- The `plusPlus` function should use the `plus` function to calculate the sum of the first two integers.

## Example

```sh
$ go run functions.go 
1+2 = 3
1+2+3 = 6

# There are several other features to Go functions. One is
# multiple return values, which we'll look at next.

```

## Solution

```go
// _Functions_ are central in Go. We'll learn about
// functions with a few different examples.

package main

import "fmt"

// Here's a function that takes two `int`s and returns
// their sum as an `int`.
func plus(a int, b int) int {

	// Go requires explicit returns, i.e. it won't
	// automatically return the value of the last
	// expression.
	return a + b
}

// When you have multiple consecutive parameters of
// the same type, you may omit the type name for the
// like-typed parameters up to the final parameter that
// declares the type.
func plusPlus(a, b, c int) int {
	return a + b + c
}

func main() {

	// Call a function just as you'd expect, with
	// `name(args)`.
	res := plus(1, 2)
	fmt.Println("1+2 =", res)

	res = plusPlus(1, 2, 3)
	fmt.Println("1+2+3 =", res)
}

```