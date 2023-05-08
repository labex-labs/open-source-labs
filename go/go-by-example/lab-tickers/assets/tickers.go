// [Timers](timers) are for when you want to do
// something once in the future - _tickers_ are for when
// you want to do something repeatedly at regular
// intervals. Here's an example of a ticker that ticks
// periodically until we stop it.

package main

import (
	"fmt"
	"time"
)

func main() {
    // TODO
	// Tickers use a similar mechanism to timers: a
	// channel that is sent values. Here we'll use the
	// `select` builtin on the channel to await the
	// values as they arrive every 500ms.
	// Tickers can be stopped like timers. Once a ticker
	// is stopped it won't receive any more values on its
	// channel. We'll stop ours after 1600ms.
}
