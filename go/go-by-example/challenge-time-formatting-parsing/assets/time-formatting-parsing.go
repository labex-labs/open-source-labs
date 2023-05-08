// Go supports time formatting and parsing via
// pattern-based layouts.

package main

import (
	"fmt"
	"time"
)

func main() {
    // TODO
	// Here's a basic example of formatting a time
	// according to RFC3339, using the corresponding layout
	// constant.
	// Time parsing uses the same layout values as `Format`.
	// `Format` and `Parse` use example-based layouts. Usually
	// you'll use a constant from `time` for these layouts, but
	// you can also supply custom layouts. Layouts must use the
	// reference time `Mon Jan 2 15:04:05 MST 2006` to show the
	// pattern with which to format/parse a given time/string.
	// The example time must be exactly as shown: the year 2006,
	// 15 for the hour, Monday for the day of the week, etc.
	// For purely numeric representations you can also
	// use standard string formatting with the extracted
	// components of the time value.
	// `Parse` will return an error on malformed input
	// explaining the parsing problem.
}
