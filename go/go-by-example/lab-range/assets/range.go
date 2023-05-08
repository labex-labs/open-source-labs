// _range_ iterates over elements in a variety of data
// structures. Let's see how to use `range` with some
// of the data structures we've already learned.

package main

import "fmt"

func main() {
    // TODO
	// Here we use `range` to sum the numbers in a slice.
	// Arrays work like this too.
	// `range` on arrays and slices provides both the
	// index and value for each entry. Above we didn't
	// need the index, so we ignored it with the
	// blank identifier `_`. Sometimes we actually want
	// the indexes though.
	// `range` on map iterates over key/value pairs.
	// `range` can also iterate over just the keys of a map.
	// `range` on strings iterates over Unicode code
	// points. The first value is the starting byte index
	// of the `rune` and the second the `rune` itself.
	// See [Strings and Runes](strings-and-runes) for more
	// details.
}
