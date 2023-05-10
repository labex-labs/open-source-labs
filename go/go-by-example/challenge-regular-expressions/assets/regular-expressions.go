// Go offers built-in support for [regular expressions](https://en.wikipedia.org/wiki/Regular_expression).
// Here are some examples of  common regexp-related tasks
// in Go.

package main

import (
	"bytes"
	"fmt"
	"regexp"
)

func main() {
    // TODO
	// This tests whether a pattern matches a string.
	// Above we used a string pattern directly, but for
	// other regexp tasks you'll need to `Compile` an
	// optimized `Regexp` struct.
	// Many methods are available on these structs. Here's
	// a match test like we saw earlier.
	// This finds the match for the regexp.
	// This also finds the first match but returns the
	// start and end indexes for the match instead of the
	// matching text.
	// The `Submatch` variants include information about
	// both the whole-pattern matches and the submatches
	// within those matches. For example this will return
	// information for both `p([a-z]+)ch` and `([a-z]+)`.
	// Similarly this will return information about the
	// indexes of matches and submatches.
	// The `All` variants of these functions apply to all
	// matches in the input, not just the first. For
	// example to find all matches for a regexp.
	// These `All` variants are available for the other
	// functions we saw above as well.
	// Providing a non-negative integer as the second
	// argument to these functions will limit the number
	// of matches.
	// Our examples above had string arguments and used
	// names like `MatchString`. We can also provide
	// `[]byte` arguments and drop `String` from the
	// function name.
	// When creating global variables with regular
	// expressions you can use the `MustCompile` variation
	// of `Compile`. `MustCompile` panics instead of
	// returning an error, which makes it safer to use for
	// global variables.
	// The `regexp` package can also be used to replace
	// subsets of strings with other values.
	// The `Func` variant allows you to transform matched
	// text with a given function.
}
