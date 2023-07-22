# Recover

## Problem

The `mayPanic` function in the provided code will panic when called. Your task is to modify the `main` function to recover from the panic and print the error message.

## Requirements

- Use the `recover` function to handle the panic in the `mayPanic` function.
- Print the error message when a panic occurs.

## Example

```sh
$ go run recover.go
Recovered. Error:
a problem
```
