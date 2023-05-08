// Go supports <em><a href="https://en.wikipedia.org/wiki/Pointer_(computer_programming)">pointers</a></em>,
// allowing you to pass references to values and records
// within your program.

package main

import "fmt"

// We'll show how pointers work in contrast to values with
// 2 functions: `zeroval` and `zeroptr`. `zeroval` has an
// `int` parameter, so arguments will be passed to it by
// value. `zeroval` will get a copy of `ival` distinct
// from the one in the calling function.
func main() {
    // TODO

// `zeroptr` in contrast has an `*int` parameter, meaning

// that it takes an `int` pointer. The `*iptr` code in the

// function body then _dereferences_ the pointer from its

// memory address to the current value at that address.

// Assigning a value to a dereferenced pointer changes the

// value at the referenced address.
	// The `&i` syntax gives the memory address of `i`,
	// i.e. a pointer to `i`.
	// Pointers can be printed too.
}
