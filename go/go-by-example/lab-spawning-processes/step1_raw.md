# Spawning Processes

## Introduction

In some cases, Go programs need to spawn non-Go processes. This challenge aims to demonstrate how to spawn external processes in Go.

## Problem

The challenge requires the implementation of a Go program that spawns external processes and collects their output.

## Requirements

- The program should be able to spawn external processes.
- The program should be able to collect the output of the external processes.
- The program should handle errors that may arise during the execution of the external processes.

## TODO

```go
// TODO: Spawn an external process that takes no arguments or input and prints something to stdout.
// Use the `exec.Command` helper to create an object to represent this external process.
// Use the `Output` method to run the command, wait for it to finish, and collect its standard output.
dateCmd := exec.Command("date")
dateOut, err := dateCmd.Output()

// TODO: Spawn an external process that takes arguments and prints something to stdout.
// Use the `exec.Command` helper to create an object to represent this external process.
// Use the `Output` method to run the command, wait for it to finish, and collect its standard output.
// Handle errors that may arise during the execution of the command.
_, err = exec.Command("date", "-x").Output()

// TODO: Spawn an external process that takes input from stdin and prints something to stdout.
// Use the `exec.Command` helper to create an object to represent this external process.
// Use `StdinPipe` and `StdoutPipe` to grab input/output pipes.
// Write some input to the process, read the resulting output, and wait for the process to exit.
grepCmd := exec.Command("grep", "hello")
grepIn, _ := grepCmd.StdinPipe()
grepOut, _ := grepCmd.StdoutPipe()
grepCmd.Start()
grepIn.Write([]byte("hello grep\ngoodbye grep"))
grepIn.Close()
grepBytes, _ := io.ReadAll(grepOut)
grepCmd.Wait()

// TODO: Spawn an external process that takes a full command with a string.
// Use the `exec.Command` helper to create an object to represent this external process.
// Use the `Output` method to run the command, wait for it to finish, and collect its standard output.
// Handle errors that may arise during the execution of the command.
lsCmd := exec.Command("bash", "-c", "ls -a -l -h")
lsOut, err := lsCmd.Output()
```

## Example

```
> date
Thu Sep  2 14:22:44 CST 2021

failed executing: exec: "date": executable file not found in $PATH
command exit rc = 1

> grep hello
hello grep

> ls -a -l -h
total 24K
drwxr-xr-x 1 root root 4.0K Sep  2 14:22 .
drwxr-xr-x 1 root root 4.0K Sep  2 14:22 ..
-rw-r--r-- 1 root root  193 Sep  2 14:22 main.go
-rwxr-xr-x 1 root root  13K Sep  2 14:22 main
```

## Summary

This challenge demonstrated how to spawn external processes in Go using the `exec` package. The program was able to spawn external processes that take no arguments or input, take arguments and print something to stdout, take input from stdin and print something to stdout, and take a full command with a string. The program also handled errors that may arise during the execution of the external processes.
