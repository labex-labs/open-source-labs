// Reading and writing files are basic tasks needed for
// many Go programs. First we'll look at some examples of
// reading files.

package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
)

// Reading files requires checking most calls for errors.
// This helper will streamline our error checks below.
func main() {
    // TODO
	// Perhaps the most basic file reading task is
	// slurping a file's entire contents into memory.
	// You'll often want more control over how and what
	// parts of a file are read. For these tasks, start
	// by `Open`ing a file to obtain an `os.File` value.
	// Read some bytes from the beginning of the file.
	// Allow up to 5 to be read but also note how many
	// actually were read.
	// You can also `Seek` to a known location in the file
	// and `Read` from there.
	// The `io` package provides some functions that may
	// be helpful for file reading. For example, reads
	// like the ones above can be more robustly
	// implemented with `ReadAtLeast`.
	// There is no built-in rewind, but `Seek(0, 0)`
	// accomplishes this.
	// The `bufio` package implements a buffered
	// reader that may be useful both for its efficiency
	// with many small reads and because of the additional
	// reading methods it provides.
	// Close the file when you're done (usually this would
	// be scheduled immediately after `Open`ing with
	// `defer`).
}
