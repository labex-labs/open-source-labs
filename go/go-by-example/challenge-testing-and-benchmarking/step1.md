# Testing and Benchmarking

## Problem

The problem to be solved in this challenge is to test and benchmark a simple implementation of an integer minimum function named `IntMin`.

## Requirements

- The `testing` package must be imported.
- The `IntMin` function must take two integer parameters and return an integer.
- The `TestIntMinBasic` function must test the `IntMin` function for basic input values.
- The `TestIntMinTableDriven` function must test the `IntMin` function using a table-driven style.
- The `BenchmarkIntMin` function must benchmark the `IntMin` function.

## Example

```sh
# Run all tests in the current project in verbose mode.
$ go test -v
== RUN   TestIntMinBasic
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
PASS
ok  	examples/testing-and-benchmarking	0.023s

# Run all benchmarks in the current project. All tests
# are run prior to benchmarks. The `bench` flag filters
# benchmark function names with a regexp.
$ go test -bench=.
goos: darwin
goarch: arm64
pkg: examples/testing
BenchmarkIntMin-8 1000000000 0.3136 ns/op
PASS
ok  	examples/testing-and-benchmarking	0.351s

```
