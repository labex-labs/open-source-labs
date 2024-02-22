# Context

The `hello` function simulates some work the server is doing by waiting for a few seconds before sending a reply to the client. While working, keep an eye on the context's `Done()` channel for a signal that we should cancel the work and return as soon as possible.

## Requirements

- Golang version 1.13 or higher.

## Example

```sh
# Run the server in the background.
$ go run context-in-http-servers.go &

# Simulate a client request to `/hello`, hitting
# Ctrl+C shortly after starting to signal
# cancellation.
$ curl localhost:8090/hello
server: hello handler started
^C
server: context canceled
server: hello handler ended
```
