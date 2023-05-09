// The primary mechanism for managing state in Go is
// communication over channels. We saw this for example
// with [worker pools](worker-pools). There are a few other
// options for managing state though. Here we'll
// look at using the `sync/atomic` package for _atomic
// counters_ accessed by multiple goroutines.

package main

import (
	"fmt"
	"sync"
	"sync/atomic"
)

func main() {
    // TODO
	// We'll use an unsigned integer to represent our
	// (always-positive) counter.
	// A WaitGroup will help us wait for all goroutines
	// to finish their work.
	// We'll start 50 goroutines that each increment the
	// counter exactly 1000 times.
	// To atomically increment the counter we
	// use `AddUint64`, giving it the memory
	// address of our `ops` counter with the
	// `&` syntax.
	// Wait until all the goroutines are done.
	// It's safe to access `ops` now because we know
	// no other goroutine is writing to it. Reading
	// atomics safely while they are being updated is
	// also possible, using functions like
	// `atomic.LoadUint64`.
}
