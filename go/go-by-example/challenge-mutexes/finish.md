# Summary

In this challenge, we learned how to use mutexes to safely access data across multiple goroutines. We created a `Container` struct to hold a map of counters, and used a `Mutex` to synchronize access to the `counters` map. We also implemented an `inc` method to increment the named counter, and used the `sync.WaitGroup` struct to wait for the goroutines to finish. Finally, we printed the `counters` map using the `fmt.Println` function.
