# Range Over Channels

## Problem

You are required to write a function that takes in a channel of integers and returns the sum of all the integers received from the channel.

## Requirements

- The function should be named `sumInts`.
- The function should take in a single parameter of type `chan int`.
- The function should return a single integer value.
- You are not allowed to use any loops or recursion inside the function body.
- You are not allowed to use any external packages.

## Example

```sh
$ go run range-over-channels.go
one
two

# This example also showed that it's possible to close
# a non-empty channel but still have the remaining
# values be received.

```