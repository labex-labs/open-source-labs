# Goroutines

## Introduction
This challenge is designed to test your understanding of goroutines in Golang. Goroutines are lightweight threads of execution that allow for concurrent execution of functions.

## Problem
The problem to be solved in this challenge is to create and run goroutines to execute functions concurrently.

## Requirements
- The `f` function should print out its input string and a counter variable three times.
- The `main` function should call the `f` function synchronously and print out "direct" and a counter variable three times.
- The `main` function should call the `f` function asynchronously using a goroutine and print out "goroutine" and a counter variable three times.
- The `main` function should start a goroutine to execute an anonymous function that prints out a message.
- The `main` function should wait for the goroutines to finish executing before printing out "done".

## TODO
```
func f(from string) {
	for i := 0; i < 3; i++ {
		fmt.Println(from, ":", i)
	}
}

func main() {

	// Call f function synchronously
	f("direct")

	// Call f function asynchronously using a goroutine
	go f("goroutine")

	// Start a goroutine to execute an anonymous function
	go func(msg string) {
		fmt.Println(msg)
	}("going")

	// Wait for goroutines to finish executing
	time.Sleep(time.Second)
	fmt.Println("done")
}
```

## Example
```
direct : 0
direct : 1
direct : 2
going
goroutine : 0
goroutine : 1
goroutine : 2
done
```

## Summary
In this challenge, you learned how to create and run goroutines to execute functions concurrently. You also learned how to start a goroutine to execute an anonymous function and how to wait for goroutines to finish executing.