# Execing Processes

## Introduction

This lab focuses on replacing the current Go process with another process using Go's implementation of the classic `exec` function.

The problem is to replace the current Go process with another process, such as a non-Go process.

- Go programming language
- Basic knowledge of Go's `exec` function
- Familiarity with environment variables

## TODO

Complete the code block below by using Go's `exec` function to replace the current Go process with the `ls` command.

```go
package main

import (
	"os"
	"os/exec"
	"syscall"
)

func main() {

	binary, lookErr := exec.LookPath("ls")
	if lookErr != nil {
		panic(lookErr)
	}

	args := []string{"ls", "-a", "-l", "-h"}

	env := os.Environ()

	// TODO: Use Go's exec function to replace the current process with the ls command
	execErr := syscall.Exec(binary, args, env)
	if execErr != nil {
		panic(execErr)
	}
}
```

```
$ go run main.go
total 16
drwxr-xr-x  4 user  staff   128B Aug  4 16:29 .
drwxr-xr-x  5 user  staff   160B Aug  4 16:29 ..
-rw-r--r--  1 user  staff   1.1K Aug  4 16:29 main.go
```

## Summary

In this lab, we learned how to replace the current Go process with another process using Go's implementation of the classic `exec` function. This can be useful when we need to execute a non-Go process from within a Go program.
