// In Go it's idiomatic to communicate errors via an
// explicit, separate return value. This contrasts with
// the exceptions used in languages like Java and Ruby and
// the overloaded single result / error value sometimes
// used in C. Go's approach makes it easy to see which
// functions return errors and to handle them using the
// same language constructs employed for any other,
// non-error tasks.

package main

import (
	"errors"
	"fmt"
)

// By convention, errors are the last return value and
// have type `error`, a built-in interface.
func main() {
    // TODO
	// `errors.New` constructs a basic `error` value
	// with the given error message.
	// A `nil` value in the error position indicates that
	// there was no error.

// It's possible to use custom types as `error`s by

// implementing the `Error()` method on them. Here's a

// variant on the example above that uses a custom type

// to explicitly represent an argument error.
	// In this case we use `&argError` syntax to build
	// a new struct, supplying values for the two
	// fields `arg` and `prob`.
	// The two loops below test out each of our
	// error-returning functions. Note that the use of an
	// inline error check on the `if` line is a common
	// idiom in Go code.
	// If you want to programmatically use the data in
	// a custom error, you'll need to get the error as an
	// instance of the custom error type via type
	// assertion.
}
