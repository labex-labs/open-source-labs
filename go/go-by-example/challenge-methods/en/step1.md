# Methods

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
