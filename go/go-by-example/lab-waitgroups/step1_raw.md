# waitgroups

## Introduction

The `waitgroups` lab is designed to help you understand how to use a wait group to wait for multiple goroutines to finish.

The problem to be solved in this lab is to launch several goroutines and increment the WaitGroup counter for each. Then, we need to wait for all the goroutines launched to finish.

- Basic knowledge of Golang.
- Understanding of concurrency in Golang.
- Familiarity with the `sync` package.

## TODO

Complete the code block marked with the TODO keyword to launch several goroutines and increment the WaitGroup counter for each. Then, wait for all the goroutines launched to finish.

```go
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
```

```
Worker 1 starting
Worker 2 starting
Worker 3 starting
Worker 4 starting
Worker 5 starting
Worker 1 done
Worker 2 done
Worker 3 done
Worker 4 done
Worker 5 done
```

## Summary

In this lab, we learned how to use a wait group to wait for multiple goroutines to finish. We also learned how to launch several goroutines and increment the WaitGroup counter for each. Finally, we saw how to wait for all the goroutines launched to finish.
