# Errors

## Problem

The challenge provides two functions that return an error if the input argument is 42. The first function returns a basic error value, while the second function uses a custom type to represent the error.

## Requirements

- The `errors` package must be imported.
- The `f1` function must return an error if the input argument is 42.
- The `f2` function must return an error of type `argError` if the input argument is 42.
- The `argError` type must have two fields: `arg` and `prob`.
- The `argError` type must implement the `Error()` method.
- The `main` function must call both `f1` and `f2` with input arguments of 7 and 42.
- The `main` function must print the result of each function call, along with any error that was returned.
- The `main` function must demonstrate how to programmatically use the data in a custom error.

## Example

```sh
$ go run errors.go
f1 worked: 10
f1 failed: can't work with 42
f2 worked: 10
f2 failed: 42 - can't work with it
42
can't work with it

# See this [great post](https://go.dev/blog/error-handling-and-go)
# on the Go blog for more on error handling.

```
