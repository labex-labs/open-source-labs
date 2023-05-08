# Recursion

## Problem

The `sum` function takes an integer slice and returns the sum of all the integers in the slice. However, the function is incomplete and needs to be implemented using recursion.

## Requirements

- The `sum` function must be implemented using recursion.
- The function must take an integer slice as input.
- The function must return the sum of all the integers in the slice.

## Example

```sh
$ go run recursion.go 
5040
13

```

## Solution

```go
// Go supports
// <a href="https://en.wikipedia.org/wiki/Recursion_(computer_science)"><em>recursive functions</em></a>.
// Here's a classic example.

package main

import "fmt"

// This `fact` function calls itself until it reaches the
// base case of `fact(0)`.
func fact(n int) int {
	if n == 0 {
		return 1
	}
	return n * fact(n-1)
}

func main() {
	fmt.Println(fact(7))

	// Closures can also be recursive, but this requires the
	// closure to be declared with a typed `var` explicitly
	// before it's defined.
	var fib func(n int) int

	fib = func(n int) int {
		if n < 2 {
			return n
		}

		// Since `fib` was previously declared in `main`, Go
		// knows which function to call with `fib` here.
		return fib(n-1) + fib(n-2)
	}

	fmt.Println(fib(7))
}

```