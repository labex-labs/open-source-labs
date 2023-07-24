# Stateful Goroutines

## Introduction

This lab aims to demonstrate how to use channels and goroutines to synchronize access to shared state across multiple goroutines.

In concurrent programming, it is essential to synchronize access to shared state to avoid race conditions and data corruption. This lab presents a scenario where a single goroutine owns the state, and other goroutines send messages to read or write the state.

- Use channels to issue read and write requests to the state-owning goroutine.
- Use `readOp` and `writeOp` structs to encapsulate requests and responses.
- Use a map to store the state.
- Use `resp` channels to indicate success and return values.
- Use `atomic` package to count read and write operations.
- Use `time` package to add a delay between operations.

## TODO

Complete the following code blocks:

```go
type readOp struct {
	key  int
	resp chan int
}
type writeOp struct {
	key  int
	val  int
	resp chan bool
}

go func() {
	var state = make(map[int]int)
	for {
		select {
		case read := <-reads:
			read.resp <- state[read.key]
		case write := <-writes:
			state[write.key] = write.val
			write.resp <- true
		}
	}
}()

for r := 0; r < 100; r++ {
	go func() {
		for {
			read := readOp{
				key:  rand.Intn(5),
				resp: make(chan int)}
			reads <- read
			<-read.resp
			atomic.AddUint64(&readOps, 1)
			time.Sleep(time.Millisecond)
		}
	}()
}

for w := 0; w < 10; w++ {
	go func() {
		for {
			write := writeOp{
				key:  rand.Intn(5),
				val:  rand.Intn(100),
				resp: make(chan bool)}
			writes <- write
			<-write.resp
			atomic.AddUint64(&writeOps, 1)
			time.Sleep(time.Millisecond)
		}
	}()
}
```

```
readOps: 1000
writeOps: 100
```

## Summary

This lab demonstrated how to use channels and goroutines to synchronize access to shared state. By having a single goroutine own the state and using channels to issue read and write requests, we can avoid race conditions and data corruption.
