# {{ range-over-channels }}

## Introduction

This challenge aims to test your ability to iterate over values received from a channel using the `for` and `range` syntax in Golang.

## Problem

You are required to write a function that takes in a channel of integers and returns the sum of all the integers received from the channel.

## Requirements

- The function should be named `sumInts`.
- The function should take in a single parameter of type `chan int`.
- The function should return a single integer value.
- You are not allowed to use any loops or recursion inside the function body.
- You are not allowed to use any external packages.

## TODO

```go
func sumInts(c chan int) int {
    sum := 0
    // TODO: Iterate over values received from the channel
    // and add them to the sum variable.
    // Hint: Use the `range` keyword to iterate over the channel.
    // Hint: Use a goroutine to receive values from the channel.
    return sum
}
```

## Example

```go
c := make(chan int)
go func() {
    c <- 1
    c <- 2
    c <- 3
    close(c)
}()
fmt.Println(sumInts(c))
// Output: 6
```

## Summary

In this challenge, you were tasked with writing a function that sums up all the integers received from a channel using the `for` and `range` syntax in Golang. By completing this challenge, you should have a better understanding of how to iterate over values received from a channel and how to use goroutines to receive values from a channel.
