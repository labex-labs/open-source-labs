// Go offers excellent support for string formatting in
// the `printf` tradition. Here are some examples of
// common string formatting tasks.

package main

import (
	"fmt"
	"os"
)

type point struct {
	x, y int
}

func main() {
    // TODO
	// Go offers several printing "verbs" designed to
	// format general Go values. For example, this prints
	// an instance of our `point` struct.
	// If the value is a struct, the `%+v` variant will
	// include the struct's field names.
	// The `%#v` variant prints a Go syntax representation
	// of the value, i.e. the source code snippet that
	// would produce that value.
	// To print the type of a value, use `%T`.
	// Formatting booleans is straight-forward.
	// There are many options for formatting integers.
	// Use `%d` for standard, base-10 formatting.
	// This prints a binary representation.
	// This prints the character corresponding to the
	// given integer.
	// `%x` provides hex encoding.
	// There are also several formatting options for
	// floats. For basic decimal formatting use `%f`.
	// `%e` and `%E` format the float in (slightly
	// different versions of) scientific notation.
	// For basic string printing use `%s`.
	// To double-quote strings as in Go source, use `%q`.
	// As with integers seen earlier, `%x` renders
	// the string in base-16, with two output characters
	// per byte of input.
	// To print a representation of a pointer, use `%p`.
	// When formatting numbers you will often want to
	// control the width and precision of the resulting
	// figure. To specify the width of an integer, use a
	// number after the `%` in the verb. By default the
	// result will be right-justified and padded with
	// spaces.
	// You can also specify the width of printed floats,
	// though usually you'll also want to restrict the
	// decimal precision at the same time with the
	// width.precision syntax.
	// To left-justify, use the `-` flag.
	// You may also want to control width when formatting
	// strings, especially to ensure that they align in
	// table-like output. For basic right-justified width.
	// To left-justify use the `-` flag as with numbers.
	// So far we've seen `Printf`, which prints the
	// formatted string to `os.Stdout`. `Sprintf` formats
	// and returns a string without printing it anywhere.
	// You can format+print to `io.Writers` other than
	// `os.Stdout` using `Fprintf`.
}
