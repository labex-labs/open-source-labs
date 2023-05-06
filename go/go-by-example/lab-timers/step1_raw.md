# Timers

## Introduction
This challenge focuses on the use of timers and tickers in Golang. Timers and tickers are useful for executing code at a specific time or repeatedly at a given interval.

## Problem
The challenge requires the implementation of a timer that waits for a specified duration and then fires. Additionally, the timer should be cancellable before it fires.

## Requirements
- The `time` package should be imported.
- Two timers should be created, one that waits for 2 seconds and another that waits for 1 second.
- The first timer should print "Timer 1 fired" when it fires.
- The second timer should print "Timer 2 fired" when it fires.
- The second timer should be cancelled before it fires.
- The program should wait for 2 seconds to show that the second timer did not fire.

## TODO
```go
// Create a timer that waits for 2 seconds and print "Timer 1 fired" when it fires.

// Create a timer that waits for 1 second and print "Timer 2 fired" when it fires.
// Cancel the timer before it fires.

// Wait for 2 seconds to show that the second timer did not fire.
```

## Example
```
Timer 1 fired
Timer 2 stopped
```

## Summary
This challenge demonstrated the use of timers in Golang. Timers can be used to execute code at a specific time or to wait for a specified duration before executing code. Additionally, timers can be cancelled before they fire.