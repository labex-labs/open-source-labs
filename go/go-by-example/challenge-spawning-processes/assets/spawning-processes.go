// Sometimes our Go programs need to spawn other, non-Go
// processes.

package main

import (
	"fmt"
	"io"
	"os/exec"
)

func main() {
    // TODO
	// We'll start with a simple command that takes no
	// arguments or input and just prints something to
	// stdout. The `exec.Command` helper creates an object
	// to represent this external process.
	// The `Output` method runs the command, waits for it
	// to finish and collects its standard output.
	//  If there were no errors, `dateOut` will hold bytes
	// with the date info.
	// `Output` and other methods of `Command` will return
	// `*exec.Error` if there was a problem executing the
	// command (e.g. wrong path), and `*exec.ExitError`
	// if the command ran but exited with a non-zero return
	// code.
	// Next we'll look at a slightly more involved case
	// where we pipe data to the external process on its
	// `stdin` and collect the results from its `stdout`.
	// Here we explicitly grab input/output pipes, start
	// the process, write some input to it, read the
	// resulting output, and finally wait for the process
	// to exit.
	// We omitted error checks in the above example, but
	// you could use the usual `if err != nil` pattern for
	// all of them. We also only collect the `StdoutPipe`
	// results, but you could collect the `StderrPipe` in
	// exactly the same way.
	// Note that when spawning commands we need to
	// provide an explicitly delineated command and
	// argument array, vs. being able to just pass in one
	// command-line string. If you want to spawn a full
	// command with a string, you can use `bash`'s `-c`
	// option:
}
