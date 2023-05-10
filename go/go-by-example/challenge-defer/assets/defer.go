// _Defer_ is used to ensure that a function call is
// performed later in a program's execution, usually for
// purposes of cleanup. `defer` is often used where e.g.
// `ensure` and `finally` would be used in other languages.

package main

import (
	"fmt"
	"os"
)

// Suppose we wanted to create a file, write to it,
// and then close when we're done. Here's how we could
// do that with `defer`.
func main() {
    // TODO
	// Immediately after getting a file object with
	// `createFile`, we defer the closing of that file
	// with `closeFile`. This will be executed at the end
	// of the enclosing function (`main`), after
	// `writeFile` has finished.
	// It's important to check for errors when closing a
	// file, even in a deferred function.
}
