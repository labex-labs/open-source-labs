# Golang Challenge: Channel Buffering

## Problem

By default, channels in Golang are unbuffered, meaning that they only accept sends if there is a corresponding receive ready to receive the sent value. However, buffered channels accept a limited number of values without a corresponding receiver for those values. In this challenge, you are required to create a buffered channel and send values into the channel without a corresponding concurrent receive.

## Requirements

- Basic knowledge of Golang channels
- Understanding of buffered channels

## Example

```sh
$ go run channel-buffering.go
buffered
channel
```

## Solution

```go
// By default channels are _unbuffered_, meaning that they
// will only accept sends (`chan <-`) if there is a
// corresponding receive (`<- chan`) ready to receive the
// sent value. _Buffered channels_ accept a limited
// number of  values without a corresponding receiver for
// those values.

package main

import "fmt"

func main() {

	// Here we `make` a channel of strings buffering up to
	// 2 values.
	messages := make(chan string, 2)

	// Because this channel is buffered, we can send these
	// values into the channel without a corresponding
	// concurrent receive.
	messages <- "buffered"
	messages <- "channel"

	// Later we can receive these two values as usual.
	fmt.Println(<-messages)
	fmt.Println(<-messages)
}

```
