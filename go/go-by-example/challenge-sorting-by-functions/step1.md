# Sorting by Functions

The problem to be solved in this challenge is to implement a custom sort function in Go that sorts a slice of strings by their length.

## Requirements

- The `byLength` type should be created as an alias for the `[]string` type.
- The `sort.Interface` should be implemented on the `byLength` type.
- The `Len` and `Swap` functions should be implemented on the `byLength` type.
- The `Less` function should be implemented on the `byLength` type to hold the actual custom sorting logic.
- The `main` function should convert the original `fruits` slice to `byLength`, and then use `sort.Sort` on that typed slice.

## Example

```sh
# Running our program shows a list sorted by string
# length, as desired.
$ go run sorting-by-functions.go
[kiwi peach banana]

# By following this same pattern of creating a custom
# type, implementing the three `Interface` methods on that
# type, and then calling sort.Sort on a collection of that
# custom type, we can sort Go slices by arbitrary
# functions.
```
