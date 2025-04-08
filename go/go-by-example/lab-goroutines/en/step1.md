# Goroutines

The problem to be solved in this lab is to create and run goroutines to execute functions concurrently.

- The `f` function should print out its input string and a counter variable three times.
- The `main` function should call the `f` function synchronously and print out "direct" and a counter variable three times.
- The `main` function should call the `f` function asynchronously using a goroutine and print out "goroutine" and a counter variable three times.
- The `main` function should start a goroutine to execute an anonymous function that prints out a message.
- The `main` function should wait for the goroutines to finish executing before printing out "done".

```sh
# When we run this program, we see the output of the
# blocking call first, then the output of the two
# goroutines. The goroutines' output may be interleaved,
# because goroutines are being run concurrently by the
# Go runtime.

# Next we'll look at a complement to goroutines in
# concurrent Go programs: channels.
```

There is the full code below:

```go
// A _goroutine_ is a lightweight thread of execution.

package main

import (
	"fmt"
	"time"
)

func f(from string) {
	for i := 0; i < 3; i++ {
		fmt.Println(from, ":", i)
	}
}

func main() {

	// Suppose we have a function call `f(s)`. Here's how
	// we'd call that in the usual way, running it
	// synchronously.
	f("direct")

	// To invoke this function in a goroutine, use
	// `go f(s)`. This new goroutine will execute
	// concurrently with the calling one.
	go f("goroutine")

	// You can also start a goroutine for an anonymous
	// function call.
	go func(msg string) {
		fmt.Println(msg)
	}("going")

	// Our two function calls are running asynchronously in
	// separate goroutines now. Wait for them to finish
	// (for a more robust approach, use a [WaitGroup](waitgroups)).
	time.Sleep(time.Second)
	fmt.Println("done")
}

```
