// Use `os.Exit` to immediately exit with a given
// status.

package main

import (
	"fmt"
	"os"
)

func main() {
    // TODO
	// `defer`s will _not_ be run when using `os.Exit`, so
	// this `fmt.Println` will never be called.
	// Exit with status 3.
}

// Note that unlike e.g. C, Go does not use an integer
// return value from `main` to indicate exit status. If
// you'd like to exit with a non-zero status you should
// use `os.Exit`.
