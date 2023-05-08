# Goroutines

## Problem

The problem to be solved in this challenge is to create and run goroutines to execute functions concurrently.

## Requirements

- The `f` function should print out its input string and a counter variable three times.
- The `main` function should call the `f` function synchronously and print out "direct" and a counter variable three times.
- The `main` function should call the `f` function asynchronously using a goroutine and print out "goroutine" and a counter variable three times.
- The `main` function should start a goroutine to execute an anonymous function that prints out a message.
- The `main` function should wait for the goroutines to finish executing before printing out "done".

## Example

```sh
# When we run this program, we see the output of the
# blocking call first, then the output of the two
# goroutines. The goroutines' output may be interleaved,
# because goroutines are being run concurrently by the
# Go runtime.
$ go run goroutines.go
direct : 0
direct : 1
direct : 2
goroutine : 0
going
goroutine : 1
goroutine : 2
done

# Next we'll look at a complement to goroutines in
# concurrent Go programs: channels.

```
