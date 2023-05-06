# Slices

## Problem

The problem to be solved in this challenge is to create and manipulate slices in Go. You will need to create an empty slice with non-zero length, set and get values in the slice, use the `len` function to get the length of the slice, use the `append` function to add new values to the slice, use the `copy` function to copy a slice, and use the slice operator to get a slice of elements from an existing slice.

## Requirements

To complete this challenge, you will need to have a basic understanding of Go syntax and the slice data type. You will also need to be familiar with the `make`, `append`, and `copy` functions, as well as the slice operator.

## Example

```sh
# Note that while slices are different types than arrays,
# they are rendered similarly by `fmt.Println`.
$ go run slices.go
emp: [  ]
set: [a b c]
get: c
len: 3
apd: [a b c d e f]
cpy: [a b c d e f]
sl1: [c d e]
sl2: [a b c d e]
sl3: [c d e f]
dcl: [g h i]
2d:  [[0] [1 2] [2 3 4]]

# Check out this [great blog post](https://go.dev/blog/slices-intro)
# by the Go team for more details on the design and
# implementation of slices in Go.

# Now that we've seen arrays and slices we'll look at
# Go's other key builtin data structure: maps.

```