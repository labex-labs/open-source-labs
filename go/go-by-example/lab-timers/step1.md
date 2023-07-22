# Timers

The lab requires the implementation of a timer that waits for a specified duration and then fires. Additionally, the timer should be cancellable before it fires.

- The `time` package should be imported.
- Two timers should be created, one that waits for 2 seconds and another that waits for 1 second.
- The first timer should print "Timer 1 fired" when it fires.
- The second timer should print "Timer 2 fired" when it fires.
- The second timer should be cancelled before it fires.
- The program should wait for 2 seconds to show that the second timer did not fire.

```sh
// The first timer will fire ~2s after we start the
// program, but the second should be stopped before it has
// a chance to fire.
$ go run timers.go
Timer 1 fired
Timer 2 stopped
```

There is the full code below:

```go
// We often want to execute Go code at some point in the
// future, or repeatedly at some interval. Go's built-in
// _timer_ and _ticker_ features make both of these tasks
// easy. We'll look first at timers and then
// at [tickers](tickers).

package main

import (
	"fmt"
	"time"
)

func main() {

	// Timers represent a single event in the future. You
	// tell the timer how long you want to wait, and it
	// provides a channel that will be notified at that
	// time. This timer will wait 2 seconds.
	timer1 := time.NewTimer(2 * time.Second)

	// The `<-timer1.C` blocks on the timer's channel `C`
	// until it sends a value indicating that the timer
	// fired.
	<-timer1.C
	fmt.Println("Timer 1 fired")

	// If you just wanted to wait, you could have used
	// `time.Sleep`. One reason a timer may be useful is
	// that you can cancel the timer before it fires.
	// Here's an example of that.
	timer2 := time.NewTimer(time.Second)
	go func() {
		<-timer2.C
		fmt.Println("Timer 2 fired")
	}()
	stop2 := timer2.Stop()
	if stop2 {
		fmt.Println("Timer 2 stopped")
	}

	// Give the `timer2` enough time to fire, if it ever
	// was going to, to show it is in fact stopped.
	time.Sleep(2 * time.Second)
}

```
