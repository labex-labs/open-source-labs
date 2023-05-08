# Execing Processes

## Problem

The problem is to replace the current Go process with another process, such as a non-Go process.

## Requirements

- Go programming language
- Basic knowledge of Go's `exec` function
- Familiarity with environment variables

## Example

```sh
# When we run our program it is replaced by `ls`.
$ go run execing-processes.go
total 16
drwxr-xr-x  4 mark 136B Oct 3 16:29 .
drwxr-xr-x 91 mark 3.0K Oct 3 12:50 ..
-rw-r--r--  1 mark 1.3K Oct 3 16:28 execing-processes.go

# Note that Go does not offer a classic Unix `fork`
# function. Usually this isn't an issue though, since
# starting goroutines, spawning processes, and exec'ing
# processes covers most use cases for `fork`.

```

## Solution

```go
// In the previous example we looked at
// [spawning external processes](spawning-processes). We
// do this when we need an external process accessible to
// a running Go process. Sometimes we just want to
// completely replace the current Go process with another
// (perhaps non-Go) one. To do this we'll use Go's
// implementation of the classic
// <a href="https://en.wikipedia.org/wiki/Exec_(operating_system)"><code>exec</code></a>
// function.

package main

import (
	"os"
	"os/exec"
	"syscall"
)

func main() {

	// For our example we'll exec `ls`. Go requires an
	// absolute path to the binary we want to execute, so
	// we'll use `exec.LookPath` to find it (probably
	// `/bin/ls`).
	binary, lookErr := exec.LookPath("ls")
	if lookErr != nil {
		panic(lookErr)
	}

	// `Exec` requires arguments in slice form (as
	// opposed to one big string). We'll give `ls` a few
	// common arguments. Note that the first argument should
	// be the program name.
	args := []string{"ls", "-a", "-l", "-h"}

	// `Exec` also needs a set of [environment variables](environment-variables)
	// to use. Here we just provide our current
	// environment.
	env := os.Environ()

	// Here's the actual `syscall.Exec` call. If this call is
	// successful, the execution of our process will end
	// here and be replaced by the `/bin/ls -a -l -h`
	// process. If there is an error we'll get a return
	// value.
	execErr := syscall.Exec(binary, args, env)
	if execErr != nil {
		panic(execErr)
	}
}

```