
// Launch several goroutines and increment the WaitGroup
// counter for each.
for i := 1; i <= 5; i++ {
    wg.Add(1)
    // Avoid re-use of the same `i` value in each goroutine closure.
    // See [the FAQ](https://golang.org/doc/faq#closures_and_goroutines)
    // for more details.
    i := i

    // Wrap the worker call in a closure that makes sure to tell
    // the WaitGroup that this worker is done. This way the worker
    // itself does not have to be aware of the concurrency primitives
    // involved in its execution.
    go func() {
        defer wg.Done()
        worker(i)
    }()
}

// Block until the WaitGroup counter goes back to 0;
// all the workers notified they're done.
wg.Wait()
