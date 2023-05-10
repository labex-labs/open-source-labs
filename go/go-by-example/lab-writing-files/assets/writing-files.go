// Writing files in Go follows similar patterns to the
// ones we saw earlier for reading.

package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
    // TODO
	// To start, here's how to dump a string (or just
	// bytes) into a file.
	// For more granular writes, open a file for writing.
	// It's idiomatic to defer a `Close` immediately
	// after opening a file.
	// You can `Write` byte slices as you'd expect.
	// A `WriteString` is also available.
	// Issue a `Sync` to flush writes to stable storage.
	// `bufio` provides buffered writers in addition
	// to the buffered readers we saw earlier.
	// Use `Flush` to ensure all buffered operations have
	// been applied to the underlying writer.
}
