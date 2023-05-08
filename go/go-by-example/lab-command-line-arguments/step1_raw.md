# Command-line arguments

## Introduction

The purpose of this challenge is to practice working with command-line arguments in Golang.

## Problem

The program currently prints out the raw command-line arguments passed to it. However, it needs to be modified to print out specific arguments based on their index.

## Requirements

- Basic knowledge of Golang
- Familiarity with command-line arguments

## TODO

```go
func main() {

	// `os.Args` provides access to raw command-line
	// arguments. Note that the first value in this slice
	// is the path to the program, and `os.Args[1:]`
	// holds the arguments to the program.
	argsWithProg := os.Args
	argsWithoutProg := os.Args[1:]

	// TODO: Print out the first argument passed to the program
	// TODO: Print out the second argument passed to the program
	// TODO: Print out the third argument passed to the program

	fmt.Println(argsWithProg)
	fmt.Println(argsWithoutProg)
}
```

## Example

Assuming the program is called `args.go` and is run with the following command:

```
go run args.go foo bar baz
```

The program should output:

```
foo
bar
baz
```

## Summary

In this challenge, we learned how to access and print out specific command-line arguments in Golang. By using the `os.Args` variable and indexing into it, we can easily access the arguments passed to the program.
