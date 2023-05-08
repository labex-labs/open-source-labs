# Golang Challenge: Constants

## Introduction
This challenge aims to test your understanding of constants in Golang.

## Problem
The code below declares a constant value and performs arithmetic operations with it. Your task is to complete the TODO sections to make the code work as expected.

```go
package main

import (
	"fmt"
	"math"
)

// `const` declares a constant value.
const s string = "constant"

func main() {
	fmt.Println(s)

	// TODO: Declare a constant named n with a value of 500000000

	// Constant expressions perform arithmetic with
	// arbitrary precision.
	// TODO: Declare a constant named d that is equal to 3e20 divided by n

	fmt.Println(d)

	// A numeric constant has no type until it's given
	// one, such as by an explicit conversion.
	// TODO: Convert d to an int64 and print it

	// A number can be given a type by using it in a
	// context that requires one, such as a variable
	// assignment or function call. For example, here
	// `math.Sin` expects a `float64`.
	// TODO: Call the math.Sin function with n as its argument and print the result
}
```

## Requirements
- Declare a constant named `n` with a value of `500000000`
- Declare a constant named `d` that is equal to `3e20` divided by `n`
- Convert `d` to an `int64` and print it
- Call the `math.Sin` function with `n` as its argument and print the result

## TODO
```go
// TODO: Declare a constant named n with a value of 500000000

// TODO: Declare a constant named d that is equal to 3e20 divided by n

// TODO: Convert d to an int64 and print it

// TODO: Call the math.Sin function with n as its argument and print the result
```

## Example
```
constant
6e+11
600000000000
-0.28470407323754404
```

## Summary
In this challenge, you learned how to declare and use constants in Golang. Constants can be of character, string, boolean, and numeric values. Constant expressions perform arithmetic with arbitrary precision. A numeric constant has no type until it's given one, such as by an explicit conversion.