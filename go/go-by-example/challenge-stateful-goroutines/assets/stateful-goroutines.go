// In the previous example we used explicit locking with
// [mutexes](mutexes) to synchronize access to shared state
// across multiple goroutines. Another option is to use the
// built-in synchronization features of  goroutines and
// channels to achieve the same result. This channel-based
// approach aligns with Go's ideas of sharing memory by
// communicating and having each piece of data owned
// by exactly 1 goroutine.

package main

import (
	"fmt"
	"math/rand"
	"sync/atomic"
	"time"
)

// In this example our state will be owned by a single
// goroutine. This will guarantee that the data is never
// corrupted with concurrent access. In order to read or
// write that state, other goroutines will send messages
// to the owning goroutine and receive corresponding
// replies. These `readOp` and `writeOp` `struct`s
// encapsulate those requests and a way for the owning
// goroutine to respond.
type readOp struct {
	key  int
	resp chan int
}
type writeOp struct {
	key  int
	val  int
	resp chan bool
}

func main() {
    // TODO
	// As before we'll count how many operations we perform.
	// The `reads` and `writes` channels will be used by
	// other goroutines to issue read and write requests,
	// respectively.
	// Here is the goroutine that owns the `state`, which
	// is a map as in the previous example but now private
	// to the stateful goroutine. This goroutine repeatedly
	// selects on the `reads` and `writes` channels,
	// responding to requests as they arrive. A response
	// is executed by first performing the requested
	// operation and then sending a value on the response
	// channel `resp` to indicate success (and the desired
	// value in the case of `reads`).
	// This starts 100 goroutines to issue reads to the
	// state-owning goroutine via the `reads` channel.
	// Each read requires constructing a `readOp`, sending
	// it over the `reads` channel, and then receiving the
	// result over the provided `resp` channel.
	// We start 10 writes as well, using a similar
	// approach.
	// Let the goroutines work for a second.
	// Finally, capture and report the op counts.
}
