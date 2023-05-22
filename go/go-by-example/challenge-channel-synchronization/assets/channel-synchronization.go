// We can use channels to synchronize execution
// across goroutines. Here's an example of using a
// blocking receive to wait for a goroutine to finish.
// When waiting for multiple goroutines to finish,
// you may prefer to use a [WaitGroup](waitgroups).

package main

import (
	"fmt"
	"time"
)

// This is the function we'll run in a goroutine. The
// `done` channel will be used to notify another
// goroutine that this function's work is done.
func main() {
    // TODO
	// Send a value to notify that we're done.
	// Start a worker goroutine, giving it the channel to
	// notify on.
	// Block until we receive a notification from the
	// worker on the channel.
}
