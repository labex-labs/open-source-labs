
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
