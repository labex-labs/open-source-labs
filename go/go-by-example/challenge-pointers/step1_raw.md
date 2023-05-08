# Pointers

## Introduction
This challenge will test your understanding of pointers in Golang. Pointers are used to pass references to values and records within your program.

## Problem
The problem is to understand how pointers work in contrast to values with two functions: `zeroval` and `zeroptr`. `zeroval` has an `int` parameter, so arguments will be passed to it by value. `zeroval` will get a copy of `ival` distinct from the one in the calling function. `zeroptr` in contrast has an `*int` parameter, meaning that it takes an `int` pointer. The `*iptr` code in the function body then _dereferences_ the pointer from its memory address to the current value at that address. Assigning a value to a dereferenced pointer changes the value at the referenced address.

## Requirements
- You should have a basic understanding of Golang.
- You should know how to define and use functions in Golang.
- You should know how to use pointers in Golang.

## TODO
Complete the `zeroval` and `zeroptr` functions. Use the TODO keyword to mark the code that needs to be completed.

```go
func zeroval(ival int) {
    // TODO: Set ival to 0
}

func zeroptr(iptr *int) {
    // TODO: Set the value of iptr to 0
}
```

## Example
```
initial: 1
zeroval: 1
zeroptr: 0
pointer: 0x40e020
```

## Summary
In this challenge, you learned how to use pointers in Golang. You also learned the difference between passing values and pointers to functions.