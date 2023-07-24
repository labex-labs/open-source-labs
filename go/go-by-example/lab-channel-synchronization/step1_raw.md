# Channel Synchronization

## Introduction

This lab aims to test your knowledge of using channels to synchronize execution across goroutines.

The problem to be solved in this lab is to create a goroutine that performs some work and notifies another goroutine when it's done using a channel.

To complete this lab, you will need to:

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

```
working...done
```

## Summary

In this lab, you learned how to use channels to synchronize execution across goroutines. By creating a channel and passing it to a goroutine, you can wait for the goroutine to finish its work and notify you when it's done.
