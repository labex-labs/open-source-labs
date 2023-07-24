# Channel Directions

## Introduction

This lab aims to test your understanding of using channels as function parameters in Golang.

The problem to be solved in this lab is to modify the given code to ensure that the channels used as function parameters are specified to only send or receive values.

- Basic knowledge of Golang
- Understanding of channels and their usage in Golang

## TODO

```go
// This `ping` function only accepts a channel for sending
// values. It would be a compile-time error to try to
// receive on this channel.
func ping(pings chan<- string, msg string) {
	pings <- msg
}

// The `pong` function accepts one channel for receives
// (`pings`) and a second for sends (`pongs`).
func pong(pings <-chan string, pongs chan<- string) {
	msg := <-pings
	pongs <- msg
}

func main() {
	pings := make(chan string, 1)
	pongs := make(chan string, 1)
	ping(pings, "passed message")
	pong(pings, pongs)
	fmt.Println(<-pongs)
}
```

```
passed message
```

## Summary

In this lab, you learned how to specify if a channel is meant to only send or receive values, which increases the type-safety of the program.
