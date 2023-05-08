# Timers and Tickers

## Problem

In this challenge, you need to create a ticker that ticks every 500ms until we stop it. You will use a channel to await the values as they arrive.

## Requirements

- Use the `time` package to create a ticker.
- Use a channel to await the values as they arrive.
- Use the `select` statement to receive values from the channel.
- Stop the ticker after 1600ms.

## Example

```sh
# When we run this program the ticker should tick 3 times
# before we stop it.
$ go run tickers.go
Tick at 2012-09-23 11:29:56.487625 -0700 PDT
Tick at 2012-09-23 11:29:56.988063 -0700 PDT
Tick at 2012-09-23 11:29:57.488076 -0700 PDT
Ticker stopped

```