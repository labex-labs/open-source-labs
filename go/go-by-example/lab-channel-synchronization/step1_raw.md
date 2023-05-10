# Golang Challenge: Channel Synchronization

## Introduction

This challenge aims to test your knowledge of using channels to synchronize execution across goroutines.

## Problem

The problem to be solved in this challenge is to create a goroutine that performs some work and notifies another goroutine when it's done using a channel.

## Requirements

To complete this challenge, you will need to:

- Create a function named `worker` that takes a channel of type `bool` as a parameter.
- Inside the `worker` function, perform some work and then send a value to the channel to notify that the work is done.
- In the `main` function, create a channel of type `bool` with a buffer size of 1.
- Start a goroutine that calls the `worker` function and passes the channel as a parameter.
- Block the `main` function until a value is received from the channel.

## TODO

Complete the `worker` function to perform some work and send a value to the channel to notify that the work is done.

```go
func worker(done chan bool) {
    // TODO: Perform some work
    // TODO: Send a value to the channel to notify that the work is done
}
```

## Example

```
working...done
```

## Summary

In this challenge, you learned how to use channels to synchronize execution across goroutines. By creating a channel and passing it to a goroutine, you can wait for the goroutine to finish its work and notify you when it's done.
