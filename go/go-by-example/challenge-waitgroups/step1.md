# waitgroups

The problem to be solved in this challenge is to launch several goroutines and increment the WaitGroup counter for each. Then, we need to wait for all the goroutines launched to finish.

## Requirements

- Basic knowledge of Golang.
- Understanding of concurrency in Golang.
- Familiarity with the `sync` package.

## Example

```sh
$ go run waitgroups.go
Worker 5 starting
Worker 3 starting
Worker 4 starting
Worker 1 starting
Worker 2 starting
Worker 4 done
Worker 1 done
Worker 2 done
Worker 5 done
Worker 3 done

# The order of workers starting up and finishing
# is likely to be different for each invocation.
```
