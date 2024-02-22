# Command-line arguments

The program currently prints out the raw command-line arguments passed to it. However, it needs to be modified to print out specific arguments based on their index.

## Requirements

- Basic knowledge of Golang
- Familiarity with command-line arguments

## Example

```sh
# To experiment with command-line arguments it's best to
# build a binary with `go build` first.
$ go build command-line-arguments.go
$ ./command-line-arguments a b c d
[./command-line-arguments a b c d]
[a b c d]
c

# Next we'll look at more advanced command-line processing
# with flags.
```
