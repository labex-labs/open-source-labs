# Recover

## Introduction

In Golang, `recover` is a built-in function that can be used to recover from a panic. This lab will test your ability to use `recover` to handle panics.

The `mayPanic` function in the provided code will panic when called. Your task is to modify the `main` function to recover from the panic and print the error message.

- Use the `recover` function to handle the panic in the `mayPanic` function.
- Print the error message when a panic occurs.

## TODO

```go
// This function panics.
func mayPanic() {
	panic("a problem")
}

func main() {
	// `recover` must be called within a deferred function.
	// When the enclosing function panics, the defer will
	// activate and a `recover` call within it will catch
	// the panic.
	defer func() {
		// TODO: Use recover to handle the panic and print the error message.
	}()

	mayPanic()

	// This code will not run, because `mayPanic` panics.
	// The execution of `main` stops at the point of the
	// panic and resumes in the deferred closure.
	fmt.Println("After mayPanic()")
}
```

```
Recovered. Error:
 a problem
```

## Summary

In this lab, you learned how to use the `recover` function to handle panics in Golang. By using `recover`, you can prevent your program from crashing and continue executing code.
