# Constants

## Problem

The problem to be solved is to demonstrate the use of constants in Golang for character, string, boolean, and numeric values.

## Requirements

The Challenge has the following requirements:

- Use the `const` keyword to declare a constant value.
- Constants should be of character, string, boolean, and numeric values.
- A constant statement can appear anywhere a `var` statement can.
- Demonstrate that constant expressions perform arithmetic with arbitrary precision.
- A numeric constant has no type until it's given one, such as by an explicit conversion.
- A number can be given a type by using it in a context that requires one, such as a variable assignment or function call.

## Example

```sh
$ go run constant.go 
constant
6e+11
600000000000
-0.28470407323754404

```

## Solution

```go
// Go supports _constants_ of character, string, boolean,
// and numeric values.

package main

import (
	"fmt"
	"math"
)

// `const` declares a constant value.
const s string = "constant"

func main() {
	fmt.Println(s)

	// A `const` statement can appear anywhere a `var`
	// statement can.
	const n = 500000000

	// Constant expressions perform arithmetic with
	// arbitrary precision.
	const d = 3e20 / n
	fmt.Println(d)

	// A numeric constant has no type until it's given
	// one, such as by an explicit conversion.
	fmt.Println(int64(d))

	// A number can be given a type by using it in a
	// context that requires one, such as a variable
	// assignment or function call. For example, here
	// `math.Sin` expects a `float64`.
	fmt.Println(math.Sin(n))
}

```