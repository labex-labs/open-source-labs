# Methods

## Introduction

This challenge aims to test the knowledge of the Go programming language's method feature.

## Problem

The code provided defines a struct type called `rect` with two fields, `width` and `height`. Two methods are defined for this struct type, `area` and `perim`. The `area` method calculates the area of the rectangle, and the `perim` method calculates the perimeter of the rectangle. The main function calls these two methods and prints their results.

## Requirements

- The `area` method should have a receiver type of `*rect`.
- The `perim` method should have a receiver type of `rect`.
- The `area` method should return the area of the rectangle.
- The `perim` method should return the perimeter of the rectangle.
- The `main` function should call both methods and print their results.

## TODO

Complete the `area` and `perim` methods according to the requirements.

```go
// This `area` method has a _receiver type_ of `*rect`.
func (r *rect) area() int {
	// TODO: Calculate the area of the rectangle.
}

// Methods can be defined for either pointer or value
// receiver types. Here's an example of a value receiver.
func (r rect) perim() int {
	// TODO: Calculate the perimeter of the rectangle.
}
```

## Example

```
area:  50
perim: 30
area:  50
perim: 30
```

## Summary

This challenge tests the ability to define methods in Go and use them to perform calculations on struct types. The `area` and `perim` methods are defined for the `rect` struct type, and the `main` function calls these methods and prints their results.
