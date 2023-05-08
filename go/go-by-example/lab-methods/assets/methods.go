// Go supports _methods_ defined on struct types.

package main

import "fmt"

type rect struct {
	width, height int
}

// This `area` method has a _receiver type_ of `*rect`.
func main() {
    // TODO

// Methods can be defined for either pointer or value

// receiver types. Here's an example of a value receiver.
	// Here we call the 2 methods defined for our struct.
	// Go automatically handles conversion between values
	// and pointers for method calls. You may want to use
	// a pointer receiver type to avoid copying on method
	// calls or to allow the method to mutate the
	// receiving struct.
}
