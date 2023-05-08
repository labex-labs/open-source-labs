# Testing and Benchmarking

## Introduction
This challenge aims to demonstrate the importance of unit testing and benchmarking in writing principled Go programs. The `testing` package provides the tools needed to write unit tests, and the `go test` command runs tests.

## Problem
The problem to be solved in this challenge is to test and benchmark a simple implementation of an integer minimum function named `IntMin`.

## Requirements
- The `testing` package must be imported.
- The `IntMin` function must take two integer parameters and return an integer.
- The `TestIntMinBasic` function must test the `IntMin` function for basic input values.
- The `TestIntMinTableDriven` function must test the `IntMin` function using a table-driven style.
- The `BenchmarkIntMin` function must benchmark the `IntMin` function.

## TODO
```go
// TODO: Write a test function named TestIntMinBasic to test the IntMin function for basic input values.

// TODO: Write a test function named TestIntMinTableDriven to test the IntMin function using a table-driven style.

// TODO: Write a benchmark function named BenchmarkIntMin to benchmark the IntMin function.
```

## Example
```
$ go test -v
=== RUN   TestIntMinBasic
--- PASS: TestIntMinBasic (0.00s)
=== RUN   TestIntMinTableDriven
=== RUN   TestIntMinTableDriven/0,1
=== RUN   TestIntMinTableDriven/1,0
=== RUN   TestIntMinTableDriven/2,-2
=== RUN   TestIntMinTableDriven/0,-1
=== RUN   TestIntMinTableDriven/-1,0
--- PASS: TestIntMinTableDriven (0.00s)
    --- PASS: TestIntMinTableDriven/0,1 (0.00s)
    --- PASS: TestIntMinTableDriven/1,0 (0.00s)
    --- PASS: TestIntMinTableDriven/2,-2 (0.00s)
    --- PASS: TestIntMinTableDriven/0,-1 (0.00s)
    --- PASS: TestIntMinTableDriven/-1,0 (0.00s)
goos: darwin
goarch: amd64
pkg: example
BenchmarkIntMin-8   	1000000000	         0.0000001 ns/op
PASS
ok  	example	0.002s
```

## Summary
This challenge demonstrated how to write unit tests and benchmark functions using the `testing` package in Go. The `TestIntMinBasic` function tested the `IntMin` function for basic input values, while the `TestIntMinTableDriven` function used a table-driven style to test the `IntMin` function. The `BenchmarkIntMin` function benchmarked the `IntMin` function to measure its performance.