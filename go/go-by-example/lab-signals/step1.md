# Signals

## Problem

In some cases, we want our Go programs to handle Unix signals intelligently. For instance, we might want a server to shut down gracefully when it receives a `SIGTERM`, or a command-line tool to stop processing input if it receives a `SIGINT`.

## Requirements

- Create a buffered channel to receive `os.Signal` notifications.
- Register the channel to receive notifications of specified signals using `signal.Notify`.
- Create a goroutine to execute a blocking receive for signals.
- Print out the received signal and notify the program that it can finish.
- Wait for the expected signal and then exit.

## Example

```sh
# When we run this program it will block waiting for a
# signal. By typing `ctrl-C` (which the
# terminal shows as `^C`) we can send a `SIGINT` signal,
# causing the program to print `interrupt` and then exit.
$ go run signals.go
awaiting signal
^C
interrupt
exiting
```

## Solution

```go
// Sometimes we'd like our Go programs to intelligently
// handle [Unix signals](https://en.wikipedia.org/wiki/Unix_signal).
// For example, we might want a server to gracefully
// shutdown when it receives a `SIGTERM`, or a command-line
// tool to stop processing input if it receives a `SIGINT`.
// Here's how to handle signals in Go with channels.

package main

import (
	"fmt"
	"os"
	"os/signal"
	"syscall"
)

func main() {

	// Go signal notification works by sending `os.Signal`
	// values on a channel. We'll create a channel to
	// receive these notifications. Note that this channel
	// should be buffered.
	sigs := make(chan os.Signal, 1)

	// `signal.Notify` registers the given channel to
	// receive notifications of the specified signals.
	signal.Notify(sigs, syscall.SIGINT, syscall.SIGTERM)

	// We could receive from `sigs` here in the main
	// function, but let's see how this could also be
	// done in a separate goroutine, to demonstrate
	// a more realistic scenario of graceful shutdown.
	done := make(chan bool, 1)

	go func() {
		// This goroutine executes a blocking receive for
		// signals. When it gets one it'll print it out
		// and then notify the program that it can finish.
		sig := <-sigs
		fmt.Println()
		fmt.Println(sig)
		done <- true
	}()

	// The program will wait here until it gets the
	// expected signal (as indicated by the goroutine
	// above sending a value on `done`) and then exit.
	fmt.Println("awaiting signal")
	<-done
	fmt.Println("exiting")
}

```
