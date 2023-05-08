# Atomic Counters

## Introduction
This challenge focuses on managing state in Go using the `sync/atomic` package for atomic counters accessed by multiple goroutines.

## Problem
The problem is to increment a counter exactly 1000 times using 50 goroutines and the `sync/atomic` package.

## Requirements
- Use the `sync/atomic` package to increment the counter.
- Use a WaitGroup to wait for all goroutines to finish their work.

## TODO
Complete the code block inside the goroutine to increment the counter using `AddUint64`.

```
go func() {
    for c := 0; c < 1000; c++ {
        // TODO: Use AddUint64 to increment the counter
    }
    wg.Done()
}()
```

## Example
```
ops: 50000
```

## Summary
In this challenge, we learned how to use the `sync/atomic` package to manage state in Go by incrementing a counter using multiple goroutines. The `AddUint64` function was used to atomically increment the counter, and a WaitGroup was used to wait for all goroutines to finish their work.