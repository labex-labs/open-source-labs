# Exit

The problem to be solved in this lab is to exit a Go program with a specific status code using the `os.Exit` function.

To complete this lab, you will need to have a basic understanding of Go programming and the `os` package.

```sh
#  If you run `exit.go` using `go run`, the exit
# will be picked up by `go` and printed.
$ go run exit.go
exit status 3

# By building and executing a binary you can see
# the status in the terminal.
$ go build exit.go
$ ./exit
$ echo $?
3

# Note that the `!` from our program never got printed.
```

There is the full code below:

```go
// Use `os.Exit` to immediately exit with a given
// status.

package main

import (
	"fmt"
	"os"
)

func main() {

	// `defer`s will _not_ be run when using `os.Exit`, so
	// this `fmt.Println` will never be called.
	defer fmt.Println("!")

	// Exit with status 3.
	os.Exit(3)
}

// Note that unlike e.g. C, Go does not use an integer
// return value from `main` to indicate exit status. If
// you'd like to exit with a non-zero status you should
// use `os.Exit`.

```
