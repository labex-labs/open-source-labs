# Mutexes

The problem to be solved in this challenge is to increment a named counter in a loop using multiple goroutines, and ensure that the access to the counter is synchronized.

## Requirements

- Use a `Container` struct to hold a map of counters.
- Use a `Mutex` to synchronize access to the `counters` map.
- The `Container` struct should have an `inc` method that takes a `name` string and increments the corresponding counter in the `counters` map.
- The `inc` method should lock the mutex before accessing the `counters` map, and unlock it at the end of the function using a `defer` statement.
- Use the `sync.WaitGroup` struct to wait for the goroutines to finish.
- Use the `fmt.Println` function to print the `counters` map.

## Example

```sh
# Running the program shows that the counters
# updated as expected.

# Next we'll look at implementing this same state
# management task using only goroutines and channels.
```
