# Golang Challenge: HTTP Server

## Problem

You are required to write a simple HTTP server that can handle two routes: `/hello` and `/headers`. The `/hello` route should return a simple "hello" response, while the `/headers` route should return all the HTTP request headers.

## Requirements

- The server should use the `net/http` package.
- The `/hello` route should return a "hello" response.
- The `/headers` route should return all the HTTP request headers.
- The server should listen on port `8090`.

## Example

```sh
# Run the server in the background.
$ go run http-servers.go &

# Access the `/hello` route.
$ curl localhost:8090/hello
hello
```
