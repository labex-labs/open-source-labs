// Go's _structs_ are typed collections of fields.
// They're useful for grouping data together to form
// records.

package main

import "fmt"

// This `person` struct type has `name` and `age` fields.
type person struct {
	name string
	age  int
}

// `newPerson` constructs a new person struct with the given name.
func main() {
    // TODO
	// You can safely return a pointer to local variable
	// as a local variable will survive the scope of the function.
	// This syntax creates a new struct.
	// You can name the fields when initializing a struct.
	// Omitted fields will be zero-valued.
	// An `&` prefix yields a pointer to the struct.
	// It's idiomatic to encapsulate new struct creation in constructor functions
	// Access struct fields with a dot.
	// You can also use dots with struct pointers - the
	// pointers are automatically dereferenced.
	// Structs are mutable.
}
