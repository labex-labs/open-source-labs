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
    // TODO
	// For our example we'll exec `ls`. Go requires an
	// absolute path to the binary we want to execute, so
	// we'll use `exec.LookPath` to find it (probably
	// `/bin/ls`).
	// `Exec` requires arguments in slice form (as
	// opposed to one big string). We'll give `ls` a few
	// common arguments. Note that the first argument should
	// be the program name.
	// `Exec` also needs a set of [environment variables](environment-variables)
	// to use. Here we just provide our current
	// environment.
	// Here's the actual `syscall.Exec` call. If this call is
	// successful, the execution of our process will end
	// here and be replaced by the `/bin/ls -a -l -h`
	// process. If there is an error we'll get a return
	// value.
}
