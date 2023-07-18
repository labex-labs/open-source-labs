# Epoch

## Introduction

The Epoch lab is a Golang lab that aims to test your ability to get the number of seconds, milliseconds, or nanoseconds since the Unix epoch.

The problem to be solved in this lab is to write a Golang program that can calculate the number of seconds, milliseconds, or nanoseconds since the Unix epoch.

To complete this lab, you need to have a basic understanding of Golang and the following requirements:

- Familiarity with the `time` package in Golang.
- Knowledge of how to use the `Unix`, `UnixMilli`, and `UnixNano` functions in the `time` package.

## TODO

Complete the following code block to get the number of seconds, milliseconds, or nanoseconds since the Unix epoch:

```go
package main

import (
	"fmt"
	"time"
)

func main() {

	// Use `time.Now` with `Unix`, `UnixMilli` or `UnixNano`
	// to get elapsed time since the Unix epoch in seconds,
	// milliseconds or nanoseconds, respectively.
	now := time.Now()
	fmt.Println(now)

	fmt.Println(now.Unix())
	fmt.Println(now.UnixMilli())
	fmt.Println(now.UnixNano())

	// You can also convert integer seconds or nanoseconds
	// since the epoch into the corresponding `time`.
	fmt.Println(time.Unix(now.Unix(), 0))
	fmt.Println(time.Unix(0, now.UnixNano()))
}
```

```
2021-10-01 15:04:05.000000001 +0800 CST m=+0.000000002
1633086245
1633086245000
1633086245000000000
2021-10-01 15:04:05 +0800 CST
2021-10-01 15:04:05.000000001 +0800 CST
```

## Summary

The Epoch lab is a Golang lab that tests your ability to get the number of seconds, milliseconds, or nanoseconds since the Unix epoch. By completing this lab, you will gain a better understanding of the `time` package in Golang and how to use the `Unix`, `UnixMilli`, and `UnixNano` functions.
