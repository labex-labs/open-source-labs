// When using channels as function parameters, you can
// specify if a channel is meant to only send or receive
// values. This specificity increases the type-safety of
// the program.

package main

import "fmt"

// This `ping` function only accepts a channel for sending
// values. It would be a compile-time error to try to
// receive on this channel.
func main() {
    // TODO

// The `pong` function accepts one channel for receives

// (`pings`) and a second for sends (`pongs`).
}
