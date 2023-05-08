# Timeouts

## Problem

When programs connect to external resources or need to bound execution time, timeouts are important. The challenge is to implement timeouts in Go using channels and `select`.

## Requirements

- Implement timeouts in Go using channels and `select`.
- Use a buffered channel to prevent goroutine leaks in case the channel is never read.
- Use `time.After` to await a value to be sent after the timeout.
- Use `select` to proceed with the first receive that's ready.

## Example

```sh
# Running this program shows the first operation timing
# out and the second succeeding.
$ go run timeouts.go 
timeout 1
result 2

```