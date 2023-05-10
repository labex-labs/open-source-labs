// Go's `math/rand` package provides
// [pseudorandom number](https://en.wikipedia.org/wiki/Pseudorandom_number_generator)
// generation.

package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
    // TODO
	// For example, `rand.Intn` returns a random `int` n,
	// `0 <= n < 100`.
	// `rand.Float64` returns a `float64` `f`,
	// `0.0 <= f < 1.0`.
	// This can be used to generate random floats in
	// other ranges, for example `5.0 <= f' < 10.0`.
	// The default number generator is deterministic, so it'll
	// produce the same sequence of numbers each time by default.
	// To produce varying sequences, give it a seed that changes.
	// Note that this is not safe to use for random numbers you
	// intend to be secret; use `crypto/rand` for those.
	// Call the resulting `rand.Rand` just like the
	// functions on the `rand` package.
	// If you seed a source with the same number, it
	// produces the same sequence of random numbers.
}
