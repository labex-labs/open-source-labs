# Sorting

## Problem

The problem to be solved in this challenge is to sort slices of strings and integers using the `sort` package.

## Requirements

- The `sort` package must be imported.
- The `sort.Strings()` function must be used to sort a slice of strings.
- The `sort.Ints()` function must be used to sort a slice of integers.
- The `sort.IntsAreSorted()` function must be used to check if a slice of integers is already sorted.

## Example

```sh
# Running our program prints the sorted string and int
# slices and `true` as the result of our `AreSorted` test.
$ go run sorting.go
Strings: [a b c]
Ints: [2 4 7]
Sorted: true
```

## Solution

```go
// Go's `sort` package implements sorting for builtins
// and user-defined types. We'll look at sorting for
// builtins first.

package main

import (
	"fmt"
	"sort"
)

func main() {

	// Sort methods are specific to the builtin type;
	// here's an example for strings. Note that sorting is
	// in-place, so it changes the given slice and doesn't
	// return a new one.
	strs := []string{"c", "a", "b"}
	sort.Strings(strs)
	fmt.Println("Strings:", strs)

	// An example of sorting `int`s.
	ints := []int{7, 2, 4}
	sort.Ints(ints)
	fmt.Println("Ints:   ", ints)

	// We can also use `sort` to check if a slice is
	// already in sorted order.
	s := sort.IntsAreSorted(ints)
	fmt.Println("Sorted: ", s)
}

```
