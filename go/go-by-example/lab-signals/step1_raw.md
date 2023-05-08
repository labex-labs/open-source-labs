# Signals

## Introduction
The Signals challenge demonstrates how to handle Unix signals in Go programs using channels.

## Problem
In some cases, we want our Go programs to handle Unix signals intelligently. For instance, we might want a server to shut down gracefully when it receives a `SIGTERM`, or a command-line tool to stop processing input if it receives a `SIGINT`. 

## Requirements
- Create a buffered channel to receive `os.Signal` notifications.
- Register the channel to receive notifications of specified signals using `signal.Notify`.
- Create a goroutine to execute a blocking receive for signals.
- Print out the received signal and notify the program that it can finish.
- Wait for the expected signal and then exit.

## TODO
```go
// TODO: Create a buffered channel to receive `os.Signal` notifications.
sigs := make(chan os.Signal, 1)

// TODO: Register the channel to receive notifications of specified signals using `signal.Notify`.
signal.Notify(sigs, syscall.SIGINT, syscall.SIGTERM)

// TODO: Create a goroutine to execute a blocking receive for signals.
go func() {
    // TODO: When it gets one, print it out and then notify the program that it can finish.
    sig := <-sigs
    fmt.Println()
    fmt.Println(sig)
    done <- true
}()

// TODO: Wait for the expected signal and then exit.
<-done
```

## Example
```
$ go run signals.go
awaiting signal
^C
interrupt
exiting
```

## Summary
The Signals challenge demonstrates how to handle Unix signals in Go programs using channels. By creating a buffered channel to receive `os.Signal` notifications and registering the channel to receive notifications of specified signals using `signal.Notify`, we can gracefully handle signals and exit the program when the expected signal is received.