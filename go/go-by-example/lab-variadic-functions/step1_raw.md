# Variadic Functions

## Introduction

In Go, a function that can take a variable number of arguments is called a variadic function. This lab will test your understanding of how to use variadic functions in Go.

In this lab, you need to implement a function named `max` that takes an arbitrary number of integers as arguments and returns the maximum value.

- The function `max` should take an arbitrary number of integers as arguments.
- The function `max` should return the maximum value of the integers passed as arguments.

## TODO

```go
func max(nums ...int) int {
	// TODO: Implement the max function
}
```

```go
max(1, 2, 3, 4, 5) // Output: 5
max(10, 20, 30) // Output: 30
max(5, 10, 15, 20, 25, 30) // Output: 30
```

## Summary

In this lab, you learned how to use variadic functions in Go. You implemented a function named `max` that takes an arbitrary number of integers as arguments and returns the maximum value.
