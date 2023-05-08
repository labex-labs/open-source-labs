# Worker Pools

## Introduction
This challenge demonstrates how to implement a worker pool using goroutines and channels.

## Problem
Implement a worker pool that receives work on the `jobs` channel and sends the corresponding results on the `results` channel. The worker pool should have multiple concurrent instances, and each worker should sleep for a second per job to simulate an expensive task.

## Requirements
- Use goroutines and channels to implement the worker pool.
- The worker pool should have multiple concurrent instances.
- Each worker should sleep for a second per job to simulate an expensive task.
- The worker pool should receive work on the `jobs` channel and send the corresponding results on the `results` channel.

## TODO
```go
// TODO: Implement the worker function
func worker(id int, jobs <-chan int, results chan<- int) {
    // TODO: Receive work on the jobs channel
    // TODO: Simulate an expensive task by sleeping for a second per job
    // TODO: Send the corresponding result on the results channel
}

func main() {
    // TODO: Create channels for jobs and results
    // TODO: Start up multiple workers
    // TODO: Send work on the jobs channel
    // TODO: Collect results from the results channel
}
```

## Example
```
worker 3 started  job 1
worker 2 started  job 2
worker 1 started  job 3
worker 3 finished job 1
worker 3 started  job 4
worker 2 finished job 2
worker 1 finished job 3
worker 3 finished job 4
worker 2 started  job 5
worker 2 finished job 5
```

## Summary
This challenge demonstrated how to implement a worker pool using goroutines and channels. The worker pool receives work on the `jobs` channel and sends the corresponding results on the `results` channel. Each worker sleeps for a second per job to simulate an expensive task.