# Non-Blocking Channel Operations

## Introduction

This lab aims to test your understanding of non-blocking channel operations in Golang. You will be required to implement non-blocking sends, receives, and multi-way selects using the `select` statement with a `default` clause.

The problem to be solved in this lab is to implement non-blocking channel operations using the `select` statement with a `default` clause.

- Implement a non-blocking receive on a channel using the `select` statement with a `default` clause.
- Implement a non-blocking send on a channel using the `select` statement with a `default` clause.
- Implement a multi-way non-blocking select using the `select` statement with multiple `case` clauses and a `default` clause.

## TODO

```go
messages := make(chan string)
signals := make(chan bool)

// TODO: Implement a non-blocking receive on the messages channel.
// If a value is available on messages, print "received message <message>".
// If not, print "no message received".

// TODO: Implement a non-blocking send on the messages channel.
// Send the message "hi" to the messages channel.
// If the channel has no buffer and there is no receiver, print "no message sent".

// TODO: Implement a multi-way non-blocking select.
// If a value is available on messages, print "received message <message>".
// If a value is available on signals, print "received signal <signal>".
// If no value is available on either channel, print "no activity".
```

```
no message received
no message sent
no activity
```

## Summary

In this lab, you learned how to implement non-blocking channel operations using the `select` statement with a `default` clause. You implemented a non-blocking receive, a non-blocking send, and a multi-way non-blocking select.
