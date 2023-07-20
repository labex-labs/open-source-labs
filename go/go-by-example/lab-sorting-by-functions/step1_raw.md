# Sorting by Functions

## Introduction

This lab aims to test your ability to sort a collection by something other than its natural order. In this case, we will sort strings by their length instead of alphabetically.

The problem to be solved in this lab is to implement a custom sort function in Go that sorts a slice of strings by their length.

- The `byLength` type should be created as an alias for the `[]string` type.
- The `sort.Interface` should be implemented on the `byLength` type.
- The `Len` and `Swap` functions should be implemented on the `byLength` type.
- The `Less` function should be implemented on the `byLength` type to hold the actual custom sorting logic.
- The `main` function should convert the original `fruits` slice to `byLength`, and then use `sort.Sort` on that typed slice.

## TODO

```
// TODO: Implement the byLength type as an alias for the []string type.

// TODO: Implement the sort.Interface on the byLength type.

// TODO: Implement the Len and Swap functions on the byLength type.

// TODO: Implement the Less function on the byLength type to hold the actual custom sorting logic.

// TODO: Convert the original fruits slice to byLength, and then use sort.Sort on that typed slice.
```

```
Input: []string{"peach", "banana", "kiwi"}
Output: []string{"kiwi", "peach", "banana"}
```

## Summary

In this lab, we learned how to sort a collection by something other than its natural order. We implemented a custom sort function in Go that sorts a slice of strings by their length.
