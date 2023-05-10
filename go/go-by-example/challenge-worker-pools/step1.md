# Worker Pools

## Problem

Implement a worker pool that receives work on the `jobs` channel and sends the corresponding results on the `results` channel. The worker pool should have multiple concurrent instances, and each worker should sleep for a second per job to simulate an expensive task.

## Requirements

- Use goroutines and channels to implement the worker pool.
- The worker pool should have multiple concurrent instances.
- Each worker should sleep for a second per job to simulate an expensive task.
- The worker pool should receive work on the `jobs` channel and send the corresponding results on the `results` channel.

## Example

```sh
# Our running program shows the 5 jobs being executed by
# various workers. The program only takes about 2 seconds
# despite doing about 5 seconds of total work because
# there are 3 workers operating concurrently.
$ time go run worker-pools.go
worker 1 started job 1
worker 2 started job 2
worker 3 started job 3
worker 1 finished job 1
worker 1 started job 4
worker 2 finished job 2
worker 2 started job 5
worker 3 finished job 3
worker 1 finished job 4
worker 2 finished job 5

real 0m2.358s
```
