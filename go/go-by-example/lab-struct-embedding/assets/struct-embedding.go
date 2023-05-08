// Go supports _embedding_ of structs and interfaces
// to express a more seamless _composition_ of types.
// This is not to be confused with [`//go:embed`](embed-directive) which is
// a go directive introduced in Go version 1.16+ to embed
// files and folders into the application binary.

package main

import "fmt"

type base struct {
	num int
}

func main() {
    // TODO

// A `container` _embeds_ a `base`. An embedding looks

// like a field without a name.
	// When creating structs with literals, we have to
	// initialize the embedding explicitly; here the
	// embedded type serves as the field name.
	// We can access the base's fields directly on `co`,
	// e.g. `co.num`.
	// Alternatively, we can spell out the full path using
	// the embedded type name.
	// Since `container` embeds `base`, the methods of
	// `base` also become methods of a `container`. Here
	// we invoke a method that was embedded from `base`
	// directly on `co`.
	// Embedding structs with methods may be used to bestow
	// interface implementations onto other structs. Here
	// we see that a `container` now implements the
	// `describer` interface because it embeds `base`.
}
