// Go supports
// <a href="https://en.wikipedia.org/wiki/Recursion_(computer_science)"><em>recursive functions</em></a>.
// Here's a classic example.

package main

import "fmt"

// This `fact` function calls itself until it reaches the
// base case of `fact(0)`.
func main() {
    // TODO
	// Closures can also be recursive, but this requires the
	// closure to be declared with a typed `var` explicitly
	// before it's defined.
	// Since `fib` was previously declared in `main`, Go
	// knows which function to call with `fib` here.
}
