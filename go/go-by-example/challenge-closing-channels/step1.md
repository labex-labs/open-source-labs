# Closing Channels

## Problem

In this challenge, you need to modify the given code to close the `jobs` channel when there are no more jobs for the worker. You also need to use the `done` channel to notify when all the jobs have been completed.

## Requirements

- Use a buffered channel `jobs` to communicate work to be done from the `main()` goroutine to a worker goroutine.
- Use a channel `done` to notify when all the jobs have been completed.
- Use a worker goroutine to repeatedly receive from `jobs` with `j, more := <-jobs`.
- Use the special 2-value form of receive to notify on `done` when all the jobs have been completed.
- Send 3 jobs to the worker over the `jobs` channel, then close it.
- Use the [synchronization](channel-synchronization) approach to await the worker.

## Example

```sh
$ go run closing-channels.go
sent job 1
received job 1
sent job 2
received job 2
sent job 3
received job 3
sent all jobs
received all jobs

# The idea of closed channels leads naturally to our next
# example: `range` over channels.
```
