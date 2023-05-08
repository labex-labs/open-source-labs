# Golang Challenge: Channel Buffering

## Problem

By default, channels in Golang are unbuffered, meaning that they only accept sends if there is a corresponding receive ready to receive the sent value. However, buffered channels accept a limited number of values without a corresponding receiver for those values. In this challenge, you are required to create a buffered channel and send values into the channel without a corresponding concurrent receive.

## Requirements

- Basic knowledge of Golang channels
- Understanding of buffered channels

## Example

```sh
$ go run channel-buffering.go 
buffered
channel

```