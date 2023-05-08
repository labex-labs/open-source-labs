# Exit

## Problem

The problem to be solved in this challenge is to exit a Go program with a specific status code using the `os.Exit` function.

## Requirements

To complete this challenge, you will need to have a basic understanding of Go programming and the `os` package.

## Example

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