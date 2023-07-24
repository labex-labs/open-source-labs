# `for`

## Introduction

This challenge aims to test your understanding of the `for` loop in Golang.

## Problem

The code below contains different types of `for` loops. However, some parts of the code are incomplete, and you need to fill in the blanks to make the code work correctly.

## Requirements

- Basic knowledge of Golang syntax
- Familiarity with `for` loops in Golang

## TODO

```go
// The most basic type, with a single condition.
i := 1
for i <= 3 {
    fmt.Println(i)
    i = i + 1
}

// A classic initial/condition/after `for` loop.
for j := 7; j <= 9; j++ {
    fmt.Println(j)
}

// `for` without a condition will loop repeatedly
// until you `break` out of the loop or `return` from
// the enclosing function.
for {
    fmt.Println("loop")
    break
}

// You can also `continue` to the next iteration of
// the loop.
for n := 0; n <= 5; n++ {
    if n%2 == 0 {
        continue
    }
    fmt.Println(n)
}
```

## Example

```
1
2
3
7
8
9
loop
1
3
5
```

## Summary

In this challenge, you learned about different types of `for` loops in Golang and how to use them. You also practiced filling in incomplete code blocks to make them work correctly.
