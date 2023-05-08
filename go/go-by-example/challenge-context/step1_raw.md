# Golang Challenge - {{context}}

## Introduction
This challenge aims to demonstrate the usage of `context.Context` for controlling cancellation in Golang. A `Context` carries deadlines, cancellation signals, and other request-scoped values across API boundaries and goroutines.

## Problem
The `hello` function simulates some work the server is doing by waiting for a few seconds before sending a reply to the client. While working, keep an eye on the context's `Done()` channel for a signal that we should cancel the work and return as soon as possible.

## Requirements
- Golang version 1.13 or higher.

## TODO
Complete the `main` function to create a `Context` with a 5-second timeout and pass it to the `hello` function.

```go
func main() {
    // TODO: Create a context with a 5-second timeout
    // TODO: Pass the context to the hello function
    // As before, we register our handler on the "/hello"
    // route, and start serving.
    http.HandleFunc("/hello", hello)
    http.ListenAndServe(":8090", nil)
}
```

## Example
Assuming the `hello` function takes longer than 5 seconds to complete, the server should return an error message to the client after the timeout.

```
$ curl http://localhost:8090/hello
context deadline exceeded
```

## Summary
In this challenge, we learned how to use `context.Context` to control cancellation in Golang. By creating a `Context` with a timeout and passing it to a function, we can ensure that the function returns as soon as possible if the timeout is exceeded.