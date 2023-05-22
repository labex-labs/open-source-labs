# Random Numbers

## Introduction

This challenge aims to test your ability to generate random numbers using the `math/rand` package in Golang.

## Problem

You are required to write a program that generates random integers and floats within a specified range. The program should also be able to produce varying sequences of numbers by changing the seed.

## Requirements

- The program should use the `math/rand` package to generate random numbers.
- The program should generate random integers within a specified range.
- The program should generate random floats within a specified range.
- The program should be able to produce varying sequences of numbers by changing the seed.

## TODO

Complete the following code blocks to meet the requirements of the challenge:

```go
// Generate a random integer between 0 and 100 (inclusive)
rand.Intn(100)

// Generate a random float between 0.0 and 1.0 (exclusive)
rand.Float64()

// Generate a random float between 5.0 and 10.0 (exclusive)
(rand.Float64() * 5) + 5

// Generate a new random number generator with a seed that changes
rand.NewSource(time.Now().UnixNano())
rand.New(s1)

// Generate a new random number generator with a fixed seed
rand.NewSource(42)
rand.New(s2)
```

## Example

```
81,87
0.6645600532184904
9.188124246731327,7.948268578674167
73,6
81,87
81,87
```

## Summary

This challenge requires you to generate random numbers using the `math/rand` package in Golang. You should be able to generate random integers and floats within a specified range and produce varying sequences of numbers by changing the seed.
