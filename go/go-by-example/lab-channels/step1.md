# Channels

In this lab, you are required to create a new channel and send a value into it from a new goroutine. You will then receive the value from the channel and print it out.

- You must use the `make(chan val-type)` syntax to create a new channel.
- The channel must be typed by the values it conveys.
- You must use the `channel <-` syntax to send a value into the channel.
- You must use the `<-channel` syntax to receive a value from the channel.
- You must use a new goroutine to send the value into the channel.

```sh
# When we run the program the `"ping"` message is
# successfully passed from one goroutine to another via
# our channel.
$ go run channels.go
ping

# By default sends and receives block until both the
# sender and receiver are ready. This property allowed
# us to wait at the end of our program for the `"ping"`
# message without having to use any other synchronization.
```

There is the full code below:

```go
// _Channels_ are the pipes that connect concurrent
// goroutines. You can send values into channels from one
// goroutine and receive those values into another
// goroutine.

package main

import "fmt"

func main() {

	// Create a new channel with `make(chan val-type)`.
	// Channels are typed by the values they convey.
	messages := make(chan string)

	// _Send_ a value into a channel using the `channel <-`
	// syntax. Here we send `"ping"`  to the `messages`
	// channel we made above, from a new goroutine.
	go func() { messages <- "ping" }()

	// The `<-channel` syntax _receives_ a value from the
	// channel. Here we'll receive the `"ping"` message
	// we sent above and print it out.
	msg := <-messages
	fmt.Println(msg)
}

```
