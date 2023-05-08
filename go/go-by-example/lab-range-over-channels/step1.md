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

## Solution

```go
// In a [previous](range) example we saw how `for` and
// `range` provide iteration over basic data structures.
// We can also use this syntax to iterate over
// values received from a channel.

package main

import "fmt"

func main() {

	// We'll iterate over 2 values in the `queue` channel.
	queue := make(chan string, 2)
	queue <- "one"
	queue <- "two"
	close(queue)

	// This `range` iterates over each element as it's
	// received from `queue`. Because we `close`d the
	// channel above, the iteration terminates after
	// receiving the 2 elements.
	for elem := range queue {
		fmt.Println(elem)
	}
}

```
