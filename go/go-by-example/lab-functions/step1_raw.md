# Functions

## Introduction

In this challenge, we will learn about functions in Go. We will see how to define functions, how to pass arguments to them, and how to return values from them.

## Problem

In the given code, we have two functions `plus` and `plusPlus`. The `plus` function takes two integers as arguments and returns their sum. The `plusPlus` function takes three integers as arguments and returns their sum. Your task is to complete the `plusPlus` function by adding the third integer to the sum of the first two integers.

## Requirements

- The `plus` function should take two integers as arguments and return their sum as an integer.
- The `plusPlus` function should take three integers as arguments and return their sum as an integer.
- The `plusPlus` function should use the `plus` function to calculate the sum of the first two integers.

## TODO

```go
func plusPlus(a, b, c int) int {
    // TODO: Add the third integer to the sum of the first two integers
    // and return the result.
}

func main() {
    res := plusPlus(1, 2, 3)
    fmt.Println("1+2+3 =", res)
}
```

## Example

```
1+2+3 = 6
```

## Summary

In this challenge, we learned about functions in Go. We saw how to define functions, how to pass arguments to them, and how to return values from them. We also saw how to use one function inside another function.
