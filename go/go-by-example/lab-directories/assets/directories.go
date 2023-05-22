// Go has several useful functions for working with
// *directories* in the file system.

package main

import (
	"fmt"
	"os"
	"path/filepath"
)

func main() {
    // TODO
	// Create a new sub-directory in the current working
	// directory.
	// When creating temporary directories, it's good
	// practice to `defer` their removal. `os.RemoveAll`
	// will delete a whole directory tree (similarly to
	// `rm -rf`).
	// Helper function to create a new empty file.
	// We can create a hierarchy of directories, including
	// parents with `MkdirAll`. This is similar to the
	// command-line `mkdir -p`.
	// `ReadDir` lists directory contents, returning a
	// slice of `os.DirEntry` objects.
	// `Chdir` lets us change the current working directory,
	// similarly to `cd`.
	// Now we'll see the contents of `subdir/parent/child`
	// when listing the *current* directory.
	// `cd` back to where we started.
	// We can also visit a directory *recursively*,
	// including all its sub-directories. `Walk` accepts
	// a callback function to handle every file or
	// directory visited.

// `visit` is called for every file or directory found

// recursively by `filepath.Walk`.
}
