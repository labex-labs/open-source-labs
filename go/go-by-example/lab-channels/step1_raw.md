# Channels

## Introduction

The Channels challenge is designed to test your understanding of channels in Golang. Channels are used to connect concurrent goroutines, allowing values to be sent and received between them.

## Problem

In this challenge, you are required to create a new channel and send a value into it from a new goroutine. You will then receive the value from the channel and print it out.

## Requirements

- You must use the `make(chan val-type)` syntax to create a new channel.
- The channel must be typed by the values it conveys.
- You must use the `channel <-` syntax to send a value into the channel.
- You must use the `<-channel` syntax to receive a value from the channel.
- You must use a new goroutine to send the value into the channel.

## TODO

```
// Create a new channel with `make(chan val-type)`.
// Channels are typed by the values they convey.
messages := make(chan string)

// TODO: Send a value into the `messages` channel from a new goroutine.

// TODO: Receive the value from the `messages` channel and print it out.
```

## Example

```
ping
```

## Summary

The Channels challenge tests your ability to use channels in Golang to send and receive values between concurrent goroutines. By completing this challenge, you will have a better understanding of how channels work and how they can be used to improve the performance of your Golang programs.
