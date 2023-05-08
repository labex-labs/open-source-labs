# Methods

## Problem

The code provided defines a struct type called `rect` with two fields, `width` and `height`. Two methods are defined for this struct type, `area` and `perim`. The `area` method calculates the area of the rectangle, and the `perim` method calculates the perimeter of the rectangle. The main function calls these two methods and prints their results.

## Requirements

- The `area` method should have a receiver type of `*rect`.
- The `perim` method should have a receiver type of `rect`.
- The `area` method should return the area of the rectangle.
- The `perim` method should return the perimeter of the rectangle.
- The `main` function should call both methods and print their results.

## Example

```sh
$ go run methods.go
area: 50
perim: 30
area: 50
perim: 30

# Next we'll look at Go's mechanism for grouping and
# naming related sets of methods: interfaces.
```

## Solution

```go
// Go supports _methods_ defined on struct types.

package main

import "fmt"

type rect struct {
	width, height int
}

// This `area` method has a _receiver type_ of `*rect`.
func (r *rect) area() int {
	return r.width * r.height
}

// Methods can be defined for either pointer or value
// receiver types. Here's an example of a value receiver.
func (r rect) perim() int {
	return 2*r.width + 2*r.height
}

func main() {
	r := rect{width: 10, height: 5}

	// Here we call the 2 methods defined for our struct.
	fmt.Println("area: ", r.area())
	fmt.Println("perim:", r.perim())

	// Go automatically handles conversion between values
	// and pointers for method calls. You may want to use
	// a pointer receiver type to avoid copying on method
	// calls or to allow the method to mutate the
	// receiving struct.
	rp := &r
	fmt.Println("area: ", rp.area())
	fmt.Println("perim:", rp.perim())
}

```
