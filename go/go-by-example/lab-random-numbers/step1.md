# Random Numbers

## Problem

You are required to write a program that generates random integers and floats within a specified range. The program should also be able to produce varying sequences of numbers by changing the seed.

## Requirements

- The program should use the `math/rand` package to generate random numbers.
- The program should generate random integers within a specified range.
- The program should generate random floats within a specified range.
- The program should be able to produce varying sequences of numbers by changing the seed.

## Example

```sh
# Depending on where you run this sample, some of the
# generated numbers may be different. Note that on
# the Go playground seeding with `time.Now()` still
# produces deterministic results due to the way the
# playground is implemented.
$ go run random-numbers.go
81,87
0.6645600532184904
7.123187485356329,8.434115364335547
0,28
5,87
5,87


# See the [`math/rand`](https://pkg.go.dev/math/rand)
# package docs for references on other random quantities
# that Go can provide.

```

## Solution

```go
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

	// For example, `rand.Intn` returns a random `int` n,
	// `0 <= n < 100`.
	fmt.Print(rand.Intn(100), ",")
	fmt.Print(rand.Intn(100))
	fmt.Println()

	// `rand.Float64` returns a `float64` `f`,
	// `0.0 <= f < 1.0`.
	fmt.Println(rand.Float64())

	// This can be used to generate random floats in
	// other ranges, for example `5.0 <= f' < 10.0`.
	fmt.Print((rand.Float64()*5)+5, ",")
	fmt.Print((rand.Float64() * 5) + 5)
	fmt.Println()

	// The default number generator is deterministic, so it'll
	// produce the same sequence of numbers each time by default.
	// To produce varying sequences, give it a seed that changes.
	// Note that this is not safe to use for random numbers you
	// intend to be secret; use `crypto/rand` for those.
	s1 := rand.NewSource(time.Now().UnixNano())
	r1 := rand.New(s1)

	// Call the resulting `rand.Rand` just like the
	// functions on the `rand` package.
	fmt.Print(r1.Intn(100), ",")
	fmt.Print(r1.Intn(100))
	fmt.Println()

	// If you seed a source with the same number, it
	// produces the same sequence of random numbers.
	s2 := rand.NewSource(42)
	r2 := rand.New(s2)
	fmt.Print(r2.Intn(100), ",")
	fmt.Print(r2.Intn(100))
	fmt.Println()
	s3 := rand.NewSource(42)
	r3 := rand.New(s3)
	fmt.Print(r3.Intn(100), ",")
	fmt.Print(r3.Intn(100))
}

```