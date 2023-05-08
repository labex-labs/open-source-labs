// The `filepath` package provides functions to parse
// and construct *file paths* in a way that is portable
// between operating systems; `dir/file` on Linux vs.
// `dir\file` on Windows, for example.
package main

import (
	"fmt"
	"path/filepath"
	"strings"
)

func main() {
    // TODO
	// `Join` should be used to construct paths in a
	// portable way. It takes any number of arguments
	// and constructs a hierarchical path from them.
	// You should always use `Join` instead of
	// concatenating `/`s or `\`s manually. In addition
	// to providing portability, `Join` will also
	// normalize paths by removing superfluous separators
	// and directory changes.
	// `Dir` and `Base` can be used to split a path to the
	// directory and the file. Alternatively, `Split` will
	// return both in the same call.
	// We can check whether a path is absolute.
	// Some file names have extensions following a dot. We
	// can split the extension out of such names with `Ext`.
	// To find the file's name with the extension removed,
	// use `strings.TrimSuffix`.
	// `Rel` finds a relative path between a *base* and a
	// *target*. It returns an error if the target cannot
	// be made relative to base.
}
