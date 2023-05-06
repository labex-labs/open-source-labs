# Golang Challenge: Channel Buffering

## Introduction
This challenge aims to test your understanding of buffered channels in Golang.

## Problem
By default, channels in Golang are unbuffered, meaning that they only accept sends if there is a corresponding receive ready to receive the sent value. However, buffered channels accept a limited number of values without a corresponding receiver for those values. In this challenge, you are required to create a buffered channel and send values into the channel without a corresponding concurrent receive.

## Requirements
- Basic knowledge of Golang channels
- Understanding of buffered channels

## TODO
Complete the code block in the `main` function to create a buffered channel of strings that can buffer up to 2 values. Send the values "buffered" and "channel" into the channel without a corresponding concurrent receive. Finally, receive these two values from the channel and print them to the console.

```go
messages := make(chan string, 2)

// TODO: Send "buffered" and "channel" into the channel without a corresponding concurrent receive.

fmt.Println(<-messages)
fmt.Println(<-messages)
```

## Example
```
buffered
channel
```

## Summary
In this challenge, you have learned how to create a buffered channel in Golang and send values into the channel without a corresponding concurrent receive. This is useful in scenarios where you want to send values to a channel without blocking the sender.