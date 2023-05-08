// To wait for multiple goroutines to finish, we can
// use a *wait group*.

package main

import (
	"fmt"
	"sync"
	"time"
)

// This is the function we'll run in every goroutine.
func main() {
    // TODO
	// Sleep to simulate an expensive task.
	// This WaitGroup is used to wait for all the
	// goroutines launched here to finish. Note: if a WaitGroup is
	// explicitly passed into functions, it should be done *by pointer*.
	// Launch several goroutines and increment the WaitGroup
	// counter for each.
	// Avoid re-use of the same `i` value in each goroutine closure.
	// See [the FAQ](https://golang.org/doc/faq#closures_and_goroutines)
	// for more details.
	// Wrap the worker call in a closure that makes sure to tell
	// the WaitGroup that this worker is done. This way the worker
	// itself does not have to be aware of the concurrency primitives
	// involved in its execution.
	// Block until the WaitGroup counter goes back to 0;
	// all the workers notified they're done.
	// Note that this approach has no straightforward way
	// to propagate errors from workers. For more
	// advanced use cases, consider using the
	// [errgroup package](https://pkg.go.dev/golang.org/x/sync/errgroup).
}
