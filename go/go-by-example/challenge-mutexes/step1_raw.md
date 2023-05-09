# Mutexes

## Introduction

This challenge aims to demonstrate how to use mutexes to safely access data across multiple goroutines.

## Problem

The problem to be solved in this challenge is to increment a named counter in a loop using multiple goroutines, and ensure that the access to the counter is synchronized.

## Requirements

- Use a `Container` struct to hold a map of counters.
- Use a `Mutex` to synchronize access to the `counters` map.
- The `Container` struct should have an `inc` method that takes a `name` string and increments the corresponding counter in the `counters` map.
- The `inc` method should lock the mutex before accessing the `counters` map, and unlock it at the end of the function using a `defer` statement.
- Use the `sync.WaitGroup` struct to wait for the goroutines to finish.
- Use the `fmt.Println` function to print the `counters` map.

## TODO

```go
// TODO: Use a mutex to synchronize access to the counters map.
type Container struct {
	counters map[string]int
}

// TODO: Implement the inc method to increment the named counter.
func (c *Container) inc(name string) {
	c.counters[name]++
}

func main() {
	c := Container{
		counters: map[string]int{"a": 0, "b": 0},
	}

	var wg sync.WaitGroup

	doIncrement := func(name string, n int) {
		for i := 0; i < n; i++ {
			// TODO: Call the inc method to increment the named counter.
		}
		wg.Done()
	}

	wg.Add(3)
	go doIncrement("a", 10000)
	go doIncrement("a", 10000)
	go doIncrement("b", 10000)

	wg.Wait()
	// TODO: Use fmt.Println to print the counters map.
}
```

## Example

```
map[a:20000 b:10000]
```

## Summary

In this challenge, we learned how to use mutexes to safely access data across multiple goroutines. We created a `Container` struct to hold a map of counters, and used a `Mutex` to synchronize access to the `counters` map. We also implemented an `inc` method to increment the named counter, and used the `sync.WaitGroup` struct to wait for the goroutines to finish. Finally, we printed the `counters` map using the `fmt.Println` function.
