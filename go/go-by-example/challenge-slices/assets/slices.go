// _Slices_ are an important data type in Go, giving
// a more powerful interface to sequences than arrays.

package main

import "fmt"

func main() {
    // TODO
	// Unlike arrays, slices are typed only by the
	// elements they contain (not the number of elements).
	// To create an empty slice with non-zero length, use
	// the builtin `make`. Here we make a slice of
	// `string`s of length `3` (initially zero-valued).
	// We can set and get just like with arrays.
	// `len` returns the length of the slice as expected.
	// In addition to these basic operations, slices
	// support several more that make them richer than
	// arrays. One is the builtin `append`, which
	// returns a slice containing one or more new values.
	// Note that we need to accept a return value from
	// `append` as we may get a new slice value.
	// Slices can also be `copy`'d. Here we create an
	// empty slice `c` of the same length as `s` and copy
	// into `c` from `s`.
	// Slices support a "slice" operator with the syntax
	// `slice[low:high]`. For example, this gets a slice
	// of the elements `s[2]`, `s[3]`, and `s[4]`.
	// This slices up to (but excluding) `s[5]`.
	// And this slices up from (and including) `s[2]`.
	// We can declare and initialize a variable for slice
	// in a single line as well.
	// Slices can be composed into multi-dimensional data
	// structures. The length of the inner slices can
	// vary, unlike with multi-dimensional arrays.
}
