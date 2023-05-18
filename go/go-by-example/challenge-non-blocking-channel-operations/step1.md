# Non-Blocking Channel Operations

## Problem

The problem to be solved in this challenge is to implement non-blocking channel operations using the `select` statement with a `default` clause.

## Requirements

- Implement a non-blocking receive on a channel using the `select` statement with a `default` clause.
- Implement a non-blocking send on a channel using the `select` statement with a `default` clause.
- Implement a multi-way non-blocking select using the `select` statement with multiple `case` clauses and a `default` clause.

## Example

```sh
$ go run non-blocking-channel-operations.go
no message received
no message sent
no activity
```
