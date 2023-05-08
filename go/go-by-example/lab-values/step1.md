# Golang Value Types Challenge

## Problem

Your task is to complete the `calculate` function that takes in two integers and returns their sum and product.

## Requirements

- The `calculate` function should take in two integers as parameters.
- The `calculate` function should return two integers, the sum and product of the input parameters.

## Example

```sh
$ go run values.go
golang
1+1 = 2
7.0/3.0 = 2.3333333333333335
false
true
false
```

## Solution

```go
// Go has various value types including strings,
// integers, floats, booleans, etc. Here are a few
// basic examples.

package main

import "fmt"

func main() {

	// Strings, which can be added together with `+`.
	fmt.Println("go" + "lang")

	// Integers and floats.
	fmt.Println("1+1 =", 1+1)
	fmt.Println("7.0/3.0 =", 7.0/3.0)

	// Booleans, with boolean operators as you'd expect.
	fmt.Println(true && false)
	fmt.Println(true || false)
	fmt.Println(!true)
}

```
