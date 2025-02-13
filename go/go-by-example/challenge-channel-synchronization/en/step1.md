# Channel Synchronization

The problem to be solved in this challenge is to create a goroutine that performs some work and notifies another goroutine when it's done using a channel.

## Requirements

To complete this challenge, you will need to:

- Create a function named `worker` that takes a channel of type `bool` as a parameter.
- Inside the `worker` function, perform some work and then send a value to the channel to notify that the work is done.
- In the `main` function, create a channel of type `bool` with a buffer size of 1.
- Start a goroutine that calls the `worker` function and passes the channel as a parameter.
- Block the `main` function until a value is received from the channel.

## Example

```sh
$ go run channel-synchronization.go
working...done

# If you removed the `<- done` line from this program, the
# program would exit before the `worker` even
# started.
```
