// In the previous example we looked at setting up a simple
// [HTTP server](http-servers). HTTP servers are useful for
// demonstrating the usage of `context.Context` for
// controlling cancellation. A `Context` carries deadlines,
// cancellation signals, and other request-scoped values
// across API boundaries and goroutines.
package main

import (
	"fmt"
	"net/http"
	"time"
)

func main() {
    // TODO
	// A `context.Context` is created for each request by
	// the `net/http` machinery, and is available with
	// the `Context()` method.
	// Wait for a few seconds before sending a reply to the
	// client. This could simulate some work the server is
	// doing. While working, keep an eye on the context's
	// `Done()` channel for a signal that we should cancel
	// the work and return as soon as possible.
	// The context's `Err()` method returns an error
	// that explains why the `Done()` channel was
	// closed.
	// As before, we register our handler on the "/hello"
	// route, and start serving.
}
