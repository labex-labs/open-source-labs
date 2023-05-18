// Starting with version 1.18, Go has added support for
// _generics_, also known as _type parameters_.

package main

import "fmt"

// As an example of a generic function, `MapKeys` takes
// a map of any type and returns a slice of its keys.
// This function has two type parameters - `K` and `V`;
// `K` has the `comparable` _constraint_, meaning that
// we can compare values of this type with the `==` and
// `!=` operators. This is required for map keys in Go.
// `V` has the `any` constraint, meaning that it's not
// restricted in any way (`any` is an alias for `interface{}`).
func main() {
    // TODO

// As an example of a generic type, `List` is a

// singly-linked list with values of any type.

// We can define methods on generic types just like we

// do on regular types, but we have to keep the type

// parameters in place. The type is `List[T]`, not `List`.
	// When invoking generic functions, we can often rely
	// on _type inference_. Note that we don't have to
	// specify the types for `K` and `V` when
	// calling `MapKeys` - the compiler infers them
	// automatically.
	// ... though we could also specify them explicitly.
}
