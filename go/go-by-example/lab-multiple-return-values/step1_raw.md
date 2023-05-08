# Multiple Return Values

## Introduction
In Go, functions can return multiple values. This feature is commonly used to return both a result and an error value from a function.

## Problem
Complete the `swap` function to return two input parameters in reverse order.

## Requirements
- The `swap` function should take two integers as input parameters.
- The `swap` function should return two integers in reverse order.

## TODO
```go
func swap(a, b int) (int, int) {
	// TODO: Swap the values of a and b and return them in reverse order.
}

func main() {
	a, b := 3, 5
	fmt.Println(a, b)
	a, b = swap(a, b)
	fmt.Println(a, b)
}
```

## Example
```
Input: 3, 5
Output: 5, 3
```

## Summary
In this challenge, you learned how to use multiple return values in Go. By completing the `swap` function, you were able to swap two integers and return them in reverse order.