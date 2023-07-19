# Select

## Introduction

This challenge aims to test your knowledge of Go's `select` statement, which allows you to wait on multiple channel operations.

## Problem

In this challenge, you are given two channels, `c1` and `c2`, which will receive a value after some amount of time. Your task is to use `select` to await both of these values simultaneously, printing each one as it arrives.

## Requirements

- You should use the `select` statement to wait on both channels.
- You should print the value received from each channel as it arrives.

## TODO

Complete the following code block:

```go
// For our example we'll select across two channels.
c1 := make(chan string)
c2 := make(chan string)

// Each channel will receive a value after some amount
// of time, to simulate e.g. blocking RPC operations
// executing in concurrent goroutines.
go func() {
    time.Sleep(1 * time.Second)
    c1 <- "one"
}()
go func() {
    time.Sleep(2 * time.Second)
    c2 <- "two"
}()

// We'll use `select` to await both of these values
// simultaneously, printing each one as it arrives.
for i := 0; i < 2; i++ {
    select {
    case msg1 := <-c1:
        fmt.Println("received", msg1)
    case msg2 := <-c2:
        fmt.Println("received", msg2)
    }
}
```

## Example

```
received one
received two
```

## Summary

This challenge tests your ability to use the `select` statement in Go to wait on multiple channel operations. By completing this challenge, you will gain a better understanding of how to use `select` to coordinate concurrent goroutines.
