# Stateful Goroutines

## Problem

In concurrent programming, it is essential to synchronize access to shared state to avoid race conditions and data corruption. This challenge presents a scenario where a single goroutine owns the state, and other goroutines send messages to read or write the state.

## Requirements

- Use channels to issue read and write requests to the state-owning goroutine.
- Use `readOp` and `writeOp` structs to encapsulate requests and responses.
- Use a map to store the state.
- Use `resp` channels to indicate success and return values.
- Use `atomic` package to count read and write operations.
- Use `time` package to add a delay between operations.

## Example

```sh
# Running our program shows that the goroutine-based
# state management example completes about 80,000
# total operations.
$ go run stateful-goroutines.go
readOps: 71708
writeOps: 7177

# For this particular case the goroutine-based approach
# was a bit more involved than the mutex-based one. It
# might be useful in certain cases though, for example
# where you have other channels involved or when managing
# multiple such mutexes would be error-prone. You should
# use whichever approach feels most natural, especially
# with respect to understanding the correctness of your
# program.

```