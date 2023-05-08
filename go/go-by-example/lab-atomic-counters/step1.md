# Atomic Counters

## Problem

The problem is to increment a counter exactly 1000 times using 50 goroutines and the `sync/atomic` package.

## Requirements

- Use the `sync/atomic` package to increment the counter.
- Use a WaitGroup to wait for all goroutines to finish their work.

## Example

```sh
# We expect to get exactly 50,000 operations. Had we
# used the non-atomic `ops++` to increment the counter,
# we'd likely get a different number, changing between
# runs, because the goroutines would interfere with
# each other. Moreover, we'd get data race failures
# when running with the `-race` flag.
$ go run atomic-counters.go
ops: 50000

# Next we'll look at mutexes, another tool for managing
# state.

```

## Solution

```go
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

	// We'll use an unsigned integer to represent our
	// (always-positive) counter.
	var ops uint64

	// A WaitGroup will help us wait for all goroutines
	// to finish their work.
	var wg sync.WaitGroup

	// We'll start 50 goroutines that each increment the
	// counter exactly 1000 times.
	for i := 0; i < 50; i++ {
		wg.Add(1)

		go func() {
			for c := 0; c < 1000; c++ {
				// To atomically increment the counter we
				// use `AddUint64`, giving it the memory
				// address of our `ops` counter with the
				// `&` syntax.
				atomic.AddUint64(&ops, 1)
			}
			wg.Done()
		}()
	}

	// Wait until all the goroutines are done.
	wg.Wait()

	// It's safe to access `ops` now because we know
	// no other goroutine is writing to it. Reading
	// atomics safely while they are being updated is
	// also possible, using functions like
	// `atomic.LoadUint64`.
	fmt.Println("ops:", ops)
}

```