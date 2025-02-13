# Channels

In this challenge, you are required to create a new channel and send a value into it from a new goroutine. You will then receive the value from the channel and print it out.

## Requirements

- You must use the `make(chan val-type)` syntax to create a new channel.
- The channel must be typed by the values it conveys.
- You must use the `channel <-` syntax to send a value into the channel.
- You must use the `<-channel` syntax to receive a value from the channel.
- You must use a new goroutine to send the value into the channel.

## Example

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
