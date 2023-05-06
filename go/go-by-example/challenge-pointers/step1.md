# Pointers

## Problem

The problem is to understand how pointers work in contrast to values with two functions: `zeroval` and `zeroptr`. `zeroval` has an `int` parameter, so arguments will be passed to it by value. `zeroval` will get a copy of `ival` distinct from the one in the calling function. `zeroptr` in contrast has an `*int` parameter, meaning that it takes an `int` pointer. The `*iptr` code in the function body then _dereferences_ the pointer from its memory address to the current value at that address. Assigning a value to a dereferenced pointer changes the value at the referenced address.

## Requirements

- You should have a basic understanding of Golang.
- You should know how to define and use functions in Golang.
- You should know how to use pointers in Golang.

## Example

```sh
# `zeroval` doesn't change the `i` in `main`, but
# `zeroptr` does because it has a reference to
# the memory address for that variable.
$ go run pointers.go
initial: 1
zeroval: 1
zeroptr: 0
pointer: 0x42131100

```