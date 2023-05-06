# Closing Channels

## Introduction
In Golang, closing a channel can be used to communicate completion to the channel's receivers. This challenge will demonstrate how to use a channel to communicate work to be done from the `main()` goroutine to a worker goroutine, and how to close the channel when there are no more jobs for the worker.

## Problem
In this challenge, you need to modify the given code to close the `jobs` channel when there are no more jobs for the worker. You also need to use the `done` channel to notify when all the jobs have been completed.

## Requirements
- Use a buffered channel `jobs` to communicate work to be done from the `main()` goroutine to a worker goroutine.
- Use a channel `done` to notify when all the jobs have been completed.
- Use a worker goroutine to repeatedly receive from `jobs` with `j, more := <-jobs`.
- Use the special 2-value form of receive to notify on `done` when all the jobs have been completed.
- Send 3 jobs to the worker over the `jobs` channel, then close it.
- Use the [synchronization](channel-synchronization) approach to await the worker.

## TODO
```go
// Here's the worker goroutine. It repeatedly receives
// from `jobs` with `j, more := <-jobs`. In this
// special 2-value form of receive, the `more` value
// will be `false` if `jobs` has been `close`d and all
// values in the channel have already been received.
// We use this to notify on `done` when we've worked
// all our jobs.
go func() {
    for {
        j, more := <-jobs
        if more {
            fmt.Println("received job", j)
        } else {
            fmt.Println("received all jobs")
            done <- true
            return
        }
    }
}()

// This sends 3 jobs to the worker over the `jobs`
// channel, then closes it.
for j := 1; j <= 3; j++ {
    jobs <- j
    fmt.Println("sent job", j)
}
close(jobs)
fmt.Println("sent all jobs")

// We await the worker using the
// [synchronization](channel-synchronization) approach
// we saw earlier.
<-done
```

## Example
```
sent job 1
received job 1
sent job 2
received job 2
sent job 3
received job 3
sent all jobs
received all jobs
```

## Summary
In this challenge, you learned how to use a channel to communicate work to be done from the `main()` goroutine to a worker goroutine, and how to close the channel when there are no more jobs for the worker. You also learned how to use the `done` channel to notify when all the jobs have been completed.