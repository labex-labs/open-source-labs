# Variadic Functions

## Problem

In this challenge, you need to implement a function named `max` that takes an arbitrary number of integers as arguments and returns the maximum value. 

## Requirements

- The function `max` should take an arbitrary number of integers as arguments.
- The function `max` should return the maximum value of the integers passed as arguments.

## Example

```sh
$ go run variadic-functions.go 
[1 2] 3
[1 2 3] 6
[1 2 3 4] 10

# Another key aspect of functions in Go is their ability
# to form closures, which we'll look at next.

```

## Solution

```go
// [_Variadic functions_](https://en.wikipedia.org/wiki/Variadic_function)
// can be called with any number of trailing arguments.
// For example, `fmt.Println` is a common variadic
// function.

package main

import "fmt"

// Here's a function that will take an arbitrary number
// of `int`s as arguments.
func sum(nums ...int) {
	fmt.Print(nums, " ")
	total := 0
	// Within the function, the type of `nums` is
	// equivalent to `[]int`. We can call `len(nums)`,
	// iterate over it with `range`, etc.
	for _, num := range nums {
		total += num
	}
	fmt.Println(total)
}

func main() {

	// Variadic functions can be called in the usual way
	// with individual arguments.
	sum(1, 2)
	sum(1, 2, 3)

	// If you already have multiple args in a slice,
	// apply them to a variadic function using
	// `func(slice...)` like this.
	nums := []int{1, 2, 3, 4}
	sum(nums...)
}

```