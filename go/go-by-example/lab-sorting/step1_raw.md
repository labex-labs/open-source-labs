# Sorting

## Introduction

The Go programming language provides a built-in package named `sort` that implements sorting for builtins and user-defined types. In this challenge, we will focus on sorting for builtins.

## Problem

The problem to be solved in this challenge is to sort slices of strings and integers using the `sort` package.

## Requirements

- The `sort` package must be imported.
- The `sort.Strings()` function must be used to sort a slice of strings.
- The `sort.Ints()` function must be used to sort a slice of integers.
- The `sort.IntsAreSorted()` function must be used to check if a slice of integers is already sorted.

## TODO

Complete the following code to sort the given slices of strings and integers using the `sort` package:

```
package main

import (
	"fmt"
	"sort"
)

func main() {

	// TODO: Sort the following slice of strings
	strs := []string{"c", "a", "b"}

	// TODO: Sort the following slice of integers
	ints := []int{7, 2, 4}

	// TODO: Use the sort.IntsAreSorted() function to check if the following slice of integers is already sorted
	s := sort.IntsAreSorted(ints)

	fmt.Println("Strings:", strs)
	fmt.Println("Ints:   ", ints)
	fmt.Println("Sorted: ", s)
}
```

## Example

```
Strings: [a b c]
Ints:    [2 4 7]
Sorted:  true
```

## Summary

The `sort` package in Go provides a simple and efficient way to sort slices of built-in types. By using the `sort.Strings()`, `sort.Ints()`, and `sort.IntsAreSorted()` functions, we can easily sort and check if a slice is already sorted.
