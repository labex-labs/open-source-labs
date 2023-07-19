# HTTP Server

## Introduction

This challenge aims to test your ability to write a basic HTTP server using the `net/http` package in Golang.

## Problem

You are required to write a simple HTTP server that can handle two routes: `/hello` and `/headers`. The `/hello` route should return a simple "hello" response, while the `/headers` route should return all the HTTP request headers.

## Requirements

- The server should use the `net/http` package.
- The `/hello` route should return a "hello" response.
- The `/headers` route should return all the HTTP request headers.
- The server should listen on port `8090`.

## TODO

```go
// TODO: Write a handler function for the `/hello` route that returns a "hello" response.

// TODO: Write a handler function for the `/headers` route that returns all the HTTP request headers.

// TODO: Register the handlers on server routes using the `http.HandleFunc` function.

// TODO: Call the `ListenAndServe` function with the port and a handler.
```

## Example

If you run the server and make a request to the `/hello` route, you should receive a "hello" response. If you make a request to the `/headers` route, you should receive all the HTTP request headers.

## Summary

In this challenge, you were required to write a simple HTTP server that can handle two routes: `/hello` and `/headers`. You learned how to use the `net/http` package to write handlers for each route and register them on the server. Finally, you learned how to start the server and listen for incoming requests.
