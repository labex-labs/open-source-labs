# Slices

## Introduction

The Slices challenge is designed to test your knowledge of the slice data type in Go. Slices are a more powerful interface to sequences than arrays, and this challenge will help you understand how to use them.

## Problem

The problem to be solved in this challenge is to create and manipulate slices in Go. You will need to create an empty slice with non-zero length, set and get values in the slice, use the `len` function to get the length of the slice, use the `append` function to add new values to the slice, use the `copy` function to copy a slice, and use the slice operator to get a slice of elements from an existing slice.

## Requirements

To complete this challenge, you will need to have a basic understanding of Go syntax and the slice data type. You will also need to be familiar with the `make`, `append`, and `copy` functions, as well as the slice operator.

## TODO

Use the TODO keyword to mark the code that needs to be completed.

```
// Create an empty slice with non-zero length
s := make([]int, TODO)

// Set values in the slice
s[0] = TODO
s[1] = TODO
s[2] = TODO

// Get values from the slice
fmt.Println("s[0]:", TODO)
fmt.Println("s[1]:", TODO)
fmt.Println("s[2]:", TODO)

// Get the length of the slice
fmt.Println("len(s):", TODO)

// Append new values to the slice
s = append(s, TODO)
s = append(s, TODO, TODO)
fmt.Println("s:", TODO)

// Copy the slice
c := make([]int, TODO)
copy(c, s)
fmt.Println("c:", TODO)

// Get a slice of elements from an existing slice
l := s[TODO:TODO]
fmt.Println("l:", TODO)
```

## Example

```
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
```

## Summary

The Slices challenge is designed to test your knowledge of the slice data type in Go. By completing this challenge, you will gain a better understanding of how to create and manipulate slices in Go, including how to set and get values in a slice, use the `len` function, use the `append` and `copy` functions, and use the slice operator.
