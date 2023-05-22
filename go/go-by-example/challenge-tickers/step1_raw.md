# Timers and Tickers

## Introduction

This challenge is about using tickers in Golang. Tickers are used when you want to do something repeatedly at regular intervals.

## Problem

In this challenge, you need to create a ticker that ticks every 500ms until we stop it. You will use a channel to await the values as they arrive.

## Requirements

- Use the `time` package to create a ticker.
- Use a channel to await the values as they arrive.
- Use the `select` statement to receive values from the channel.
- Stop the ticker after 1600ms.

## TODO

```
// Create a ticker that ticks every 500ms until we stop it.
// Use a channel to await the values as they arrive.
// Use the `select` statement to receive values from the channel.
// Stop the ticker after 1600ms.

func tickerFunc() {
    ticker := // TODO: Create a ticker that ticks every 500ms
    done := make(chan bool)

    go func() {
        for {
            select {
            case <-done:
                return
            case t := <-ticker.C:
                fmt.Println("Tick at", t)
            }
        }
    }()

    // TODO: Stop the ticker after 1600ms
    fmt.Println("Ticker stopped")
}
```

## Example

```
Tick at 2021-10-01 15:04:00.500 +0800 CST m=+0.501000001
Tick at 2021-10-01 15:04:01 +0800 CST m=+1.001000001
Tick at 2021-10-01 15:04:01.500 +0800 CST m=+1.501000001
Tick at 2021-10-01 15:04:02 +0800 CST m=+2.001000001
Ticker stopped
```

## Summary

In this challenge, you learned how to use tickers in Golang. You created a ticker that ticks every 500ms until we stop it, used a channel to await the values as they arrive, and stopped the ticker after 1600ms.
