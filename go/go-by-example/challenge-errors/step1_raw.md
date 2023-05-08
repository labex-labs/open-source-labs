# {{ errors }}

## Introduction

The purpose of this challenge is to understand how to handle errors in Golang.

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

## TODO

```go
// By convention, errors are the last return value and
// have type `error`, a built-in interface.
func f1(arg int) (int, error) {
	if arg == 42 {

		// `errors.New` constructs a basic `error` value
		// with the given error message.
		return -1, errors.New("can't work with 42")

	}

	// A `nil` value in the error position indicates that
	// there was no error.
	return arg + 3, nil
}

// It's possible to use custom types as `error`s by
// implementing the `Error()` method on them. Here's a
// variant on the example above that uses a custom type
// to explicitly represent an argument error.
type argError struct {
	arg  int
	prob string
}

func (e *argError) Error() string {
	return fmt.Sprintf("%d - %s", e.arg, e.prob)
}

func f2(arg int) (int, error) {
	if arg == 42 {

		// In this case we use `&argError` syntax to build
		// a new struct, supplying values for the two
		// fields `arg` and `prob`.
		return -1, &argError{arg, "can't work with it"}
	}
	return arg + 3, nil
}

func main() {

	// The two loops below test out each of our
	// error-returning functions. Note that the use of an
	// inline error check on the `if` line is a common
	// idiom in Go code.
	for _, i := range []int{7, 42} {
		if r, e := f1(i); e != nil {
			fmt.Println("f1 failed:", e)
		} else {
			fmt.Println("f1 worked:", r)
		}
	}
	for _, i := range []int{7, 42} {
		if r, e := f2(i); e != nil {
			fmt.Println("f2 failed:", e)
		} else {
			fmt.Println("f2 worked:", r)
		}
	}

	// If you want to programmatically use the data in
	// a custom error, you'll need to get the error as an
	// instance of the custom error type via type
	// assertion.
	_, e := f2(42)
	if ae, ok := e.(*argError); ok {
		fmt.Println(ae.arg)
		fmt.Println(ae.prob)
	}
}
```

## Example

```
f1 worked: 10
f1 failed: can't work with 42
f2 worked: 10
f2 failed: 42 - can't work with it
42
can't work with it
```

## Summary

This challenge demonstrates how to handle errors in Golang using the `error` interface and custom error types. It also shows how to programmatically use the data in a custom error.
