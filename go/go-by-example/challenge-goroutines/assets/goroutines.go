// A _goroutine_ is a lightweight thread of execution.

package main

import (
	"fmt"
	"time"
)

func main() {
    // TODO
	// Suppose we have a function call `f(s)`. Here's how
	// we'd call that in the usual way, running it
	// synchronously.
	// To invoke this function in a goroutine, use
	// `go f(s)`. This new goroutine will execute
	// concurrently with the calling one.
	// You can also start a goroutine for an anonymous
	// function call.
	// Our two function calls are running asynchronously in
	// separate goroutines now. Wait for them to finish
	// (for a more robust approach, use a [WaitGroup](waitgroups)).
}
