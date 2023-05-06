# Golang Challenge: Channel Synchronization

## Problem

The problem to be solved in this challenge is to create a goroutine that performs some work and notifies another goroutine when it's done using a channel.

## Requirements

To complete this challenge, you will need to:
- Create a function named `worker` that takes a channel of type `bool` as a parameter.
- Inside the `worker` function, perform some work and then send a value to the channel to notify that the work is done.
- In the `main` function, create a channel of type `bool` with a buffer size of 1.
- Start a goroutine that calls the `worker` function and passes the channel as a parameter.
- Block the `main` function until a value is received from the channel.

## Example

```sh
$ go run channel-synchronization.go      
working...done                  

# If you removed the `<- done` line from this program, the
# program would exit before the `worker` even
# started.

```

## Solution

```go
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
func worker(done chan bool) {
	fmt.Print("working...")
	time.Sleep(time.Second)
	fmt.Println("done")

	// Send a value to notify that we're done.
	done <- true
}

func main() {

	// Start a worker goroutine, giving it the channel to
	// notify on.
	done := make(chan bool, 1)
	go worker(done)

	// Block until we receive a notification from the
	// worker on the channel.
	<-done
}

```