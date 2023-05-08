# Signals

## Problem

In some cases, we want our Go programs to handle Unix signals intelligently. For instance, we might want a server to shut down gracefully when it receives a `SIGTERM`, or a command-line tool to stop processing input if it receives a `SIGINT`.

## Requirements

- Create a buffered channel to receive `os.Signal` notifications.
- Register the channel to receive notifications of specified signals using `signal.Notify`.
- Create a goroutine to execute a blocking receive for signals.
- Print out the received signal and notify the program that it can finish.
- Wait for the expected signal and then exit.

## Example

```sh
# When we run this program it will block waiting for a
# signal. By typing `ctrl-C` (which the
# terminal shows as `^C`) we can send a `SIGINT` signal,
# causing the program to print `interrupt` and then exit.
$ go run signals.go
awaiting signal
^C
interrupt
exiting
```
